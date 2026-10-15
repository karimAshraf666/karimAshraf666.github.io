---
name: component-crd
description: >
  Write, update, or build from a Component Reference/Requirements Document (CRD): one living,
  human-written, agent-readable file per UI component that carries requirements, decisions,
  rejected options, design notes, dev research and usage. Use for "new component", "add a
  component", "spec this component", "CRD", "component requirements", "amend <component>",
  or before building any component in a design system. Read sibling CRDs first.
---

# Component CRD

Method: Cassie Groos, "Probabilistic isn't a dirty word" (Design Systems Collective, Aug 2026)
and Hatch 2026 talk. 8 months in production, 58 CRDs; v2 structure below.

**What it is:** one file per component, co-authored by PM/designer/dev and maintained by
agents, travelling with the component from "someone asked for this" to "a page-building
agent needs to know how to use it". It carries what Figma, code and agent rules *can't*
tell you: behaviour, accessibility intent, edge cases, decisions and their reasons.

**What it isn't:** a props table, a token list, a changelog (that's git), or pretty docs.

## Before writing

1. Read the relevant **sibling CRDs** (a new menu item reads MenuRow; a new card reads the
   other cards). Inherit their precedents and say which ones you used.
2. Read `design/DESIGN.md`, `decisions/`, `ruled-out.md`.
3. Never invent: unknown = leave empty or mark `[open]`.

## File: `design/components/<name>.crd.md`

Use `template.md` in this folder. Key mechanics:

- **Frontmatter** tracks `lifecycle` (requested | backlog | active | built | deprecated) and a
  per-section `status`. Lifecycle lives in frontmatter, never in folder location: files never move.
- **Amendment block** (top, above section 1) when changing a shipped component. Readers see
  it's under revision before acting. Fold it in when resolved, then delete the block.
- **Section 1: Requirements** states only what is true now:
  Purpose · Scope · **Anatomy** (named parts; every statement uses only these nouns. If you
  need another word, the anatomy is incomplete) · numbered **ID'd statements**:
  `F` functional · `S` states · `B` behaviour · `C` content · `A` accessibility · `I` integration.
  - Every ID'd line is **atomic and testable**. "Leading OR trailing icon, never both" passes;
    "icons feel balanced" fails. A line that could be half-satisfied is two lines.
  - Not machine-testable? Prefix `[review]` (human eyeballs it).
  - Hunches and unknowns: prefix `[open]`. **A build agent that meets `[open]` stops and asks.**
  - **Out of scope** (belongs to another component) and **Ruled out** (rejected, with who/why,
    to stop re-litigation) sit next to the requirements.
- **Section 2: Design notes**, written back by design as they work. Variants/states that changed
  go back into section 1 (the CRD is their origin). Spacing/visual spec is NOT repeated: it lives in Figma/tokens.
- **Section 3: Pre-dev research**: how the codebase and other CRDs already solve it, industry
  standards, implementation decisions, questions. (Devs were doing this anyway and losing it in prompts.)
- **Section 4: Usage guidance**: when to use, when not and what to use instead. Docs and
  page-building agents read this.
- **Decision log**: dated one-liners with the why, in the same commit as the work.
  Log it if someone could plausibly propose the opposite.

**Ready for dev** is computed, never stored: requirements + design notes complete, joint
design/dev review done, zero `[open]`, zero open questions.

**Don't put in:** acceptance-criteria lists (section 1 *is* the list), changelogs, code
props tables, Figma-to-code mappings, cross-component rules (token wiring, global a11y,
naming, responsiveness belong in DESIGN.md / build skill once).

## Building from a CRD

1. Check ready-for-dev. If not ready, stop and report what's missing.
2. Generate tests from the IDs (one or more per ID; test names cite the ID).
3. Build using only tokens and existing primitives.
4. A failing test points back to the statement that required it.
5. Anything learned goes back into the CRD (section 2/3 or decision log) in the same session.
