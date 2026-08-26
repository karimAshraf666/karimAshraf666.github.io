# Evidence Inventory | V8 | 2026-08-26

Scope: source review, evidence verification, accessibility QA, and publication through the repository's existing GitHub Pages workflow. Files reviewed include the HTML pages, `assets/`, `docs/`, and the résumé PDF.
Sources cross-referenced: `index.html`, the four project pages, `docs/ASSET_INVENTORY.md`, `README.md`, on-disk assets, and direct view of the Bluworks and Money Fellows image files.
Resume text was extracted on 2026-08-20 (pymupdf and pdfminer installed locally), and the public LinkedIn experience section was read in an authenticated browser session. Portfolio figures are now checked against both. Karim confirmed in session that the CV is the source of record for numbers, and that every project published on his UXcel profile is cleared to appear on the portfolio in the same way Bluworks already does.

Public-safety key: **LOW** = sourced from public material or fully abstract. **MED** = provenance plausible but not fully documented on-page. **HIGH** = real internal product material or internal metrics with no documented public clearance.

---

## Matrix

### Money Fellows, `money-fellows.html` (+ summary tile in `index.html`)

| Column | Detail |
|---|---|
| **Verified claims** | Role: Product Designer, Feb 2025 to present. Scope: Goals, Recommendations, Onboarding, Migration. Goals V2 vocabulary: Goal, Received, Scheduled, Short or Extra. Sources: page copy plus LinkedIn profile copy (per ASSET_INVENTORY, the source of record for public MF claims). Metrics shown: 61.1% goal-creation conversion, 69.8% join-flow entry, 12% organic Goals engagement, 14% Recommendations adoption, 6,000+ recommendation bundles, ~48% conversion at a high performing new-user entry point, ~99% onboarding screen to screen (in research copy), 70+ research interviews. The prohibited cumulative "200+ research" claim is not present and must never be added. |
| **Local assets available** | 12 PNGs in `assets/money-fellows/`: `01-cover-and-rules`, `02-money-words-and-coverage-bar`, `03-my-goals-before-after`, `04-goal-details-before-after`, `05-intro-and-completion`, `06-finished-goals`, `07-screens-home-and-onboarding`, `08-screens-my-goals-states`, `09-screens-archive-arabic-circles`, `10-screens-goal-details-states`, `11-screens-details-edge-states`, `12-screens-create-and-plan`. |
| **Assets currently used** | **Zero product images, by Karim's instruction on 2026-08-20: business case study and technical work only, screens and flows to be added later.** Verified again in V8: `money-fellows.html` contains no `<img>` element at all. The page explains the model through an original CSS/HTML cover and a four-step decision flow, both labelled on-page as abstractions rather than product screens. All 12 PNGs in `assets/money-fellows/` remain on disk, unused, gitignored, and confirmed 404 on the live site. |
| **Gaps** | No file is missing; every product screen is deliberately withheld. **V6 addition:** the page now carries the business model explicitly (a money circle, and how slot position turns the same total into either borrowing or saving) and a dedicated section on eligibility, limits, KYC, credit communication and lifecycle changes, which the CV and LinkedIn both list but the page previously only implied. Public product facts (6/10/12-month circles, up to 1,200,000 EGP, rewards on later slots, Central Bank of Egypt regulation, over 8 million users) are attributed on-page to Money Fellows' own published material. Remaining gap is visual: annotated screens and flows, pending clearance. |
| **Public-safety uncertainty** | **LOW**, by construction. The page shows no confidential interface. Each diagram is labelled on-page as an original abstraction, not a product screen. **V4:** every figure was cross-checked on 2026-08-20 against the CV and the live public LinkedIn experience section. All nine match exactly (12%, 61.1%, 69.8%, 14%, 6,000+, ~48%, ~99%, 70+ interviews, migration in under two weeks), and all are already public on LinkedIn, so no unpublished internal figure appears on the site. The prohibited cumulative "200+ research" claim is absent. |

### Bluworks, `bluworks.html`

