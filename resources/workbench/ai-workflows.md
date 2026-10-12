# AI-assisted design workflows

## Expand an interaction-state specification

Turn a bounded brief into a reviewable matrix of states and recovery paths.

Act as a product design partner. Use the supplied brief and existing component rules.
Input: [user task], [platform], [existing pattern], [backend signals], [constraints].
Create a table: state, trigger, visible feedback, available action, data preserved, recovery, accessibility/RTL check, acceptance test.
Distinguish confirmed backend behavior from assumptions. Include interruptions and uncertain outcomes when relevant. Do not invent capabilities or auto-retry rules.
Finish with open questions for design, engineering and QA. Mark all suggested behavior as a proposal for human review.

Review: Review triggers and retry behavior with engineering before using the output as a specification.

## Synthesize research with traceable evidence

Keep observations and interpretation separate while drafting findings.

Use only the approved, anonymized notes below. Every note has an evidence ID.
Group observations into themes without inventing quotes, sample sizes or prevalence.
For each theme provide: evidence IDs, observation, interpretation, contradictory evidence, confidence limits and a question to investigate.
Then propose opportunities and explain which evidence supports each. Separate proposed solutions from findings.
If the notes do not support a claim, say insufficient evidence.
Input: [research question] [notes with evidence IDs].

Review: Check every evidence reference and preserve disagreements; a plausible summary is not validation.

## Review an AI-assisted prototype

Create a structured review against an agreed brief and component system.

Review the supplied prototype and brief. Use the actual component system and acceptance criteria supplied here.
Check task completion, labels, permissions, loading/error/empty states, recovery, responsive behavior, Arabic/English content and accessibility.
For each observable issue provide: location, expected behavior, actual behavior, impact, proposed severity, reproduction steps and a verification check.
Separate observed issues from untested risks. Do not declare a flow tested if you have only seen screenshots.
Input: [brief] [component rules] [prototype/screens] [test results].

Review: Run the important interactions yourself and agree issue severity with the team.

## Prepare a component contribution brief

Make a proposal understandable to design, engineering and system owners.

Draft a component proposal from the supplied facts.
Include recurring user need, existing patterns considered, why reuse/extension is or is not sufficient, anatomy, properties, states, content rules, accessibility, RTL, design-to-code mapping, owner, test cases and rollout.
Include alternatives and tradeoffs. Highlight gaps as open questions. Do not claim the proposal has been adopted or measured.
Input: [problem] [examples] [current library] [constraints] [proposed behavior].

Review: The system owner and engineering partner decide whether to extend, add or reject the proposal.