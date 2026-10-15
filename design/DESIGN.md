# Karim portfolio design context

The current identity originates in redesign.css. Evidence originates in docs/EVIDENCE-INVENTORY.md. Resource data originates in scripts/build_workbench.py. The generated resource catalog and workbench page mirror that data.

## Convert on touch

The discovery refinement uses design/tokens/discovery.css. New navigation and directory rules use those tokens. Existing unaffected styles remain in styles.css, redesign.css and workbench.css. Do not bulk-migrate unrelated CSS during a navigation task.

Use existing components. A new component needs a CRD before implementation. Component behavior originates in design/components/. Geometry and visual values originate in tokens. Keep one origin for each fact. Log decisions with their reasons. An unresolved open marker in an active CRD requires Karim's input. Keep unknown evidence empty.

## Identity

Manrope with system-ui fallback. Pale paper and white surfaces dominate. Cobalt indicates action and selection, ink carries headings, muted ink carries supporting text. Preserve at least 4.5:1 body contrast, visible keyboard focus, readable text measure and reduced-motion support. The directory shows category choices and content, rather than decorative counters or a large marketing hero.

## Components

- portfolio-navigation.crd.md: global navigation and Workbench emphasis.
- workbench-navigation.crd.md: directory sidebar and mobile disclosure.
- resource-browser.crd.md: category routes, filters, Saved and results.

The existing resource cards, practical tools, native disclosures, templates and forms remain the building blocks. Keep storage key karim-design-workbench-v1 and all original resource IDs. Build the page through scripts/build_workbench.py and scripts/portfolio_shell.py so regeneration preserves the structure.

## Motion and accessibility

Navigation never depends on animation. The library remains usable without JavaScript, with all resources and native anchor links available. Search and saved-state enhancement require JavaScript. The mobile browse panel closes after navigation or Escape, and desktop navigation stays available. Focus must move to the resulting heading when a collapsed mobile panel would otherwise contain the active element.

## Review evidence

Reference captures and final screenshots live in the private Career workspace output/workbench-discovery/. The review record is DESIGN-LOOP-LOG.md. New documentation does not imply Karim has previously deployed these practices at an employer.
