#!/usr/bin/env python3
"""Check links in this repo's HTML.

Local links are resolved per site directory (root/, mila/, drae/). Root
pages use extensionless URLs such as /privacy, which map to privacy.html.
root/_redirects is applied before a root-site target is reported missing.

Remote http(s) links are requested once each. 404 and 410 fail the run.
401, 403, 429, and 503 are reported and ignored, because those hosts often
block a checker. Other HTTP errors fail. Set CHECK_EXTERNAL=0 to skip
remote requests.
"""

from __future__ import annotations

import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITES = ("root", "mila", "drae")
HOST_TO_SITE = {
    "milatech.tech": "root",
    "www.milatech.tech": "root",
    "mila.milatech.tech": "mila",
    "drae.milatech.tech": "drae",
}
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")
SOFT_HTTP = {401, 403, 429, 503}
CHECK_EXTERNAL = os.environ.get("CHECK_EXTERNAL", "1") != "0"
UA = "Mozilla/5.0 (compatible; MilaTechLinkCheck/1.0; +https://milatech.tech/)"


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        wanted = {"href", "src", "poster"}
        if tag not in {"a", "link", "script", "img", "source", "video", "iframe", "audio"}:
            return
        line = self.getpos()[0]
        for name, value in attrs:
            if name in wanted and value:
                self.links.append((line, value.strip()))


def load_redirects() -> dict[str, str]:
    path = ROOT / "root" / "_redirects"
    rules: dict[str, str] = {}
    if not path.exists():
        return rules
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        source = parts[0] if parts[0].startswith("/") else "/" + parts[0]
        rules[source.rstrip("/") or "/"] = parts[1]
    return rules


def site_of(html_path: Path) -> str | None:
    try:
        rel = html_path.relative_to(ROOT)
    except ValueError:
        return None
    if not rel.parts:
        return None
    return rel.parts[0] if rel.parts[0] in SITES else None


def local_candidates(site: str, url_path: str) -> list[Path]:
    base = ROOT / site
    path = urllib.parse.unquote(url_path)
    if path.startswith("/"):
        path = path[1:]
    rels = []
    if path in ("", "/"):
        rels.append("index.html")
    else:
        trimmed = path[1:] if path.startswith("/") else path
        if trimmed.endswith("/"):
            rels.append(trimmed + "index.html")
            trimmed = trimmed.rstrip("/")
        rels.append(trimmed)
        if not trimmed.endswith(".html"):
            rels.append(trimmed + ".html")
            rels.append(trimmed + "/index.html")
    found = []
    for rel in rels:
        candidate = (base / rel).resolve()
        try:
            candidate.relative_to(base.resolve())
        except ValueError:
            continue
        found.append(candidate)
    return found


def exists_local(site: str, url_path: str) -> bool:
    return any(path.is_file() for path in local_candidates(site, url_path))


def exists_relative(html_path: Path, url_path: str) -> bool:
    """Resolve a same-directory link (styles.css, terms.html, assets/x)."""
    path = urllib.parse.unquote(url_path)
    if path.startswith("/"):
        return False
    base = html_path.parent
    rels = [path]
    trimmed = path[:-1] if path.endswith("/") else path
    if path.endswith("/"):
        rels.append(trimmed + "/index.html")
    if trimmed and not trimmed.endswith(".html"):
        rels.append(trimmed + ".html")
        rels.append(trimmed + "/index.html")
    root_resolved = ROOT.resolve()
    for rel in rels:
        candidate = (base / rel).resolve()
        try:
            candidate.relative_to(root_resolved)
        except ValueError:
            continue
        if candidate.is_file():
            return True
    return False


def apply_redirect(site: str, url_path: str, redirects: dict[str, str]) -> tuple[str, str] | None:
    """Return (site, path) or ('remote', absolute_url) after one redirect."""
    if site != "root":
        return None
    key = url_path if url_path.startswith("/") else "/" + url_path
    key = key.split("?", 1)[0].split("#", 1)[0]
    key = key.rstrip("/") or "/"
    target = redirects.get(key)
    if not target:
        return None
    if target.startswith("/"):
        return ("root", target)
    parsed = urllib.parse.urlparse(target)
    mapped = HOST_TO_SITE.get(parsed.netloc.lower())
    if mapped:
        return (mapped, parsed.path or "/")
    return ("remote", target)


