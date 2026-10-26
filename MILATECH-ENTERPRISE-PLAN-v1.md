# MILATECH.TECH — Enterprise Plan v1
**Date:** 2026-10-26 · **Authority:** Edward's order, 2026-10-26 13:58 EDT: "Also do it to milatech.tech." — the same enterprise treatment given to MILA, Owed, and DRAE today.
**Standing rule applied:** Act on authorized no-cost work and report. Only spend decisions, legal attestations, and physical steps go to Edward.

---

## 0. The forcing fact

milatech.tech is in Google AdSense status **"Needs attention — Low value content"** (Google updated Oct 22, 2026; publisher ca-pub-3173775162505932; ads.txt Authorized; payments complete). **No ads serve on any Mila Tech site until this domain gains substantive content and passes a re-requested review.**

So the enterprise rebuild and the AdSense unblock are the same job. Every substantive page built for enterprise credibility also counts toward Google's review. No separate "SEO content" track — one build, two payoffs.

**Edward's locked follow-on:** the moment the domain is approved, enable Auto-ads **Side rails (desktop left/right)** for milatech.tech in AdSense settings. That setting is locked until approval — it is step 1 after approval, not before.

---

## 1. Honest audit — where the site stood on 2026-10-26

Visible-text word counts (root domain — the domain Google judges as a whole):

| Page | Words | Verdict |
|---|---|---|
| index.html (Home) | ~1,062 incl. Daily Updates feed | Strongest page, but much of it is a changelog, not company substance |
| products.html | ~519 | Real lineup, thin on proof, use cases, and enterprise routing |
| about.html | ~295 | **Thin.** Two short paragraphs + a leadership blurb for a whole company |
| support.html | ~231 | **Thin.** Mostly a $0 donation panel + a mailto — not support content |
| drae.html | 15 | Redirect stub to drae.milatech.tech — correct, excluded from judgment |
| **Root total** | **~2,100** | **Classic low-value pattern: templated landing copy, no long-form, no services, no insights, no lead capture** |

