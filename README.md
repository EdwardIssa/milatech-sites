# milatech-sites

Source for Mila Tech LLC's websites, deployed via Cloudflare Workers (Static Assets) with GitHub-connected continuous deployment.

## Structure

- `mila/` → **https://mila.milatech.tech** — MILA product site
  - `index.html` — landing page (hero, features, how it works, pricing, FAQ)
  - `terms.html` — Terms of Service
  - `privacy.html` — Privacy Policy
  - `styles.css` — shared stylesheet
- `root/` → **https://milatech.tech** — Mila Tech LLC company site
  - `index.html`, `styles.css`

## Deployment

Each Cloudflare Worker is connected to this repo with its site folder as the build root directory:

| Worker | Repo root directory | Custom domain |
|---|---|---|
| `mila-landing` | `mila/` | mila.milatech.tech |
| `milatech-root` | `root/` | milatech.tech |

Pushes to `main` auto-deploy. No build step — pure static files.

## Making changes

Edit the HTML/CSS, commit, push. That's it. Keep the design language consistent across both sites (dark theme, blue accent `#3b82f6`).

## Notes

- Pricing on the MILA site must match the app's RevenueCat configuration (currently Premium $2.99/mo, $19.99/yr; coin packs 50/$0.99, 160/$1.99, 450/$3.99, 1200/$7.99).
- "Coming soon" features (age-aware filtering, Live Activities) are marked as such until shipped in the app — do not present them as live.
