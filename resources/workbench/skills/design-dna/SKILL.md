---
name: design-dna
description: >
  Codify one design the user loves into a reusable style skill so it can be reproduced on
  new content, in any format, without drifting. Use after a design-loop winner, or when the
  user says "design dna", "codify this style", "make this repeatable", "turn this into a
  skill/template", "lock in this look", "brand style for this client", or "why does this
  look good". Produces dna.json, a 2KB PROMPT.md, tests that can fail, and a new skill folder.
---

# Design DNA

A design loop finds one beautiful thing. Design DNA turns it into a command, so the 8th
output sits next to the 1st as a set. It works on anything Claude built: site, poster,
carousel, deck, email, motion.

Method source: Jack Roberts, "Design DNA" (Notion page linked from youtu.be/cM5n9priMjo).
Field reference: `dna.schema.json` in this folder.

**Why it works:** every rule you don't write down, the model guesses, and it guesses the
average of everything it has seen. That average is AI slop. So write the rules down, but
only the ones that carry identity, and keep the prompt small.

## What carries identity (read first)

1. **Relationships, not values.** "H1 is 8x body, never under 6x", not "H1 is 96px".
2. **Colour proportions.** Same hexes at 60/30/10 vs 90/8/2 are different designs. Record coverage %.
3. **The weird move.** Most designs worth copying have exactly one deliberate break (type
   crossing an image, a clipped numeral, a rule overshooting the margin). Find it, name it.
4. **Refusals.** If the accent covers 3% of the canvas, the real rule is a refusal. Write bans.
5. **Absence is design.** No shadows, no icons, no curves, nothing centred: record it.
6. **Structure.** Name the layouts (archetypes), or styling stays consistent while structure drifts.

## Seven steps. Show work at each.

1. **Observe, don't interpret.** Flat inventory: sampled hexes + % of canvas each, type
   sizes/weights count, largest:smallest type ratio, margins as % of canvas, texture, edges,
   image treatment, what is absent.
2. **Debate.** Loop A (maximalist): list everything. Loop B (minimalist): identity lives in
   3-9 moves plus a wall of bans; attack A's list. For each property ask: *if I changed this,
   would it stop looking like the reference?* Yes = load-bearing. No = trivia. Resolution:
   the exhaustive record goes in `dna.json`; the load-bearing set goes in `PROMPT.md` (≤2KB).
3. **Codify** `dna.json` using the schema. Use percentages for space so one spec drives a
   1080x1350 carousel and a 1920x1080 slide. Descriptive colour names ("dusty plum", never
   "accent-500"): image/video models can't read token names.
4. **Tests that can fail (8-12).** Binary and measurable: "accent under 8% of canvas",
   "max 3 type sizes per frame", "display:body ratio above 6:1", "weird move present exactly
   once", "body under 65 chars/line". Not tests: "feels premium". Mark which a script can check.
5. **Reconstruct and diff.** Rebuild the original from `dna.json` alone, without looking at
   the reference. Put both side by side, list every difference, and fold each one back into
   the spec. Repeat 2-3 passes. A spec that has never rebuilt its source has never been tested.
6. **Emit the skill** (folder named after `meta.slug`). Put it in the **client's repo**
   (`.claude/skills/<slug>/`) for client work, or `~/.claude/skills/<slug>/` for personal styles:
   ```
   <slug>/
     SKILL.md        when/how to use this style; asks for the inputs it needs (subject, copy, format)
     PROMPT.md       the ≤2KB payload, this is what goes in context
     dna.json        full record, never pasted into a prompt
     reference/      the original, kept forever
     example/        one worked output
     tools/check.py  automatable tests, exits non-zero on failure (optional but preferred)
   ```
   **PROMPT.md order** (attention is strongest at the ends): 1 reference image named first,
   2 one-line soul, 3 the weird move alone, 4 the 3-9 signatures as ratios, 5 bans as
   absolutes, 6 palette + type roles and coverage only, 7 archetype names and when to use
   each, 8 the self-check last. To add a 10th signature, delete one. End PROMPT.md with:
   > Before returning any output, run every test in the self-check. Name each test and its
   > result. If any fails, repair and re-run. Never return output with a failing test and a
   > note explaining it away.
7. **Report uncertainty.** List every value inferred rather than measured and every rule
   under 70% confidence. That is where drift starts.

## Analyst rules

- Never invent a value you could measure; mark inferred values.
- Never copy real logos, wordmarks, licensed photos, or proprietary fonts: list them in
  `meta.not_copied` and substitute. Reproduce the system, never the marks.
- Every font family needs a fallback.
- If output looks generic, add a **ban**, not a rule. Bans should outnumber positive rules.
- One skill per style. Never merge two identities; the average of two good designs is a bad one.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Matches values, still generic | Moves missing or too many | Cut to 3-9, write as ratios |
| Drifts back to stock AI look | Too few bans | More bans than positive rules |
| Slide 1 and 8 don't match | No named layouts | Add archetypes |
| Accent reads as a theme | No coverage % | Add coverage |
| Works on slide, breaks on carousel | Pixel spacing | Convert to % |
| Obeys some rules, differently each run | Prompt over 2KB | Cut |
| Best rule ignored | Buried in the middle | Move to top or bottom |
| Fine but forgettable | No weird move | Find the one break |
| Spec complete, output wrong | Skipped step 5 | Rebuild from spec, diff |
