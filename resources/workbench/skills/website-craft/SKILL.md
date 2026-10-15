---
name: website-craft
description: >
  End-to-end workflow for designing and building a client or personal website or landing
  page that doesn't look AI-made: interview, references, design system, asset system,
  anti-slop copy, build, screenshot verification, feedback round. Use for "build a website",
  "landing page", "redesign this site", "make this look premium", "this looks like a template",
  "website for <client>", or any new marketing page. Hands off to scroll-craft for scroll-driven
  experiences and to design-loop / design-dna for matching and codifying a look.
---

# Website Craft

Lessons combined from: Nate Herk's ScrollCraft video (youtu.be/QUI6Ug4cHnE), Jack Roberts'
Design DNA video, level 2 (youtu.be/cM5n9priMjo), and Cassie Groos' Hatch 2026 talk
(youtu.be/JeJhPtsbIGA).

Tools and where to find references, generation APIs and voice: see `PLATFORMS.md` in this folder.

## 0. Find what already exists

Before asking anything, look: the client's current site, brand kit, a `DESIGN.md` /
`design/` folder, a client DNA skill, past builds, real photos. "We're not starting from
zero" makes the first draft much better. Reuse everything real.

## 1. Interview (one pass, short)

Ask only what you can't find. Record answers **verbatim** in `BRIEF.md`:

1. **Vibe in 3-5 words + up to 3 references from any medium** (film, magazine, shop, album),
   not just websites. Naming sites is how you end up copying one.
2. **The journey, section by section, in their words.** What the visitor hits first, next, last.
3. **What must the visitor believe by the end?** One sentence, not a feature list.
4. **Energy and feeling curve.** Where calm, where intense; how they should feel at each stage;
   **the one moment they should remember** (the peak).
5. **One thing this site does that no site they've seen does.** This seeds the signature move.
   Push past "be memorable".
6. **Real assets.** Photos, footage, screenshots, testimonials, data. Decides generate vs grade.
7. **Conversion.** The one action, and where every button goes (real URLs only).

If the user explicitly says "use your judgment", write the brief yourself, mark it
`Self-authored under creative delegation`, and proceed without more questions.

## 2. References, then direction

Gather 3-6 references (Refero MCP if connected, Savee, Mobbin, client competitors, the user's
picks). Pick **one dominant direction**. Don't average references into a safe middle. Write
a short decision ledger: what is taken from which reference, and why.

## 3. The design system page (ship it with the site)

Build a `/system` page (or `design-system.html`) in the same repo, before the pages:

- **Tokens:** colour roles + coverage %, type families with fallbacks and the display:body
  ratio, spacing scale (4px or 8px base), radii, elevation, motion durations/easing.
- **Components in use:** buttons (all states), nav, cards *only if interactive*, forms, footer.
- **Graphic system** (if illustrated/generated imagery): cast/character sheet, proportions
  ("model sheet"), lighting, palette for image prompts in descriptive colour names, and an
  **asset inventory** so new images stay on-model.
- **Font recommendations:** 2-3 pairings that fit the brief, so the client has real options.
- **Copy rules** for this brand (see section 5).

This page is both client deliverable and agent context. Later pages are built from it, not
from memory.

## 4. Build

- Semantic HTML, mobile composed separately (not just stacked desktop).
- Max two type families. Body measure 45-75ch. One accent colour.
- One **signature move**, unique to this site. One engineered **peak**.
- If the brief wants scroll-as-timeline, pinned scenes, scrubbed video, or depth heroes,
  use the **scroll-craft** skill.
- If matching a reference, run **design-loop**.
- Live data where it is real (member counts, prices), with sources.
- Every claim gets a receipt (testimonial, number, source), never invented.

## 5. Copy (anti-slop pass, mandatory)

Run **humanizer** on all copy, then apply these website-specific rules:

- **Name the pain** in the visitor's words before naming the product.
- **Don't make me think.** One idea per section, plain verbs, scannable headings.
- Concrete beats clever: numbers, names, places, outcomes. Specific over impressive.
- Banned CTAs unless nothing else fits: "Get started", "Learn more", "Start free",
  "Unlock", "Elevate", "Supercharge", "Seamless". Write what actually happens next.
- Banned patterns: "It's not X, it's Y" contrasts, triads by reflex, rhetorical-question
  openers, one-line "mic drop" closers, em-dash chains, "In today's fast-paced world".
- Less text. The most common failure on reviewed client sites is too much text; the second is that it sounds AI-written.
- Keep the client's real voice; never fabricate quotes, stats, or credentials.

## 6. Visual anti-slop bans (unless the brand explicitly requires it)

- Indigo/violet gradients; purple-on-dark "AI" palettes; gradient text.
- Cards around everything; three equal feature cards with icons as the default section.
- Dark mode by default with no brief reason.
- Autopilot "calm editorial": cream background + giant serif + one italic word + terracotta.
- Centred everything; identical section rhythm top to bottom.
- Emoji as icons; generic 3D blobs; soft matte clay dioramas as a default world.
- `01 / 06` counters, "scroll to explore" nudges, fake logo walls, stock "diverse team" photos.
- Glassmorphism by reflex; shadows on everything.

## 7. Verify (never ship unseen)

Render it. Screenshot desktop (1440) and mobile (390) at every section and several scroll
positions. Check: dead scroll (nothing changes), low-contrast text, overflow, broken links,
console errors, reduced-motion state, load weight. Run the **design-loop** critics if the
work is client-facing. Fix, re-shoot, then present.

## 8. Present and take feedback

Show a short screenshot walkthrough plus the local URL. Ask for feedback **section by
section** (hero / each section / footer). Apply all of it in one round, then log what
changed in `CHANGELOG.md`. After approval, offer **design-dna** to lock the style into a
client skill.

## Deliverables checklist

`BRIEF.md` · decision ledger · `/system` page · site · screenshot strip · `CHANGELOG.md` ·
(optional) client DNA skill.
