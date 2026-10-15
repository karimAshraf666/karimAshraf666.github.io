---
name: agent-ready-design-system
description: >
  Set up, audit, or extend a design system that AI agents (Claude Code, Codex, ChatGPT)
  can build from reliably, for a client or own product. Use for "design system", "set up
  tokens", "component library", "make our system AI-ready", "agents keep inventing
  components/spacing", "design drift", "brand system for <client>", or when starting any
  multi-page product or site that will keep growing. Uses component-crd for per-component
  records and design-dna for visual identity.
---

# Agent-Ready Design System

From Cassie Groos (design systems lead, Unily), "Design Systems in the Age of Agents",
Hatch 2026 (youtu.be/JeJhPtsbIGA), and her article "Probabilistic isn't a dirty word"
(Design Systems Collective, Aug 2026).

## The core idea

A design system now has three consumers: designers, developers and **agents**. Agents get
you ~80-85% of the way, and the misses now *look* polished: an invented variant, a prop
that doesn't exist, a spacing value no token produces. That's not a capability gap. It's a
**knowledge gap**: the model fills whatever wasn't made explicit. So:

- **Put context in first**, before components exist. Don't bolt it on later.
- **For humans it's documentation, for AI it's context.** Same knowledge, different artifact.
  Keep the human-authored source; generate pretty docs on demand.
- **Ship workflows, not just parts:** skills that tell agents how pages get built here.
  Without them you get seven versions of the same pattern.
- **Agents do the vigilance** (drift checks, keeping docs/design/code in agreement).
  **Humans own judgment, saying no, and accountability.** "The agent decided" is never an answer.

## What the system ships (create what's missing, in the repo)

```
design/
  DESIGN.md            entry point for humans AND agents: principles, where everything lives, rules
  tokens/              tiers: primitive -> semantic -> component (-> brand/theme if multi-brand)
  components/<name>.crd.md   one CRD per component (use component-crd skill)
  decisions/           dated one-line decisions with the why (ADR-lite), anything someone might reverse
  ruled-out.md         things considered and rejected, so agents stop re-proposing them
  dna/                 visual identity skill(s) from design-dna, one per brand
.claude/skills/        project skills: build-page, add-component, review-drift (+ the DNA skill)
AGENTS.md / CLAUDE.md  short: points to design/DESIGN.md and lists the hard rules
```

Optional later: an MCP server or CLI exposing tokens/components; Storybook as the API reference.

## Hard rules to write into DESIGN.md

1. **One origin per fact.** Every fact is stated once where it originates; everywhere else
   links or mirrors it. Two origins for one fact = guaranteed drift.
   (Variants/props/states originate in the CRD; spacing and visual spec originate in
   Figma/tokens; the API originates in code/Storybook.)
2. **Only tokens.** No raw hex, px, or ms in components. A value not in the token set is a bug
   or a proposal, never a silent addition.
3. **Only existing components and props.** If a page needs something that doesn't exist,
   stop and propose a CRD. Don't improvise.
4. **`[open]` means stop.** An agent that meets an `[open]` marker or open question in a CRD
   stops and asks the human. It does not guess.
5. **Log decisions where they're made.** Rule of thumb: could someone plausibly propose the
   opposite? Then log it (date, decision, why). If a decision recurs, promote it to a rule here.
6. **Empty beats invented.** When converting or migrating, leave unknown sections empty.
   Guessed content looks approved.
7. **Convert on touch.** Don't bulk-migrate old docs; upgrade a file when it is substantively edited.

## Workflow: new system (client or own)

1. Gather brand inputs (existing site, brand kit, Figma, references). Run **design-dna** on the
   strongest existing piece, or on the design-loop winner.
2. Write tokens (primitive -> semantic -> component), with descriptive names in comments.
3. Write `DESIGN.md` + hard rules above + `ruled-out.md` (seed it from the interview).
4. For each core component (button, input, card, nav, modal...), write a CRD **before** building.
5. Build the components; tests come from CRD requirement IDs.
6. Create project skills: `build-page` (assemble only from the system), `add-component`
   (CRD first), `review-drift` (see below).
7. Generate the human docs page (`/system`) from the sources. Never hand-maintain a second copy.

## Workflow: audit an existing system ("why do agents keep drifting?")

Report, with file:line evidence: raw values bypassing tokens; components/variants used
in code but not documented (or vice versa); duplicated facts across docs/Figma/code;
missing decision logs; missing `ruled-out`; components with no CRD; stale docs. Rank the fixes
by how much guessing each removes.

## review-drift (the vigilance job, run on a schedule or before release)

Compare CRDs <-> code <-> tokens <-> docs. Flag: props in code not in CRD, CRD variants not
built, raw values, docs older than their source, `[open]` markers past their date, and
product-team feedback not yet routed. Output a short drift report; never auto-"fix" a
decision. Route it to the human owner.

## Canvas vs code

Screen and flow design can move into AI-first/code tools. **Component-level design is where
judgment density is highest**: keep a visual, zoomed-in place for it (Figma or rendered
component sheets) and don't let it become developer-led by default. Agents do the labour
(variant matrices, states); humans do the judgment.
