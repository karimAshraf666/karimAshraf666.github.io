# Workbench discovery and portfolio navigation

## Karim's request

> it feels like my current workbench on my portfolio is hard to navigate and discover what's actually avaialbe i think it can use a side navigation there maybe, also AI skills should be categorized together too for ease for reach, what do u think we can do to improve it? also i want the workbench tap to be a bit highlithed somehow to have people wanna see it

> u can optimize the portfolio generally too

## Build target

Make the existing library usable as a directory within Karim's current portfolio identity. Keep the pale background, Manrope, cobalt accent, floated global navigation and approved product screens. Visitors should see the available categories immediately, reach all AI skills directly, and keep access to templates, prompts and browser-local tools.

Primary audience: Karim and collaborators using the resources, plus hiring teams inspecting his product judgment and useful team artifacts. This is a refinement of the existing site. Existing claims and confidentiality decisions remain authoritative in docs/EVIDENCE-INVENTORY.md.

## Reference lock

- Dominant visual reference: the live Karim portfolio and its existing redesign.css. Preserve its colors, font, rounded controls and restrained motion.
- Structure reference: Carbon's separation of foundations, implementation and practices, studied at https://www.carbondesignsystem.com/. Apply its clear task categories, without copying its brand or rebuilding this as an enterprise dashboard.
- Behavior reference: W3C disclosure navigation at https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/. Use ordinary links, native disclosure, Escape dismissal and visible focus. No ARIA menu role.
- Existing header uses ink 15px labels, cobalt active tint and a 1120px content measure. Workbench content may use a wider directory frame, with a 224px sidebar and two resource columns. The deliberate accent is the Workbench utility link, not an additional color.

## Scope

Persistent desktop sidebar, mobile browse disclosure, category deep links, AI skills together, dedicated prompts section, simple search plus industry, preserved Saved and drafts. Highlight Workbench across the portfolio, move its homepage introduction earlier, give images intrinsic dimensions and lighter previews, and remove the font stylesheet import chain.

Do not add resources, claims of adoption, new case-study outcomes, cleared Money Fellows screens or a Playful live link. Do not publish separate resume drafts.