| Column | Detail |
|---|---|
| **Verified claims** | Role: Product Designer, Dec 2023 to Jun 2024. HR and workforce-operations SaaS. Two tracks: configurable web application plus a fixed-device (tablet) experience. Module list (Branch Manager, approval workflows and cycle, loan management, public holidays, cost centers, payroll/tax/insurance, payroll closing, attendance policies, bulk upload, worker app revamp). No metrics claimed; Track B outcome is deliberately un-numbered. |
| **Local assets available** | `assets/bluworks/`: `cover.jpg`, `screen-01.png`, `screen-02.png`, `screen-03.png`. `assets/bluworks-uxcel/`: 24 PNGs (`screen-01` to `screen-24`) from the Bluworks HR SaaS showcase. `assets/bluworks-tablet/`: 23 PNGs (`frame-00` to `frame-22`) downloaded 2026-08-20 from the Tablet Solution for Employee Clock-In showcase. |
| **Assets currently used** | **Changed in V8.** The 24-screen `#ui-library` section described in V7 no longer exists; that anchor is absent from every page. Bluworks is now curated to 10 images: `assets/bluworks/cover.jpg` plus `screen-01` to `screen-03` for the configurable web product, and six `assets/bluworks-tablet/` frames (`frame-12` to `frame-16`, `frame-18`) for the shared clock-in device. The full public libraries are reachable through the two showcase links on the page. This follows the V8 brief: curate by decision, do not restore the 42-image gallery. The 24 files in `assets/bluworks-uxcel/` are now unused but remain in the repo, cleared and available if a future pass needs them. |
| **Gaps** | None outstanding. Track B is now illustrated from its own public showcase (14 of the 23 downloaded frames are used: the full Arabic clock-in flow, its success, failure and manager-code fallback states, manager mode, biometric enrolment, plus three specification artefacts). The nine unused frames are the project cover and further specification pages, held back to keep the section about the product rather than the paperwork. |
| **Public-safety uncertainty** | **LOW.** All interface material is from two public UXcel showcases, each cited on the page: `app.uxcel.com/showcase/bluworks-hr-saas-784` (Track A) and `app.uxcel.com/showcase/tablet-solution-for-employee-clock-in-897` (Track B). V4 note: the Track B research figures on the page (15 surveys, 15 interviews, 60%, 40%, 40%) are quoted from the published showcase brief and are labelled on-page as a small sample. Numbers visible inside the tablet manager-dashboard mockups (647 hours, +13.02%, headcounts) are demo data and are deliberately never presented as outcomes. |

### Sharwa, `sharwa.html`

| Column | Detail |
|---|---|
| **Verified claims** | Role: Product Designer, Aug 2022 to Sep 2023 (matches CV and LinkedIn). Social commerce and group buying, MENA; Arabic mobile app plus responsive web. Metrics: app-open to order placement 7% to 14%; group-joining conversion 40% to 75% within two months; Google Play rating 3.2 to 4.4 (rating is externally verifiable). **V4 correction:** the page previously showed 45% to 75%. The CV states 40% to 75%, so the page was corrected to 40%. Attribution caveat is stated on-page. |
| **Local assets available** | `assets/sharwa/`: `cover.png`, `screen-01.png`, `screen-02.png`, `screen-03.png`. |
| **Assets currently used** | All 4: `cover.png`, `screen-01` (home and discovery), `screen-02` (guided group order), `screen-03` (account and product page). V8 presents the three reported figures (7% to 14%, 40% to 75%, 3.2 to 4.4) in a dedicated outcome band with the attribution caveat directly beneath them. |
| **Gaps** | None missing for the current layout. |
| **Public-safety uncertainty** | **LOW.** Resolved in V4. The showcase URL was located on Karim's UXcel profile and is now cited on the page: `app.uxcel.com/showcase/sharwa-social-e-commerce-399`. Sharwa now has the same evidence standard as Bluworks: named public source, externally verifiable rating, and conversion figures shown as reported context rather than as design acting alone. |

### 1MORETHING Ventures (1MT), `one-more-thing.html`

