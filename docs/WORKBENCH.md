# Design Workbench

The workbench supports reusable product design work across banking/finance, B2B SaaS, commerce, AI products and shared practices. It describes resources by purpose and application without asserting past adoption or a Staff employment title.

## Structure

- Resource library: 43 references, industry/type/search filters, saved items, shortlist export and progressive disclosure. The "AI skills" type holds agent skills: five hosted in `resources/workbench/skills/` (also bundled as `design-ai-skills.zip`) and three third-party skills linked at their GitHub source.
- Practical tools: editable interaction-state specification, evidence-oriented quality review and proposed decision brief. Drafts are browser-local and can be exported to the team's existing workspace.
- Team kit: eight general templates, the AI design skills bundle, four AI prompt workflows, CSV/JSON catalogs and an AI-agent index.
- Per-resource files: self-contained HTML human worksheet, CSV worksheet and Markdown agent guide, with required inputs, output structure and acceptance checks.

Third-party libraries and plugin assets are linked, not repackaged. Access notes distinguish public references, account/plan constraints, engineering setup and provider-specific scope. The catalog was checked against primary sources on 12 October 2026. AI design workflow sources and skills (Design DNA, ScrollCraft, the Hatch 2026 design-systems talk, the CRD article, reference and generation platforms) were added on 15 October 2026. Keep links and access notes current when editing the library.

## Maintenance

Run `python scripts/build_workbench.py` after changing resources or templates in that file. `scripts/workbench_resource_packages.py` generates the human/agent packages. The builder regenerates workbench.html, resource files, catalogs and the ZIP; it does not change scoped CSS or JavaScript. It adds the navigation link only when missing. Preserve independent portfolio changes.

## Verification

Check browser interactions, exported content, offline worksheet behavior, ZIP integrity, local references and anchors, and responsive layouts. Review coverage in the QA tool is not an accessibility certification or a pass score. No confidential company screens or live Playful URL are part of this feature.