What was already good and is kept untouched in spirit: family bar + visit counter + AdSense script on every page, the makeover design system (dark ink #0A0614 / brand #7A25F4), Daily Updates on Home and Fix Tracker on the MILA site (byte-identical sections preserved), honest pricing ($2.99/mo · $19.99/yr; coin packs as locked), honest DRAE pre-revenue wording.

What was missing entirely: a Services offer, a Contact/lead pipeline (a mailto is not a pipeline), any long-form editorial content, product pages that route enterprise buyers to MILA for Brands / Owed Enterprise / DRAE pilots, and any reason for Google — or a buyer — to believe this is an operating software company rather than a link farm.

Subdomains are comparatively rich (MILA site, Owed, DRAE) but **do not cure a thin root** — Google judges milatech.tech itself.

---

## 2. Positioning

**Mila Tech LLC is a builder-led software company in Troy, Michigan that finds friction in everyday systems and engineers it out — and sells what it builds.**

- **Legal/company facts (verified, used as proof):** Mila Tech LLC, a Delaware limited liability company (DE file no. 10721454, formed Aug 3, 2026), operated from Troy / Metro Detroit, Michigan. Managing member: Edward Emilio Issa. Business contact: edward@milatech.tech (Google Workspace, live since Oct 4, 2026).
- **What it builds:** consumer software (MILA), money-recovery automation (Owed), ML/agent governance software (DRAE), plus an operating business (Lock & Go Storage LLC) run with the same systems mindset.
- **Who it serves:** (1) consumers who vote, claim money, and run daily life; (2) brands, employers, credit unions, and media who need real-time sentiment and money-found-for-people as a product; (3) operations-heavy businesses that need workflow automation built by someone who has run the floor, not just studied it.
- **Proof posture:** live products with real URLs, a public bug-hunt Fix Tracker (447+ issues found and fixed across rounds), published Daily Updates, reproducible DRAE benchmarks (85.6% lower error than a static ensemble under model corruption, 19 passing tests), and a filed-real-claim record at Owed (Bestway filed 2026-10-26). No invented customers, no ARR, no testimonials that don't exist. Pre-revenue stays labeled pre-revenue.
- **Founder identity point (Edward's own, for public bios):** all of his technical talent is **self-taught** — software architect, hardware engineer, PMP, BS Finance, GED at 17, wholesale mortgage front-end operations by day. That story is a differentiator for a services buyer: the person selling the automation has done the manual job.

**Tagline kept:** "Tomorrow's technology, built for life on Earth." It now sits on top of substance instead of substituting for it.

---

## 3. Pages — the new sitemap (root domain)

Every page: family bar + visit counter + AdSense script (shared pattern, non-negotiable), substantive copy (target ≥700 words of visible, original text on core pages), and a closing next step (lead form, product CTA, or article path). No dead-end pages.

| Page | Job | Target |
|---|---|---|
| **Home** (`index.html`) | Company front door: what Mila Tech is, the three products with enterprise routes, services teaser, proof strip, Insights preview, lead CTA. Daily Updates section preserved byte-identical. | ~1,400 words + updates feed |
| **Products** (`products.html`) | Full lineup with use cases and buyer routing: MILA → MILA for Brands / sentiment; Owed → Owed Enterprise; DRAE → pilot / acquisition; Lock & Go; capabilities; R&D pipeline (honestly labeled concepts). | ~1,100 words |
| **About** (`about.html`) | A company, not a blurb: story, operating loop, timeline, Delaware/Troy facts, leadership with the self-taught founder story, how the company makes money (honestly), contact CTA. | 800–1,000 words |
| **Services** (`services.html`) — NEW | Edward's billable expertise packaged: (1) Mortgage workflow automation, (2) ML & predictive diagnostics, (3) Product engineering (concept → shipped product). Each with deliverables, process, engagement models, and a lead-form CTA. No hourly rate published — "scoped quote after a working call" until Edward sets rates. | ~900 words |
| **Insights** (`insights.html`) — NEW | The content engine home: article index with real excerpts, category filters by product line, newsletter/lead path. | Index + articles |
| **Insights articles** (3 at launch, see §5) | Long-form, original, educational — the exact material Google's review and category search both reward. Each ends with the matching product's enterprise CTA. | 700–1,000 words each |
| **Support** (`support.html`) | Real support utility: per-product help routes, response expectations, beta/Owed/DRAE FAQs, status pointers — plus the community-support panel kept. Utility content weighs heavily with reviewers. | 700+ words |
| **Contact** (`contact.html`) — NEW | The lead pipeline's front door: one form (name, work email, company, interest, seats/size where relevant, message) POSTing to the durable endpoint (§4), with mailto fallback so a down API never swallows a lead. Plus direct routes per product. | Form + routing copy |

Navigation (all root pages): Home · Products · Services · Insights · About · Support · Contact (CTA). Footer gains Services / Insights / Contact. Family bar unchanged.

---

## 4. Lead pipeline

**Pattern reused:** Owed Enterprise's proven pattern (live 2026-10-26) — public form → `POST https://api.owed.milatech.tech/enterprise-leads` → D1 `enterprise_leads` table + audit log. Fields accepted today: `company, name, email, segment, seats, message`.

**Milatech.tech usage (no new backend needed):**
- `segment` values: `milatech-services`, `mila-brands`, `owed-enterprise`, `drae-pilot`, `general`, `press`.
- `message` carries the structured detail (interest, timeline, page source) until/unless a dedicated `milatech-leads` endpoint is warranted.
- **Graceful degradation, same as Owed:** if the API doesn't answer, the form reveals a prefilled `mailto:edward@milatech.tech` fallback with all fields in the body. A lead is never lost to a down Worker.
- Every page ends in a next step: Services → lead form; product sections → that product's enterprise page (MILA site / owed.milatech.tech/enterprise / drae.milatech.tech) or the Contact form pre-set to its segment; articles → matching product CTA + Contact.
- Response promise published on Contact/Support: business inquiries answered within **2 business days** (a promise the current one-person operation can keep; tighten only when reality allows).
- No lead data is sold, ever — stated on the form, matching the Owed brand rule.

**Future (not blocking):** a dedicated leads inbox view / Resend notification on new lead, once the Resend key Edward gates for Owed lands — the same key unlocks both.

---

## 5. Content engine

**Cadence:** 2 substantive articles per month minimum, published to Insights, each 700–1,200 words, each tied to a category Mila Tech sells into. Quality and factual honesty over volume — no AI-slop farm; Google's review and Edward's brand both punish that, and every claim in an article must trace to a product Mila Tech actually ships or a process it actually runs.

**Launch set (shipping with this rebuild, drafts matured from the 2026-10-26 AdSense content pack):**
1. **"Why Most Settlement Money Is Never Claimed — and How to Claim Yours"** — money-recovery category → Owed / Owed Enterprise.
2. **"Guest Voting: What Happens When a Poll Needs No Account"** — polling/sentiment category, build-in-public engineering note → MILA / MILA for Brands.
3. **"Model Drift Is a Governance Problem, Not Just a Data Problem"** — ML safety category → DRAE pilots.

**Standing categories / next queue:**
- Polling & sentiment: what real-time sentiment can/can't tell a brand; how Daily One-style rituals create a panel.
- Money recovery: unclaimed property by state (MI/FL first); settlement deadlines explained; the intake-first filing method.
- ML safety: ensemble disagreement as a signal; fail-closed design; audit trails for model decisions.
- Build-in-public: MILA bug-hunt method (rounds, forced-failure testing); Owed's one-tap doctrine; shipping on Cloudflare Workers as a one-person company.
- Mortgage operations: workflow automation field notes (no employer-confidential material, ever).

**Distribution:** each article linked from Home's Insights preview, the matching product page, and one MILA/Owed/DRAE social post inside the existing 3/day/platform cap and fleet rules. Articles are the re-review evidence, the search assets, and the sales collateral — one artifact, three jobs.

---

## 6. Revenue paths (in the order they can actually turn on)

1. **Services engagements** — the fastest enterprise dollar: scoped automation/diagnostics/engineering projects from the Services page + lead form. Pricing is scoped per engagement until Edward sets a rate card (his call, §8).
2. **Product enterprise routes fed by this site:** MILA for Brands (sponsored polls + sentiment reporting), Owed Enterprise (employers $2 PEPM test / credit unions / tax pros), DRAE (pilot / license / $2,500 outright sale as currently offered). The company site's job is to make each of those look like it comes from a real company — because it does.
3. **Consumer product revenue** (already priced, not this site's job to re-price): MILA Premium $2.99/mo · $19.99/yr + coin packs; Owed subscription $6.99/mo behind its Stripe gate.
4. **AdSense** — unlocked by this rebuild + re-review; then Side rails ON per Edward's instruction. Honest expectation: pocket change at current traffic (~650 visits across the family on 2026-10-26 seed counts). Managed, never the strategy.
5. **Community support** — the Support page's donation panel stays ($0 raised to date, stated honestly).

---

## 7. Sequence

1. ✅ Audit (this plan, §1) — done 2026-10-26.
2. ✅ This plan — one shot, complete.
3. Build: expand About + Support; new Services, Contact, Insights + 3 launch articles; upgrade Home + Products (enterprise routing, proof, Insights preview); nav/footer updated on every root page; forms wired to the lead endpoint with mailto fallback.
4. Verify: every root page checked for family bar, visit counter, AdSense script, word count, working internal links, and form fallback; Daily Updates markup untouched.
5. Deploy: commit + push to `main` (root/ is Git-connected to the `milatech-root` Worker — push auto-deploys); verify live on milatech.tech.
6. **AdSense re-review:** only after step 5 is live and verified — request the review in the AdSense dashboard (Sites → milatech.tech → Request review). Prepared as a one-tap for Edward in his signed-in session.
7. **On approval (Edward's explicit ask):** enable Auto-ads Side rails for milatech.tech; confirm ads serving on all four family sites; announce in Daily Updates.
8. Ongoing: 2 articles/month; lead response within 2 business days; monthly check that pricing/proof claims on the site still match the products' live state.

---

## 8. Decisions for Edward (surfaced, not silently made)

1. **⚠️ COPY TRUTH — the one flagged decision.** About and Support currently say **"no ads-first roadmap / no selling your attention"** while an AdSense script runs on every page. Those words were Edward's, so this build **does not silently rewrite them** — they are preserved in the shipped pages and flagged here. Options when he decides:
   - **(a) Recommended:** replace with product-truth copy — e.g. "funded by its products and its community; free sites carry clearly-labeled advertising so the tools stay free — never by selling user data." (Drafted in the 2026-10-26 content pack.)
   - **(b)** Keep the lines and drop AdSense from milatech.tech (ads then can't be the unblock path; enterprise/services become the whole story).
   - **(c)** Keep both as-is and accept the inconsistency.
   Until he picks, the contradiction stays visible in this plan — and Google's reviewer will see the same pages either way, so (a) before the re-review request is the safer sequence.
2. **Services rate card:** publish scoped-quote-only (current build) or set public starting prices? Needs Edward's numbers.
3. **Re-review timing:** request as soon as this rebuild is live, or after decision (1) is made? Recommendation: decide (1) first — it's a 2-minute call and removes the only self-contradiction a reviewer could flag.

Everything else in this plan is no-cost build/operate work and proceeds under the standing go.

---

## 9. Targets

- **At deploy:** root domain ≥ 8,000 words of original, substantive content (from ~2,100); 8 indexable core pages (from 4); a working lead form on Contact + Services; 3 published articles.
- **AdSense:** re-review requested within 24h of deploy + Edward's copy decision; approval = ads live family-wide + Side rails enabled same day.
- **Leads:** first qualified services/enterprise lead within 30 days of deploy; 100% of form submissions durable in D1 or delivered by mailto fallback (zero silent losses — test-submitted at build).
- **Content:** 2 articles/month sustained; Insights = top-3 landing source for milatech.tech within 90 days (visit counter + Cloudflare analytics as the measure).
- **Trust:** zero invented claims on the site at any audit — customers, revenue, and results appear only when real and citable.

*Plan owner: the Mila Tech chat (6b42cb75-fbfb-42da-a2ae-b39b829d197b). Companion file: `adsense-content-pack-2026-10-26.md` (audit + article drafts this plan matures into shipped pages).*
