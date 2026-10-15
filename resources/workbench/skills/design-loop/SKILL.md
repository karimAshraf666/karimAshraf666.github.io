---
name: design-loop
description: >
  Build a visual piece (website, landing page, poster, social graphic, deck slide, email,
  motion graphic) to match a reference or brief by looping a builder against fresh-eyes
  critic agents until every critic passes. Use when the user says "design loop", "match
  this design", "make it look like this", "recreate this style", "it doesn't look right",
  "keep improving until it's perfect", or attaches a reference image/URL/video and wants
  something built from it. Pair with design-dna afterwards to make the winning look repeatable.
---

# Design Loop

Asking a model to "improve this design" ten times gives ten different designs. The loop
fixes that by giving improvement a fixed target and independent judges.

Source: Jack Roberts, "Claude Design Just Solved its #1 Problem" (youtu.be/cM5n9priMjo).
His exact skill file is in his Skool community; this is a rebuild of the method he describes,
plus the fresh-context critic rule from the "gauntlet loop" pattern.

## Inputs (ask only for what is missing)

1. **The gold standard.** A reference image, URL, video clip, or an existing piece. If there
   is no reference, run `refero-design` research or ask for 2-3 references before building.
   A brief alone is not a build target.
2. **The brief.** Who it is for, what it must say, the one action it must drive.
3. **The format and size.** Canvas size, breakpoints, duration for motion.
4. **Assets.** Real photos, logos, brand kit, copy. Real beats generated.
5. **Existing design system / DNA skill** for this client, if one exists. If a client
   DNA skill or `DESIGN.md` exists, it overrides the reference on any conflict.

## The loop

**Round 0: Observe the reference.** Write a short inventory: layout grid, type scale ratio,
colour coverage percentages, spacing rhythm, imagery treatment, the one "weird move" (the
single deliberate break in the system), and what is absent (no shadows, no icons, etc.).
Measure. Don't describe.

**Round 1: Build.** Build the piece. Render it and capture screenshots at real size
(desktop + mobile for web, every key frame for motion). Use the browser preview / Playwright /
the Claude Browser pane. **Never judge a design from its code.**

**Critique.** Spawn the critics **in parallel, each with fresh context** (a new subagent
that receives only: the reference, the brief, the screenshots, and its own rubric). Fresh
context is required: a critic that saw the builder's reasoning rubber-stamps it.

| Critic | Job | Fails the piece when... |
|---|---|---|
| **Fidelity** | Side-by-side with the reference | ratios, spacing, alignment, colour coverage, or type hierarchy visibly differ; the weird move is missing |
| **Brief** | On-message and on-audience | the one action is unclear in 5 seconds; copy is generic; content is invented |
| **Craft** | Typography, spacing, contrast, responsiveness, accessibility | overflow, orphans, line length > 75ch, contrast < 4.5:1 body, inconsistent spacing, broken mobile |
| **Slop** (optional, recommended for client work) | Looks/reads AI-made? | any item from the anti-slop list in `website-craft` or AI-tell copy |

Each critic returns: `PASS` or `FAIL`, then max 5 concrete fixes, each pointing at a
specific element with a measurable target ("hero H1 to body ratio is 4:1, reference is 7:1,
raise H1 to 88px"). Vague notes ("make it pop") are rejected and re-requested.

**Fix and re-render.** Apply fixes. Do not apply a fix that breaks another critic's PASS.
When critics conflict, the order of authority is: client design system > reference
fidelity > brief > craft polish.

**Repeat** until all critics PASS, or 4 rounds. If round 4 still fails, stop and show the
user the remaining disagreements with screenshots. Do not keep looping silently.

## Without subagents (Codex, ChatGPT, single-agent tools)

Run each critic as a separate pass in sequence. Before each pass, restate: "I am the
<name> critic. I have not seen the build reasoning. I judge only the screenshots against
the reference and rubric." Write each verdict down before reading the next.

## Output

- The final piece plus the screenshot strip (reference beside final).
- `DESIGN-LOOP-LOG.md`: rounds run, each critic's verdicts, what changed, anything left open.
- Then offer: "Want me to run design-dna on this so the style is reusable?"

## Rules

- Never copy a real logo, wordmark, licensed photo, or proprietary typeface from a
  reference. Reproduce the system, not the marks.
- Every font gets a fallback.
- Generated imagery must match the palette and lighting of the reference; regenerate
  rather than CSS-fake complex imagery.
- Show the user the result after the loop, not after every round, unless they ask.
