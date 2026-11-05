# Extract, map and migrate an existing system

Choose audit/report, canonical extraction, token mapping, documentation or selected-call-site migration. An audit does not imply a rewrite. Preserve client tokens instead of importing an external theme.

## Map by meaning

Inventory token definitions, aliases/modes, component families, stories and actual uses. Record authority per fact and conflicts between code, Figma and requirements. Current implementation does not override intended CRD requirements.

Map semantic purpose before numeric equality. An 8px gap cannot become an 8px radius token; border gray is not text gray. Resolve alias chains/modes first. Record source file:line | property/role | value | candidate token | classification | reason. Classify exact semantic match, documented deviation, ambiguous or system gap. Leave ambiguity/gaps unresolved and propose a decision instead of choosing the nearest number.

## Extract and document

Read implementation, stories and representative call sites before describing props, slots and events. Include accessible names, keyboard behavior and relevant state/tone matrix. Generate API/geometry views and link them from the CRD; keep requirements/decisions there. Select one canonical family and pilot before broad extraction.

## Pilot migration

Choose one component plus its hardest real call site. Check prop/slot parity, events, payloads, data-writing behavior and accessibility. Compare baseline/candidate under matching viewport, theme, fonts and fixtures. Review differences; never change baselines to conceal drift.

Use existing tests/lint where meaningful. Demonstrate a failing example and corrected passing case for a new drift check. Ratchet documented existing debt without requiring unrelated cleanup. Expand only within authorized scope after the pilot supports it.

Deliver mapping, evidence, unresolved decisions, pilot result and reversible next slice. This reference does not enable automatic branching, commits, CI changes, installations, agents or scheduled audits.

Original adaptation of arla6ka/design.how, MIT, commit b4140241a1b1b3d0b417c8c01b3462b0388f6a09, reviewed 2026-11-05. Source: https://github.com/arla6ka/design.how . No themes, effect vault or executable helpers imported.
