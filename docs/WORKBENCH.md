# Design Workbench

The workbench supports reusable product design work across banking/finance, B2B SaaS, commerce, AI products and shared practices. It describes resources by purpose and application without asserting past adoption or a Staff employment title.

## Structure

- Resource library: 67 references, industry/type/search filters, saved items, shortlist export and progressive disclosure. The "AI skills" type holds agent skills: 13 hosted in `resources/workbench/skills/` (also bundled as `design-ai-skills.zip`) and third-party skills linked at their source (GitHub or the author's post).
- Practical tools: editable interaction-state specification, evidence-oriented quality review and proposed decision brief. Drafts are browser-local and can be exported to the team's existing workspace.
- Team kit: eight general templates, the AI design skills bundle, four AI prompt workflows, CSV/JSON catalogs and an AI-agent index.
- Per-resource files: self-contained HTML human worksheet, CSV worksheet and Markdown agent guide, with required inputs, output structure and acceptance checks.

Third-party libraries and plugin assets are linked, not repackaged. Access notes distinguish public references, account/plan constraints, engineering setup and provider-specific scope. The catalog was checked against primary sources on 12 October 2026. AI design workflow sources and skills (Design DNA, ScrollCraft, the Hatch 2026 design-systems talk, the CRD article, reference and generation platforms, motion graphics and AI film workflows) were added on 15 October 2026. Keep links and access notes current when editing the library.

The 2 November 2026 update adds source videos from Tyler Mommsen, Paula Scher, the product-context and Notion talks, and Theo's T3 Code walkthrough. Brand art direction and product context review have hosted skills with timestamped source notes. The motion skill includes renderer and iteration guidance. T3 Code has a separate tool entry linked to its official repository; provider access, usage limits and compute remain separate from its app license. These entries describe reusable practice without claiming past adoption or a completed local installation.

## Maintenance

Run `python scripts/build_workbench.py` after changing resources or templates in that file. `scripts/workbench_resource_packages.py` generates the human/agent packages. The builder regenerates workbench.html, resource files, catalogs and the ZIP; it does not change scoped CSS or JavaScript. It adds the navigation link only when missing. Preserve independent portfolio changes.

Per-resource fields and related source links live in `RESOURCE_FIELDS` and `RESOURCE_LINKS`. The motion, brand and product-context skills have complete individual ZIPs alongside the four Claude workflow packages. Supporting references stay inside the skill folders in every download. After refreshing a canonical skill folder, rebuild the Workbench so the HTML, catalogs and bundles agree.

## Verification

Check browser interactions, exported content, offline worksheet behavior, ZIP integrity, local references and anchors, and responsive layouts. Review coverage in the QA tool is not an accessibility certification or a pass score. No confidential company screens or live Playful URL are part of this feature.