| Column | Detail |
|---|---|
| **Verified claims** | Role: Product Designer, part-time and remote, Mar 2024 to Feb 2025 (CV and LinkedIn agree). CV scope: turning ambiguous venture concepts into MVP scopes, user flows, prototypes and decision-ready direction across AI HR automation, stock counting, e-commerce assistance and B2B ordering; names Layla HR, Inveasy, Daaj and the JumlatyPro B2B revamp. Three public UXcel showcases back this: Inveasy and Dajaan state "As a Product Designer at 1MORETHING VENTURES" in their own text; JumlatyPro states "at NOMU Group". Karim confirmed in session (2026-08-20) that Jumlaty, Dajaan and Inveasy are all 1MORETHING work. The JumlatyPro showcase also states the design phase ran in one intensive week. No outcome numbers are claimed anywhere on the page. |
| **Local assets available** | `assets/1mt/`, 22 PNGs downloaded 2026-08-20 from the three showcases: `inveasy/` (5), `dajaan/` (6), `jumlaty/` (11). |
| **Assets currently used** | **Changed in V8.** Curated from 14 frames down to 8: `dajaan/cover.png` (hero), `inveasy/scanner.png`, `inveasy/manual.png`, `inveasy/results.png`, `dajaan/d.png`, `dajaan/e.png`, `jumlaty/c.png`, `jumlaty/f.png`. Each carries a caption naming the decision it demonstrates. The `index.html` card now uses the real `1mt/inveasy/cover.png` rather than the CSS art described in V7. The remaining frames stay on disk, cleared and unused. |
| **Gaps** | Layla HR (named in the CV) has no public material, so it is named in the page copy and not illustrated. No research artefacts or process documents are public for these three, so the page shows outcomes of design thinking rather than the working method behind it. |
| **Public-safety uncertainty** | **LOW.** All 14 published frames come from Karim's own public UXcel showcases, each linked in its section on the page. **Attribution correction (V5):** V4 wrongly listed Prime Talent Management Hub as 1MORETHING work. It is not. The Prime showcase states it was made for the Talent Management department at **AIESEC in Egypt**, which matches Karim's AIESEC roles on LinkedIn. Prime is not used on the 1MORETHING page. **Known wording difference:** the JumlatyPro showcase credits NOMU Group while the CV places JumlatyPro under 1MORETHING. The page states both, naming NOMU Group as the company behind JumlatyPro, so a reader who follows the link is not surprised. The vague "Results and Impact" copy in all three showcases (positive feedback, significantly reduced, increased engagement) was deliberately NOT carried onto the portfolio, as none of it is evidenced by numbers. |

---

## Cross-cutting notes

- `assets/` also holds four UXcel skill-graph variants; `uxcel-skill-graph.png` is used in the `index.html` About block, now placed beside the copy on desktop. LOW risk (public UXcel snapshot). The recovered UXcel portrait stays excluded, per ASSET_INVENTORY.
- The new home "AI in the practice" section describes how Karim uses AI (research synthesis, planning, prototyping, product operations) and presents Playful only as an independent, exploratory experiment. It claims no outcomes and lists no tools, so it carries no evidence risk.
- README rule honored: the cumulative "200+ research" claim is never used. The 70+ interviews figure is retained as the documented number.
- Style rule honored: no em dash appears in any page copy or in this document. The Money Fellows page uses no raster images at all, so no baked-in punctuation is exposed there. Bluworks and Sharwa use product/showcase screens whose internal text is out of scope for editing.
- Resume claims (dates, titles, metrics) remain UNVERIFIED-AGAINST-RESUME because PDF text extraction was blocked. Re-run once approved to confirm the page numbers match the resume exactly.

---

## Home page, rebuilt V7 (2026-08-20)

`index.html` was rewritten to state what Karim actually does rather than a generic designer positioning.

