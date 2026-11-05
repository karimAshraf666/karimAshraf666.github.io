---
name: ui-dimensional-spec
description: Create source-backed UI dimension sheets and component anatomy specifications from code, tokens, Figma or measured renders. Use for spacing, sizing, responsive geometry and implementation handoff diagrams.
---

# UI dimensional specification

Produce a readable component drawing whose measurements trace to a source. This technical drawing format does not prescribe the product's style.

1. Identify the component, variants/states, source revision and consumer. Inspect the CRD, tokens, implementation and design source. Preserve their authority; expose conflicts.
2. Record viewport, render scale, theme, fonts and fixture content. Distinguish declared, computed, screenshot-observed and unknown values. A screenshot cannot establish token names, hidden padding, physical dimensions or responsive rules.
3. Draw compact anatomy and necessary details. Label content-dependent dimensions HUG, FLEX or FILL. Include state/breakpoint views where geometry changes.
4. Give each dimension a code and a source-linked table row. Read [references/drawing-conventions.md](references/drawing-conventions.md). Unknown values stay [TBD]; do not invent precision.
5. Prefer self-contained HTML and inline SVG with selectable text and an accessible HTML table. At 390px show a readable overview with zoom/scroll for details; do not shrink labels into illegibility. Existing project artifact conventions take precedence.
6. Render and inspect: annotation collisions, table coverage, formulas, provenance and responsive claims. If rendering is unavailable, label the result a draft and list unchecked items.

The sheet is a generated view, never a second source of truth. Regenerate from its linked revision when values change. Link it from the CRD; requirements remain in the CRD. For explicitly requested animation use motion-graphics and its dimensional-spec-motion reference. Static specifications do not require video or renderer installation.

Original adaptation informed by enesozturk/dimensional-drawing, MIT, commit 5c457437c8c83524308aad3b7443e81adcc13153, reviewed 2026-11-05. Source: https://github.com/enesozturk/dimensional-drawing . No upstream scripts/templates bundled.
