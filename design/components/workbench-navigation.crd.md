---
component: Workbench navigation
lifecycle: active
status: {requirements: complete, design_notes: complete, pre_dev_research: complete, usage: complete}
precedents: [portfolio-navigation]
---
# Workbench navigation

## 1. Requirements
Purpose: expose the full contents of the workbench.
Anatomy: sidebar, browse disclosure, category links, section links, counts, download link.
- F1: Category links include all resources, AI skills, systems/UI kits, UX patterns, plugins/tools, reading and Saved.
- F2: Section links reach prompts, tools, templates and practices.
- S1: The selected category link has a visible current state.
- B1: The sidebar stays available during desktop scrolling.
- B2: The browse disclosure collapses on mobile and exposes the selected category label.
- B3: Escape closes the mobile browse disclosure and focuses its summary.
- B4: Following a category or section link closes the mobile browse disclosure.
- C1: Counts derive from resource data or actual Saved state.
- A1: Category links and section links use standard link semantics.
- A2: The expanded browse disclosure fits within the viewport and can scroll.
- I1: Existing library, tools, team-kit and practices URLs continue to work.
Out of scope: search and result matching, owned by Resource browser.
Ruled out: duplicated horizontal section navigation and a second row of category filter chips.

## 2. Design notes
One persistent directory rail on desktop. A native details disclosure on mobile. Ordinary links keep section destinations usable without JavaScript.
## 3. Pre-dev research
Use the existing native details pattern. W3C disclosure navigation supports conventional links without the specialized menu role. The existing bench-jump observer must not conflict with category routing.
## 4. Usage guidance
Use on the workbench only. The global portfolio header remains separate.
## Decision log
- 2026-10-15: AI skills and reusable prompts share an AI grouping in navigation, while their different file formats remain explicit.
