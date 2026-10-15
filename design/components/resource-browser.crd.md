---
component: Resource browser
lifecycle: active
status: {requirements: complete, design_notes: complete, pre_dev_research: complete, usage: complete}
precedents: [workbench-navigation, existing resource cards]
---
# Resource browser

## 1. Requirements
Purpose: help people find and use the existing resource collection.
Anatomy: heading, description, search, industry selector, result count, resource cards, Saved actions, reset action, show-more action.
- F1: The AI skills category contains every resource whose type is AI skills.
- F2: Search and industry selection refine the selected category.
- F3: Saved actions persist existing resource IDs under the existing storage key.
- F4: Saved export includes source, worksheet and agent-guide links.
- B1: Category routes work on direct page load and browser Back/Forward.
- B2: Changing category clears unrelated search and industry constraints.
- B3: Reset clears search and industry while preserving the selected category.
- B4: Show more reveals further matching resource cards.
- S1: Zero matches shows an explanation and a route to search all resources.
- C1: The heading names the active category.
- C2: Each resource card retains its worksheet, agent guide and source.
- C3: The source action appears before expandable guidance and companion files. AI skill source and companion guide have distinct labels.
- A1: Result changes announce through a status region.
- A2: Hidden resource cards have no keyboard-reachable controls.
- I1: Generator rebuilds preserve category navigation and resource packages.
- I2: Browser-local practical tool drafts survive the refinement.
Out of scope: changing third-party resources or claiming prior adoption.
Ruled out: a Refine popover duplicating categories already visible in the sidebar.

## 2. Design notes
Keep search and one industry selector. Group AI skill labels by their work area. Use actual source data for category counts. Preserve no-script access to the full collection.
## 3. Pre-dev research
Existing cards already carry stable IDs, type and industry tags. Saved state and drafts share one storage object. Extend that behavior instead of replacing the store or rebuilding the practical tools.
## 4. Usage guidance
Use the category links to browse, search to narrow a category, and Saved to keep a personal shortlist.
## Decision log
- 2026-10-15: Use hash routes so AI skills and other collections can be shared without another page or client framework.
- 2026-10-15: Put source actions before supporting guidance after independent review found the skill action too difficult to discover on mobile.
