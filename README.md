# Karim Ashraf Portfolio | V10

A responsive, evidence-led portfolio for senior Product Designer opportunities and selected Product Manager roles. The site is static HTML, CSS, and JavaScript with no framework, database, tracking, or build step.

## Live site

Published at **https://karimashraf666.github.io** from `main` at the repository root.

## Structure

- `index.html`: positioning, selected work, design versus product-management fit, experience including the Playful initiative, About, UXcel credentials, résumé download, and contact.
- `blog.html`: standalone writing index linked from About.
- `workbench.html`: searchable industry resource library, practical specification/review tools, team templates and AI workflows.
- `workbench.css` and `workbench.js`: scoped workbench layout and browser-local drafts/favorites.
- `resources/workbench/`: reusable Markdown/CSV templates, resource catalog and downloadable team kit. Third-party assets stay at their source.
- `resources/workbench/skills/`: AI design skills (SKILL.md) published for Claude Code, Codex and compatible agents, plus `design-ai-skills.zip`. Edit them there, then rebuild.
- `playful.html`: AI-assisted product-building case study for the live Playful platform and its operating system.
- `money-fellows.html`: Goals, recommendations, onboarding, eligibility and limits, research, migration, and verified product measures.
- `bluworks.html`: configurable HR web platform and the distinct fixed-tablet clock-in experience.
- `sharwa.html`: group-buying behavior, home discovery, guided group order, and reported product movement.
- `one-more-thing.html`: Inveasy, Daaj, and JumlatyPro venture directions.
- `styles.css`: shared visual system and responsive behavior.
- `redesign.css`: floating navigation, image-led layouts, typography, responsive styles and optional motion.
- `script.js`: mobile navigation, section state, scroll reveals, reading progress and footer year.
- `scripts/portfolio_shell.py`: shared navigation and library controls used when rebuilding the workbench.
- `scripts/workbench_navigation.py`: directory layout and category navigation derived from the existing resource cards.
- `design/`: discovery brief, component requirements, ruled-out approaches and shared tokens.
- `discovery.css`: token-based navigation and directory styling.
- `design-system.html`: generated visual reference for the discovery extension.
- `docs/EVIDENCE-INVENTORY.md`: source of truth for claims and public-safety decisions.
- `docs/PORTFOLIO-REVIEW-V8.md`: recruiter, copy, positioning, and journey standard.
- `docs/PORTFOLIO-REVIEW-V9.md`: October Playful refresh, copy changes and responsive verification.
- `docs/PORTFOLIO-REVIEW-V10.md`: October 12 visual refresh, simpler resource navigation and verification.

## Local preview

```text
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Rebuild the directory and preview assets

Resource data lives in `scripts/build_workbench.py`. Keep resource IDs stable to preserve Saved lists. Edit published skill sources in `resources/workbench/skills/`.

```text
python scripts/build_workbench.py
python scripts/optimize_portfolio.py
python scripts/build_design_reference.py
python scripts/verify_portfolio.py
node --check workbench.js
node --check script.js
```

The image optimization script requires Pillow. Original approved screens remain intact; homepage previews live in `assets/previews/`. Rebuilding ZIPs can change archive timestamps without changing their contents. Review staged files before publishing and keep unrelated resume drafts separate.

The directory uses native hash links, progressively enhanced search and browser-local Saved resources. Mobile browsing is a disclosure; desktop categories remain visible. `design/components/` defines the behaviors and `design/tokens/discovery.css` defines new visual values. Run the design reference generator after editing either source.

## Evidence rules

- The résumé is the source of record for numbers. Résumé, LinkedIn, and portfolio must agree.
- The résumé headline is `Product Designer | Product Strategy, Growth and AI-Assisted Delivery`, and the profile scope is regulated services, SaaS, social commerce, and AI-enabled ventures. Do not reintroduce fintech as the leading descriptor of Karim's overall position. Fintech stays only as the Money Fellows project label.
- Product design is the primary lane and product management is adjacent. Keep both lanes evidence-linked and do not merge them into one hybrid title.
- Never add the cumulative `200+ research` claim. The documented figure is 70+ Money Fellows interviews.
- Do not publish any file in `assets/money-fellows/`. Product screens remain withheld until Karim clears them asset by asset.
- UXcel-published work is cleared and should cite the specific public showcase.
- Attribute company facts and shared product outcomes accurately.
- Keep build-time tooling separate from product capability. The Playful video analyzer is part of the building method, not a customer-facing product or an outcome.
- Do not add a live Playful link. Its portfolio case study uses approved public screenshots and source-checked implementation details instead.
- Playful was refreshed on 6 October 2026 against production build `2cb1f28`. Do not reuse August screenshots or treat the older local `master` branch as the current deployed source.
- Prime Talent Management Hub is AIESEC work, not 1MORETHING work.
- The JumlatyPro showcase credits NOMU Group while the résumé places the work in the 1MORETHING period. Keep both statements visible.
- Do not use em dashes in HTML or CSS.

## Verification before publishing

- Parse all root HTML pages and resource worksheets.
- Confirm every local image and file reference resolves.
- Confirm internal navigation targets exist.
- Check desktop and mobile layouts for horizontal overflow.
- Test the mobile menu with keyboard and touch input.
- Confirm external UXcel, LinkedIn, email, and résumé links.
- Confirm `assets/money-fellows/` remains ignored and absent from Git history.
- Confirm no em dash appears in HTML or CSS.

To publish an approved update, commit and push `main`, then verify the actual GitHub Pages URL after the deployment completes.
