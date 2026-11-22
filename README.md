# milatech-sites


Source for Mila Tech LLC's websites, deployed via Cloudflare Workers (Static Assets) with GitHub-connected continuous deployment.


## Structure


The deployed marketing sites are multi-page, each with a shared top navigation bar and footer. `root/leadminerx/` is an older one-pager and is not the LeadMiner X store.

- `root/` → **https://milatech.tech** — Mila Tech LLC company site
  - `index.html` — Home (hero, venture/product cards, Daily Updates)
  - `products.html` — Products (lineup, capabilities, R&D pipeline)
  - `about.html` — About (company, leadership)
  - `support.html` — Support (per-product help, FAQ, community donations, contact)
  - `services.html` — Services (mortgage workflow automation, ML & predictive diagnostics, product engineering; lead form)
  - `contact.html` — Contact (lead form with mailto fallback)
  - `brands.html` — MILA for Brands (sponsored polls, sample sentiment report from a real poll, Sentiment API section — waitlist removed 2026-10-28 at Edward's order; API interest routes to the Contact page )
  - `insights.html` + `insights-*.html` — Insights (content engine; launch articles on settlement claiming, guest voting, model-drift governance)
  - `drae.html` — full DRAE product page (runtime governance for ML ensembles and AI agents; replaced the old redirect stub on 2026-11-04 — a 15-word meta-refresh page on the AdSense-reviewed root domain was a low-value-content liability)
  - `loyal.html` — full LOYAL product page (public profile search; live embedded checker)
  - `sitemap.xml` — sitemap for the root domain (added 2026-11-04)
  - `styles.css` — shared stylesheet
- `mila/` → **https://mila.milatech.tech** — MILA product site
  - `index.html` — Home (post-makeover hero, what's new, public Fix Tracker — signup waitlist section removed 2026-10-28 at Edward's order)
  - `features.html` — Features (makeover features, seven formats, how it works)
  - `pricing.html` — Pricing (Free / Premium / coin packs)
  - `faq.html` — FAQ
  - `demo.html` — interactive flash-poll demo
  - `feedback.html` — feedback form
  - `terms.html` — Terms of Service
  - `privacy.html` — Privacy Policy
  - `styles.css` — shared stylesheet
- `leadminerx/` → **https://leadminerx.milatech.tech** — LeadMiner X marketing site (the $149 store). This folder is the source for the `leadminerx-landing` worker.
  - `index.html` — Home
  - `product.html` — Product
  - `pricing.html` — Pricing
  - `faq.html` — FAQ
  - `affiliates.html` — Affiliates
  - `terms.html` — Terms of Service
  - `privacy.html` — Privacy Policy
  - `styles.css` / `mine.css` — stylesheets
  - Checkout stays on Gumroad (`milatech.gumroad.com/l/leadminerx`, `/l/sgciy`, `/l/rzwhk`). Do not swap those for Stripe unless Edward asks.
- `root/leadminerx/` is an **older one-pager** (`index.html`, `privacy.html`, `terms.html`, `styles.css`). It is not the source for https://leadminerx.milatech.tech. `milatech-root` still publishes it at https://milatech.tech/leadminerx/ because that worker's build root is `root/`. Recommend redirecting `/leadminerx` and `/leadminerx/` on milatech.tech to https://leadminerx.milatech.tech so the company site stops serving the stale one-pager. That redirect belongs in `root/` (`milatech-root`). This change does not edit `root/`, because another open PR is already changing it.
- `drae/` — **RETIRED. DO NOT DEPLOY.** This folder is the old DRAE sale tree (its `index.html` still carries the withdrawn "$2,500" sale copy). It is kept for reference only and must never be deployed. The live drae.milatech.tech site (the in-development notice) is served from `~/workspace/drae-deploy/` — that is the only drae source (see Deployment below).


## Deployment


The `root/` and `mila/` Workers are connected to this repo with their site folder as the build root directory; pushes to `main` auto-deploy. `leadminerx/` is the source for https://leadminerx.milatech.tech. The `leadminerx-landing` worker is still a wrangler upload of static assets and is not Git-connected yet, so a push does not update that domain until the worker's build root is set to `leadminerx/` the same way `mila/` and `root/` are connected. The DRAE site is deployed separately (see below).


| Worker | Repo root directory | Custom domain |
|---|---|---|
| `mila-landing` | `mila/` | mila.milatech.tech |
| `milatech-root` | `root/` | milatech.tech |
| `leadminerx-landing` | `leadminerx/` | leadminerx.milatech.tech |
| `drae-landing` | `~/workspace/drae-deploy/` (NOT this repo — wrangler deploy, assets `./dist`) | drae.milatech.tech |

`leadminerx/wrangler.jsonc` matches the live worker: name `leadminerx-landing`, compatibility date `2025-01-01`, assets only (`directory: "."`, `html_handling: "auto-trailing-slash"`), empty `previews`, no script module, no bindings, and no secrets. `leadminerx/.assetsignore` keeps that config out of the public asset set, the same as `root/` and `mila/`. Do not wrangler-deploy over `leadminerx-landing` without comparing the checkout to what is already live.

`root/leadminerx/` is still the older one-pager at https://milatech.tech/leadminerx/. Recommend a redirect there from `/leadminerx` and `/leadminerx/` to https://leadminerx.milatech.tech. Make that change in `root/`, not in `leadminerx/`.

No build step — pure static files. `root/wrangler.jsonc`, `mila/wrangler.jsonc`, and `leadminerx/wrangler.jsonc` are the Worker configs. Each includes an empty `previews` block so non-main branch builds can run `npx wrangler preview`.


## Making changes


Edit the HTML/CSS, commit, push. That's it for `root/` and `mila/`. `leadminerx/` is edited the same way, but https://leadminerx.milatech.tech does not update on push until `leadminerx-landing` is Git-connected to this folder. **DRAE is not deployed from this repo:** the `drae-landing` Worker serves `~/workspace/drae-deploy/dist`, deployed with wrangler from `~/workspace/drae-deploy/`. The `drae/` folder in this repo is the retired sale tree — never deploy it; doing so would put the withdrawn $2,500 sale pages back live over the in-development notice.

**Design language (company site, MILA, and the retired DRAE tree):** the MILA makeover identity — deep ink `#0A0614` background, brand purple `#7A25F4`, bright accent `#B79CFF`, and the official MILA logo (gradient-bars M on a black tile, `logo.png` in each site folder). No old blue accent. LeadMiner X keeps its own Mine palette in `leadminerx/mine.css` (charcoal `#141619`, safety orange `#FF6A13`, ore gold `#E8B04A`).


## Notes


- Pricing on the MILA site must match the app's RevenueCat configuration (currently Premium $2.99/mo, $19.99/yr; coin packs 50/$0.99, 160/$1.99, 450/$3.99, 1200/$7.99).
- "Coming soon" features (age-aware filtering, Live Activities) are marked as such until shipped in the app — do not present them as live.
- The Daily Updates section in `root/index.html` and the Fix Tracker section in `mila/index.html` are updated in place by scheduled jobs — keep their markup and anchors intact.
- DRAE is a pre-revenue code asset; its public sale was withdrawn on 2026-11-09 and drae.milatech.tech serves an in-development notice — never claim ARR, revenue, or customers for it.


<!-- Cloudflare Git deployment connected 2026-09-28 -->
