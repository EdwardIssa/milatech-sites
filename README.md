# milatech-sites


Source for Mila Tech LLC's websites, deployed via Cloudflare Workers (Static Assets) with GitHub-connected continuous deployment.


## Structure


Every site is multi-page with a shared top navigation bar and footer — no one-pagers.

- `root/` → **https://milatech.tech** — Mila Tech LLC company site
  - `index.html` — Home (hero, venture/product cards, Daily Updates)
  - `products.html` — Products (lineup, capabilities, R&D pipeline)
  - `about.html` — About (company, leadership)
  - `support.html` — Support (per-product help, FAQ, community donations, contact)
  - `services.html` — Services (mortgage workflow automation, ML & predictive diagnostics, product engineering; lead form)
  - `contact.html` — Contact (lead form → Owed enterprise-leads endpoint in D1, mailto fallback)
  - `insights.html` + `insights-*.html` — Insights (content engine; launch articles on settlement claiming, guest voting, model-drift governance)
  - `drae.html` — redirect stub to https://drae.milatech.tech (kept so old links don't 404)
  - `styles.css` — shared stylesheet
- `mila/` → **https://mila.milatech.tech** — MILA product site
  - `index.html` — Home (post-makeover hero, what's new, waitlist, public Fix Tracker)
  - `features.html` — Features (makeover features, seven formats, how it works)
  - `pricing.html` — Pricing (Free / Premium / coin packs)
  - `faq.html` — FAQ
  - `demo.html` — interactive flash-poll demo
  - `feedback.html` — feedback form
  - `terms.html` — Terms of Service
  - `privacy.html` — Privacy Policy
  - `styles.css` — shared stylesheet
- `drae/` → **https://drae.milatech.tech** — DRAE sale site
  - `index.html` — Home (what DRAE is, walkthrough video, benchmark, sale summary)
  - `details.html` — Details (video walkthrough, architecture, benchmark, what's included)
  - `contact.html` — Contact (acquire directly, marketplace listings, book a live demo)
  - `drae-sale-card.png`, `drae-walkthrough.mp4` — sale assets
  - `styles.css` — copy of the flagship stylesheet (shared design system)


## Deployment


The `root/` and `mila/` Workers are connected to this repo with their site folder as the build root directory; pushes to `main` auto-deploy. The DRAE site is deployed separately (see below).


| Worker | Repo root directory | Custom domain |
|---|---|---|
| `mila-landing` | `mila/` | mila.milatech.tech |
| `milatech-root` | `root/` | milatech.tech |
| `drae-landing` | `drae/` (deployed with wrangler from a clean dir) | drae.milatech.tech |

No build step — pure static files.


## Making changes


Edit the HTML/CSS, commit, push. That's it for `root/` and `mila/`. For `drae/`, also re-deploy the `drae-landing` Worker (wrangler deploy of the `drae/` folder as static assets).

**Design language (all three sites):** the MILA makeover identity — deep ink `#0A0614` background, brand purple `#7A25F4`, bright accent `#B79CFF`, and the official MILA logo (gradient-bars M on a black tile, `logo.png` in each site folder). No old blue accent.


## Notes


- Pricing on the MILA site must match the app's RevenueCat configuration (currently Premium $2.99/mo, $19.99/yr; coin packs 50/$0.99, 160/$1.99, 450/$3.99, 1200/$7.99).
- "Coming soon" features (age-aware filtering, Live Activities) are marked as such until shipped in the app — do not present them as live.
- The Daily Updates section in `root/index.html` and the Fix Tracker section in `mila/index.html` are updated in place by scheduled jobs — keep their markup and anchors intact.
- DRAE is a pre-revenue code asset offered at $2,500 with full IP assignment — never claim ARR, revenue, or customers for it.


<!-- Cloudflare Git deployment connected 2026-09-28 -->