| Item | Detail |
|---|---|
| **Verified claims** | Hero and About assert: product designer, engineering background, currently at Money Fellows, Cairo. All supported by the CV, LinkedIn and the public UXcel profile summary ("Product designer with an engineering background, focused on turning complex, risk-sensitive product rules into clear customer experiences"). The new Résumé section reproduces the CV: four design roles with their exact dates and locations, plus the Mansoura University B.Sc. in Communication and Information Engineering, Sep 2016 to Aug 2021, A+ final project. |
| **Numbers used** | Only four percentages appear on the home page: Sharwa 7% to 14% and 40% to 75%, both taken verbatim from the CV. The 70+ interviews figure appears once. No Money Fellows percentages are repeated on the home page; they live on the case study. |
| **What was removed** | The previous hero ("Designing the decisions that move people forward") and About opener ("drawn to the point where ambition meets uncertainty"), both of which described no actual capability. Empty "Open project page" captions were replaced with a one-line description of what each case study contains. |
| **Defect fixed** | Section numbering ran 01, 03, 04, 05, 06 and skipped 02. It is now sequential 01 to 06, verified in the DOM. |
| **Résumé requirement** | Karim asked for a clean readable résumé section using the current PDF. The section now carries the full career record as readable HTML for recruiters who will not open a PDF, with a download card linking the PDF (confirmed serving 200). Earlier roles (Workiji, Babel, AIESEC) stay in the PDF only, and the card says so. |
| **Public-safety uncertainty** | **LOW.** Nothing on the home page exceeds the CV, LinkedIn or the UXcel profile. |

## Residual gaps, V5

1. **Money Fellows visuals are deferred, not blocked.** Karim confirmed on 2026-08-20: business case study and technical work now, screens and flows later. The 12 on-disk screens stay unused until he clears them asset by asset. The page is written so that adding annotated flows later slots in without rewriting the argument.
2. **Prime Talent Management Hub is cleared but unused.** It is AIESEC work from an earlier period than the four Selected Work roles. It could support an earlier-career or side-work section, but it does not belong in any current case study, and adding a fifth tile would work against keeping the home page focused.
3. **The Bluworks web-app library reuses four narrative screens.** `assets/bluworks/screen-01` to `screen-03` appear in the Track A story and again inside the library. Not an accuracy problem, but a reader scrolling the page meets them twice.

## Verification log (2026-08-20)

- Resume text extracted with pdfminer; `pymupdf` and `html5lib` installed locally.
- LinkedIn experience section read in an authenticated browser session. Money Fellows figures match the CV exactly; dates match for all four roles.
- Sharwa group-joining figure corrected from 45% to 40% to match the CV. Sharwa showcase URL located and cited.
- All 24 Bluworks web frames, all 23 tablet frames, and all 22 1MORETHING frames opened and inspected individually before captioning.
- Prime attribution checked directly against its showcase text and corrected from 1MORETHING to AIESEC.
- All five pages parse with zero html5lib errors.
- Desktop 1280px and mobile 375px checked on every page: zero horizontal overflow.
- Zero em dashes across all HTML and CSS.
- Home page rebuild verified: all four internal case-study links and the résumé PDF return 200, every in-page anchor resolves to a real id, section numbers sequential, and no horizontal overflow at 1280px or 375px.
- Money Fellows business facts checked against moneyfellows.com; Karim's own scope wording checked against his public UXcel profile summary.
- New slot-position diagram given the same min-width scroll treatment as the existing diagrams, after it was caught rendering at an illegible 3.4px effective font on a 375px viewport.

---

## V8 recruiter and positioning pass | 2026-08-26

The live site, local repository, résumé PDF, authenticated LinkedIn profile, public UXcel project grid, and the prior Claude portfolio task were reviewed together.

- The homepage now identifies Karim directly as a Product Designer who turns complex product rules into clear customer decisions.
- Product Design is explicitly the primary career lane. Product Owner and Product Manager fit is presented as adjacent value based on problem framing, business-rule mapping, prioritization, specification, alignment, metrics, and delivery.
- Public project covers from the local UXcel-derived asset set are used for Bluworks, Sharwa, and 1MORETHING. Money Fellows keeps an original abstract cover and publishes no product interface.
- Money Fellows copy was condensed around the decision journey from customer intent to a trusted next step. All existing verified figures remain unchanged.
- Bluworks was curated from 42 published images to a smaller decision-led selection. The full public UXcel showcases remain linked for exhaustive evidence.
- Sharwa was rewritten around three customer frictions and three product decisions. Its three reported measures and attribution caveat remain unchanged.
- 1MORETHING was rewritten as three venture directions with AI uncertainty, fallback, and human review as the shared principle. It still makes no adoption, revenue, or production claim.
- A detailed copy, journey, and acceptance standard is recorded in `docs/PORTFOLIO-REVIEW-V8.md`.