def check_remote(url: str, cache: dict[str, str]) -> str | None:
    if url in cache:
        return cache[url]
    request = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    context = ssl.create_default_context()
    error: str | None = None
    for _ in range(2):
        try:
            with urllib.request.urlopen(request, timeout=20, context=context) as response:
                status = getattr(response, "status", 200)
                if status in SOFT_HTTP:
                    error = None
                elif status >= 400:
                    error = f"HTTP {status}"
                else:
                    error = None
                break
        except urllib.error.HTTPError as exc:
            if exc.code in SOFT_HTTP:
                error = None
                break
            if exc.code in (404, 410):
                error = f"HTTP {exc.code}"
                break
            error = f"HTTP {exc.code}"
        except Exception as exc:  # noqa: BLE001 — report the network failure
            error = str(exc)
    cache[url] = error or ""
    return error


def main() -> int:
    redirects = load_redirects()
    failures: list[str] = []
    remote_cache: dict[str, str] = {}
    html_files = sorted(ROOT.glob("*/*.html")) + sorted(ROOT.glob("*/*/*.html"))
    checked = 0
    for html_path in html_files:
        site = site_of(html_path)
        if site is None:
            continue
        parser = LinkExtractor()
        try:
            parser.feed(html_path.read_text(encoding="utf-8"))
        except UnicodeError as exc:
            failures.append(f"{html_path.relative_to(ROOT)}: cannot read ({exc})")
            continue
        for line, raw in parser.links:
            checked += 1
            if raw.startswith("#") or raw.lower().startswith(SKIP_SCHEMES):
                continue
            parsed = urllib.parse.urlparse(raw)
            where = f"{html_path.relative_to(ROOT)}:{line}"
            if parsed.scheme in ("http", "https"):
                mapped = HOST_TO_SITE.get(parsed.netloc.lower())
                if mapped:
                    target_site, target_path = mapped, parsed.path or "/"
                    redirected = apply_redirect(target_site, target_path, redirects)
                    if redirected and redirected[0] == "remote":
                        if CHECK_EXTERNAL:
                            problem = check_remote(redirected[1], remote_cache)
                            if problem:
                                failures.append(f"{where}: {raw} -> {redirected[1]} ({problem})")
                        continue
                    if redirected:
                        target_site, target_path = redirected
                    if not exists_local(target_site, target_path):
                        failures.append(f"{where}: {raw} (no file under {target_site}/)")
                elif CHECK_EXTERNAL:
                    problem = check_remote(raw.split("#", 1)[0], remote_cache)
                    if problem:
                        failures.append(f"{where}: {raw} ({problem})")
                continue
            if parsed.scheme:
                failures.append(f"{where}: unsupported link {raw}")
                continue
            path = parsed.path
            if path.startswith("/"):
                target_site = site
                redirected = apply_redirect(site, path, redirects)
                if redirected and redirected[0] == "remote":
                    if CHECK_EXTERNAL:
                        problem = check_remote(redirected[1], remote_cache)
                        if problem:
                            failures.append(f"{where}: {raw} -> {redirected[1]} ({problem})")
                    continue
                if redirected:
                    target_site, path = redirected
                if not exists_local(target_site, path):
                    failures.append(f"{where}: {raw} (no file under {target_site}/)")
            elif not exists_relative(html_path, path):
                failures.append(f"{where}: {raw} (missing relative to {html_path.parent.relative_to(ROOT)})")

    print(f"Checked {checked} links in {len(html_files)} HTML files.")
    if failures:
        print(f"{len(failures)} broken link(s):", file=sys.stderr)
        for item in failures:
            print(f"  {item}", file=sys.stderr)
        return 1
    print("No broken links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