---

## V8 independent QA pass, 2026-08-26

Reviewed the published V8 (commit `79c6b47`) as a senior product-design hiring manager and as a product leader hiring for an adjacent PO/PM role. Scope: clarity, hierarchy, responsiveness, accessibility, links, evidence fidelity, visual polish.

### Evidence and positioning: no defects found

- Word counts are now 719 to 871 per page, down from 2,125 (Money Fellows) and 2,535 (Bluworks). The scanning problem the V8 brief identified is resolved.
- Every numeric claim on the site still matches the résumé and public LinkedIn. Site-wide figures are 12%, 14%, 40%, 61.1%, 69.8%, 7%, 75%, 99%, 6,000+, 70+. No figure exceeds the documented source.
- The prohibited cumulative "200+ research" claim is absent.
- No page references `assets/money-fellows`. Confirmed 404 on the live site.
- NOMU Group attribution is present on JumlatyPro alongside the 1MORETHING period statement.
- Prime Talent Management Hub does not appear anywhere in the HTML, correctly, since it is AIESEC work.
- 1MORETHING contains no production, adoption, scale, or revenue language.
- Zero em dashes in HTML and CSS.

### Defects found and fixed

| # | Defect | Evidence | Fix |
|---|---|---|---|
| 1 | Numbered steps invisible on dark sections. `.story-list b` used `var(--case)`, a dark brand colour, and the `.dark` block overrode the paragraph colour but never the number. | Measured contrast 1.18 on 1MORETHING, 1.83 on Bluworks, 2.06 on Money Fellows, against a 4.5 requirement. | Added `.dark .story-list b { color: var(--case-soft); }`. Now 13.02, 13.98 and 14.09. |
| 2 | The evidence caveat failed contrast on the lightest outcome band. This is the attribution text, so legibility is an integrity issue, not only an accessibility one. | `.evidence-note` at `rgba(255,255,255,0.68)` measured 3.34 on Sharwa's `#196eb8`. | Raised to `0.92`. Sharwa now 4.75, Money Fellows 7.12, 1MORETHING 12.19. |
| 3 | Mobile menu button was an 18px tap target, below the 24px WCAG 2.5.8 minimum, on the primary navigation control. | Measured 18px high, 41px wide at 375px. No padding or min-height in the rule. | Padding plus negative margin and `min-height: 44px`, so the hit area grows without moving the label. Now 44px. |
| 4 | Body copy failed AA by a hair on the ventures tint. | `--muted` `#5e6863` on `#eadff3` measured 4.496 against 4.5, affecting six elements in the Daaj section. | Darkened `--muted` to `#555f59`. All five pages now pass with a minimum of 4.61. |
| 5 | Every external link and the résumé download replaced the portfolio tab, so a recruiter following a showcase link lost the site. | 10 links: six UXcel showcases, two LinkedIn, the résumé PDF. | Added `target="_blank"` with `rel="noopener noreferrer"`. The `mailto:` link is deliberately left alone. |
| 6 | No favicon on any page, so a shared link showed a blank browser-tab icon. | Zero `rel="icon"` declarations across all five pages. | Inline SVG data-URI favicon in the site palette. No new asset and no extra request. |

### Verification after the fixes

- Contrast: all five pages, zero failures at 375px and 1280px, minimum ratio 4.61.
- Layout: zero horizontal overflow on all five pages at 1280px, 768px and 375px.
- Mobile menu: opens and closes, toggles `aria-expanded`, reveals all five links.
- No console errors. All images load. All internal anchors and cross-page links resolve.
- Markup parses cleanly; one `h1` per page; no heading level skips; every `img` has an `alt`.

### Known limitations, deliberately not changed

- With JavaScript disabled at mobile width the header nav cannot be opened, since it is behind the toggle. All content still renders and remains navigable through the in-content links and the brand link home, so the readability criterion holds.
- Uppercase mono labels sit at 11px. This is an intentional editorial convention, is applied consistently, and passes contrast.
- `assets/bluworks-uxcel/` (24 files) and most `assets/bluworks-tablet/` and `assets/1mt/` frames are unused after V8 curation. They are cleared public material and are kept for future passes rather than deleted.
