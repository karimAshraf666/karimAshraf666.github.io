from pathlib import Path
import html, json, zipfile, csv, io
from workbench_resource_packages import build_resource_packages
from portfolio_shell import simplify_workbench

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / 'resources/workbench'
KIT.mkdir(parents=True, exist_ok=True)

# Curated primary sources, checked October 12, 2026. No claim of prior adoption.
resources = [
 ('confirmation','Review before confirmation','UX patterns','banking commerce shared','A clear review step before submitting important information.','Adapt this public-service pattern to important actions: let users inspect and correct information before confirming.','Specify what can be reviewed, what can be changed and which action commits the request.','Public GOV.UK pattern','https://design-system.service.gov.uk/patterns/check-answers/'),
 ('plaid','Account connection & recovery','UX patterns','banking','Authentication interruptions, unavailable institutions and recovery.','Useful for mapping account-linking exceptions with engineers. Plaid implementation and regional coverage are separate decisions.','Produce an exception matrix: trigger, user message, next action and owner.','Public docs; service access separate','https://plaid.com/docs/link/troubleshooting/'),
 ('rtl','Arabic & bidirectional content','Articles & guidance','banking saas commerce ai shared','Direction, mixed Arabic/Latin content and structural reading order.','Use when specifying RTL behavior; pair the HTML guidance with platform-specific implementation checks.','Test amounts, dates, identifiers, wrapping and directional icons in one journey.','Public guidance','https://www.w3.org/International/questions/qa-html-dir'),
 ('carbon','Carbon design resources','Systems & UI kits','saas banking','Component libraries and supporting design assets for complex products.','Useful for enterprise patterns and library structure. Choose relevant public assets rather than importing everything.','Review a recurring pattern, then write usage guidance for your team.','Public kits; Figma workspace plan applies','https://www.carbondesignsystem.com/getting-started/designing/design-resources'),
 ('tables','Dense tables & batch actions','UX patterns','saas commerce banking','Sorting, selection, expansion and actions over operational data.','Use when a user needs to find, compare or act on many records.','Specify selection scope, permissions and the consequences of a batch action.','Public guidance and demos','https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines'),
 ('fluent','Fluent 2 UI kits','Systems & UI kits','saas ai shared','Code-aligned Figma libraries across web and native mobile.','Useful for studying component structure, variable organization and platform differences.','Inspect one component\'s design properties alongside its implementation API.','Public kit links; Figma workspace plan applies','https://fluent2.microsoft.design/get-started/design'),
 ('baymard','Checkout friction research','Articles & guidance','commerce','Research on checkout steps, account selection and unnecessary effort.','Use the public article to challenge checkout assumptions before adding more fields.','Map every required field to a real need; test guest and returning-user paths.','Public article; wider research is paid','https://baymard.com/research-articles/current-state-of-checkout-ux'),
 ('polaris','Merchant admin patterns','UX patterns','commerce saas','Shopify app layouts, resource indexes and task-oriented admin pages.','Useful for merchant-facing products. These patterns target the Shopify ecosystem.','Compare an operational page against its resource-index and detail-page patterns.','Public web-component patterns','https://shopify.dev/docs/api/app-home/latest/patterns'),
 ('hax','Microsoft HAX Toolkit','UX patterns','ai','Human-AI guidelines, examples, a workbook and failure-planning tools.','Use before designing an AI feature to agree expectations, correction and recovery.','Run a focused team session and prioritize three interaction risks.','Public toolkit and workbook','https://www.microsoft.com/en-us/haxtoolkit/'),
 ('pair','People + AI Guidebook','Articles & guidance','ai','Mental models, explainability, feedback, control and graceful failure.','Useful when users must understand or question uncertain AI output.','Define what the user sees, what they can correct and when human review is needed.','Public chapters and worksheets','https://pair.withgoogle.com/guidebook-v2/chapters'),
 ('material','Material 3 patterns','Systems & UI kits','banking commerce ai shared','A mobile-oriented reference for layouts, components and interaction.','Use alongside the target platform\'s conventions and your team\'s brand system.','Compare a mobile flow at compact and expanded sizes before selecting a pattern.','Public reference; linked kit access varies','https://m3.material.io/foundations/layout/canonical-examples/overview'),
 ('uswds','USWDS forms & design assets','Systems & UI kits','banking saas shared','Accessible service patterns and official Figma/Sketch design assets.','Useful for form-heavy, high-trust services; adapt to your product and jurisdiction.','Document one form\'s labels, validation, error summary and recovery.','Public design-kit downloads','https://designsystem.digital.gov/documentation/getting-started-for-designers/'),
 ('tokens','Tokens Studio for Figma','Plugins','shared banking saas commerce ai','Token organization, reusable values and optional external storage.','Add when native variables no longer meet the agreed token workflow.','Pilot one token set with engineering and document its source of truth.','Plugin available; some features require Pro','https://docs.tokens.studio/'),
 ('stark','Stark for Figma','Plugins','shared banking saas commerce ai','Accessibility inspection inside design files.','Useful for contrast, focus-order and other design checks; verify the relevant plan and test the built product too.','Review one flow and attach findings to the design QA checklist.','Free account entry; features vary by plan','https://www.getstark.co/figma/'),
 ('iconify','Iconify for Figma','Plugins','shared banking saas commerce ai','Search and import vector icons from multiple sets.','Choose a consistent family and check the selected set\'s license.','Agree one family, size and direction rule instead of mixing styles.','Public plugin; licenses vary by icon set','https://iconify.design/docs/design/figma/'),
 ('wcag','WCAG 2.2 understanding','Articles & guidance','shared banking saas commerce ai','Detailed accessibility explanations and associated techniques.','Use to define acceptance criteria with engineering and accessibility specialists.','Translate relevant requirements into testable journey-level checks.','Public guidance','https://www.w3.org/WAI/WCAG22/Understanding/'),
 ('contrast','WebAIM contrast checker','Tools','shared banking saas commerce ai','Check foreground and background color pairs.','Use for an immediate contrast check; a passing color pair is one part of accessibility.','Review actual token pairings, including error, disabled and muted content.','Public browser tool','https://webaim.org/resources/contrastchecker/'),
 ('carbonqa','Component contribution checklist','Articles & guidance','shared banking saas commerce ai','An example of quality expectations across design, code, tests and documentation.','Useful when proposing a component or defining what complete means.','Adapt the checklist to a component proposal with an owner and evidence.','Public checklist','https://www.carbondesignsystem.com/getting-started/contributing/component-checklist'),
 ('storybook','Storybook accessibility testing','Tools','saas commerce banking shared','Accessibility checks within coded component stories.','Partner with engineers when the team uses Storybook; combine automated checks with manual testing.','Ask for stories covering error and loading states, then review the results together.','Open-source tooling; engineering setup required','https://storybook.js.org/docs/writing-tests/accessibility-testing'),
 ('dtcg','Design Tokens format','Articles & guidance','shared banking saas commerce ai','A common exchange format from the Design Tokens Community Group.','Useful when tokens need to move between tools. Confirm support in the chosen pipeline.','Agree names, aliases, owners and an export contract before automating.','Public Community Group specification','https://www.designtokens.org/tr/2025.10/format/'),
 ('codeconnect','Figma Code Connect','Tools','saas commerce ai shared','Connect design components to their real implementation.','Useful when design and engineering maintain corresponding components; check plan access first.','Map one component, review its properties and document the mapping owner.','Figma plan eligibility and engineering setup apply','https://developers.figma.com/docs/code-connect/'),
 ('mcp','Figma MCP & agent workflows','Tools','saas commerce ai shared','Supply design context to an AI agent and support structured Figma workflows.','Use selected, well-structured frames and explicit rules; verify client access and permissions.','Pilot a bounded flow using existing components, then review layout, states and behavior.','Supported client and Figma access limits apply','https://developers.figma.com/docs/figma-mcp-server/'),
 ('heuristics','Ten usability heuristics','Articles & guidance','shared banking saas commerce ai','A shared vocabulary for finding interaction problems.','Use to structure a critique, then validate important findings with user evidence.','Record an observable issue, its impact and a proposed check rather than a taste-based verdict.','Public article','https://www.nngroup.com/articles/ten-usability-heuristics/'),
 ('research','Research synthesis practice','Articles & guidance','shared banking saas commerce ai','A practical approach to separating observations, findings and actions.','Use after a research session to make evidence traceable and discuss it with the team.','Create an observation-to-finding-to-decision trail with evidence IDs.','Public service manual','https://www.gov.uk/service-manual/user-research/analyse-a-research-session'),
 # AI design workflow sources and skills, added October 15, 2026.
 ('designdna-video','Consistent AI design with Design DNA','Articles & guidance','ai commerce saas shared','Jack Roberts on the consistency problem: a design loop that critiques output against a reference, then codifies the winner into a reusable style.','Use when AI-made designs look good once but drift or turn generic on the next run.','Pick one approved piece and list the ratios, colour coverage and refusals that make it work.','Public video (20 min)','https://www.youtube.com/watch?v=cM5n9priMjo'),
 ('designdna-method','Design DNA method','Articles & guidance','ai shared','A written method for turning one design into rules that can fail: relationships over values, one deliberate break, bans, tests and a rebuild from the spec.','Use when writing a style specification an AI agent must reproduce across formats.','Rebuild a reference from your written rules alone, then list every difference as a missing rule.','Public Notion page','https://app.notion.com/p/Design-DNA-One-beautiful-design-into-a-permanent-skill-3bee8d6bd1378159ab0ee0b9a88f44f8'),
 ('scrollcraft-video','Scroll-driven website design with AI','Articles & guidance','commerce saas ai','Nate Herk on a website skill that interviews for the visitor journey, builds scroll-led pages and screenshots its own work before review.','Use when a marketing page needs a clear journey and a memorable moment rather than a template layout.','Write the journey section by section, mark where it should feel calm or intense, and name the one moment to remember.','Public video (17 min)','https://www.youtube.com/watch?v=QUI6Ug4cHnE'),
 ('agents-talk','Design systems in the age of agents','Articles & guidance','shared saas ai banking commerce','Cassie Groos (Hatch 2026) on agents as a third design-system consumer, context before components, and humans keeping judgment and accountability.','Use when agents assemble UI from your system and the misses look polished but are not yours.','List the facts an agent had to guess in its last build, then decide where each should be written once.','Public conference talk (31 min)','https://www.youtube.com/watch?v=JeJhPtsbIGA'),
 ('crd-article','Component requirements document (CRD)','Articles & guidance','shared saas ai banking commerce','One living, human-written and agent-readable document per component: testable requirement IDs, open markers, ruled-out options and dated decisions.','Use when requirements, design notes and implementation decisions drift between documents.','Draft one CRD for an existing component and mark every unknown as open instead of guessing.','Public article (14 min read)','https://www.designsystemscollective.com/probabilistic-isnt-a-dirty-word-37fa836bedd8'),
 ('ai-writing','Signs of AI writing','Articles & guidance','shared commerce saas ai banking','A catalogue of patterns that make text read as machine-written: staged contrasts, reflex triads, inflated claims and filler.','Use when reviewing interface copy, landing pages or emails drafted with AI.','Mark every pattern in one page of copy, then rewrite only those lines and compare.','Public Wikipedia guidance','https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing'),
 ('savee','Savee','Tools','shared commerce ai','A visual library for finding and saving design references across posters, layouts and brand work.','Use to lock a visual reference before generating or designing, rather than starting from a written brief alone.','Collect three references for one brief and choose a single dominant direction.','Free account','https://savee.com/'),
 ('refero','Refero','Tools','saas commerce banking ai shared','Searchable styles, real product screens and user flows, with an MCP server for AI agents.','Use for reference research on screens and flows before designing; connect the MCP when agents do the research.','Compare three shipped flows for one task and record what each does differently.','Browsing available; MCP research needs a paid plan','https://refero.design/'),
 ('higgsfield','Higgsfield','Tools','commerce ai shared','One account for many image and video generation models, available to agents through an MCP server and CLI.','Use when a build needs custom imagery or motion that matches an agreed palette and style.','Generate one asset from a written style rule and check it against the reference.','Paid credits','https://higgsfield.ai/'),
 ('kieai','kie.ai','Tools','commerce ai shared','A single API for many image and video models, used by the ScrollCraft skill for asset generation.','Use when an agent workflow needs generated images or video through one key.','Budget one asset set, record the prompts used and review the output against the brand.','Paid credits; API key required','https://kie.ai/'),
 ('fishaudio','Fish Audio','Tools','commerce ai shared','Voice generation with a large voice library, emotion tags and an API for narration.','Use for narrated motion graphics or product explainers.','Draft one 10-second narration, tag its emotional beats and review it with the visuals.','Free tier; paid plans and API','https://fish.audio/'),
 ('skill-website-craft','Website craft skill','AI skills','commerce saas ai shared','An agent workflow for websites: short interview, references, a design system page, anti-slop copy, build and screenshot verification.','Use for any new or redesigned website or landing page built with an AI agent.','Run it on one page with real assets and review the screenshots section by section.','Free SKILL.md for Claude Code, Codex and compatible agents','https://karimashraf666.github.io/resources/workbench/skills/website-craft/SKILL.md'),
 ('skill-design-loop','Design loop skill','AI skills','ai commerce saas shared','Builds against a reference while separate critic passes check fidelity, brief, craft and AI tells until each passes.','Use when a design must match a reference or keeps looking generic.','Run four rounds at most and keep the critic verdicts with the final screenshots.','Free SKILL.md for Claude Code, Codex and compatible agents','https://karimashraf666.github.io/resources/workbench/skills/design-loop/SKILL.md'),
 ('skill-design-dna','Design DNA skill','AI skills','ai commerce shared','Turns one approved design into a reusable style: dna.json, a short prompt, tests that can fail and a rebuild check.','Use after a design is approved, or when a recurring format must stay consistent.','Codify one approved piece, then produce a second piece from the skill alone and compare.','Free SKILL.md and schema','https://karimashraf666.github.io/resources/workbench/skills/design-dna/SKILL.md'),
 ('skill-agent-system','Agent-ready design system skill','AI skills','shared saas ai banking commerce','Sets up or audits a design system agents can build from: one origin per fact, tokens only, decision logs and drift reviews.','Use when starting a growing product or when agents keep inventing components and values.','Audit one repository for raw values and undocumented variants, then rank fixes by guessing removed.','Free SKILL.md','https://karimashraf666.github.io/resources/workbench/skills/agent-ready-design-system/SKILL.md'),
 ('skill-component-crd','Component CRD skill','AI skills','shared saas ai banking commerce','Writes and builds from a component requirements document, with testable IDs and open markers that stop a build.','Use before designing or building a new component.','Write one CRD, generate tests from its IDs and record what design changed.','Free SKILL.md and template','https://karimashraf666.github.io/resources/workbench/skills/component-crd/SKILL.md'),
 ('skill-scroll-craft','ScrollCraft','AI skills','commerce saas ai','Nate Herk\'s skill for scroll-driven landing pages with layered heroes, a signature move and automated screenshot checks.','Use when a page should feel like an experience: scrubbed video, pinned scenes or depth.','Build one section from your own photos first; add generated assets only if needed.','MIT on GitHub; needs Node, ffmpeg and Playwright; generation uses a kie.ai key','https://github.com/nateherkai/scroll-craft'),
 ('skill-humanizer','Humanizer','AI skills','shared commerce saas ai banking','A skill that rewrites AI-sounding text without changing what it says, based on Wikipedia\'s Signs of AI writing.','Use as a final pass on any user-facing copy drafted with AI.','Run it on one page of copy and check that no facts changed.','MIT on GitHub','https://github.com/blader/humanizer'),
 ('skill-refero','Refero design skill','AI skills','saas commerce banking ai shared','A research-first design workflow with bundled craft guides, using Refero\'s MCP for live references.','Use for the reference and research step before designing.','Keep a client\'s own design system above the skill\'s defaults; record the references it chose.','MIT on GitHub; live research needs Refero MCP','https://github.com/referodesign/refero_skill'),
 # Motion and AI video sources and skills, added October 15, 2026.
 ('motion-video','Premium motion graphics with Claude','Articles & guidance','commerce saas ai shared','Duncan Rogoff on five habits that lift AI-made promo videos: references, a written study, a motion design system, stills first and designer notes.','Use when a promo or launch video made with an AI agent looks generic or off-brand.','Approve one still per scene type before rendering any video, and log every note as a rule.','Public video (6 min)','https://www.youtube.com/watch?v=Wkf2IjZrRt4'),
 ('prompt-motion','Prompt Motion','Tools','commerce saas ai shared','A gallery of motion videos made with Claude, each posted with its full prompt, model and rendering stack.','Use to find and compare motion references before writing a brief; take the feel, never the facts.','Study two detailed prompts and list the scenes, timing rules and bans each one specifies.','Free gallery','https://prompt-motion.com/'),
 ('aifilm-video','AI film workflow with Claude skills','Articles & guidance','commerce ai shared','Joey on building the world before the shots: story bible, locked characters, scene plates, then shot prompts, with a low-resolution draft pass.','Use when AI-generated characters or scenes drift between generations, or credits run out on retries.','Draft one scene at 480p, review framing and dialogue, then render only the approved prompt at full resolution.','Public video (22 min); sponsored by Higgsfield','https://www.youtube.com/watch?v=LOUEH3DzLro'),
 ('elevenlabs','ElevenLabs','Tools','commerce ai shared','Voice generation with multiple takes, word timings and an API for narration and captions.','Use when a promo needs voiceover that captions and cuts can follow.','Generate four takes of one script and pick the best by listening, not by prompt.','Free tier; paid plans and API','https://elevenlabs.io/'),
 ('moises','Moises','Tools','commerce ai shared','Audio separation that isolates or removes music, voice and instruments from a track.','Use to remove unwanted background music from generated video audio before editing.','Separate one clip and check the dialogue stays clear after the music is removed.','Free tier; paid plans','https://moises.ai/'),
 ('skill-motion-graphics','Motion graphics skill','AI skills','commerce saas ai shared','Coded motion promos: references, a motion design system, approved stills, then a frame-exact HTML build rendered with Playwright and ffmpeg.','Use for product promos, launch films, UI motion and kinetic type built with an AI agent.','Render six stills, approve them, then the video, and keep a changelog of each review round.','Free SKILL.md; needs Node, Playwright and ffmpeg','https://karimashraf666.github.io/resources/workbench/skills/motion-graphics/SKILL.md'),
 ('skill-ai-film','AI film pipeline skill','AI skills','commerce ai shared','Runs an AI-generated film or ad in order: world bible, characters, scene plates, shot prompts, draft pass, final render and a credit log.','Use for AI-generated ads, skits, music videos or character series.','Keep a production log of model, resolution and credits for every shot.','Free SKILL.md; generation tools are paid','https://karimashraf666.github.io/resources/workbench/skills/ai-film-pipeline/SKILL.md'),
 ('skill-film-joey','AI film skills by Joey','AI skills','commerce ai shared','Five free skills: Story Bible Builder, Castkit characters, Scenecraft plates, Shotcaller for Seedance and Motiondojo for motion transfer.','Use with the AI film pipeline when building characters, scenes and shot prompts for video models.','Lock one character face before building outfits or a character sheet.','Free from the author on Higgsfield','https://higgsfield.ai/@joeysnoisygroup/blogs/all-my-claude-skills-for-better-prompting'),
]

# Claude workflow adaptations. Existing resources retain their earlier review date.
claude_skills = [
 ('skill-claude-workflow','Claude workflow','AI skills','shared saas commerce banking ai','A practical operating workflow for Claude: task alignment, focused context, appropriate effort and observable verification.','Use when briefing Claude or improving a team workflow across Claude Code, Cowork and chat. Commands depend on the client.','Take one recurring task, write its completion check and compare the result with the current approach.','Free SKILL.md with supporting guides; no API key or plugin required','https://karimashraf666.github.io/resources/workbench/skills/claude-workflow/SKILL.md'),
 ('skill-task-brief','Agent task brief','AI skills','shared saas commerce banking ai','Turn an unclear request into a useful brief with sources, constraints and acceptance checks.','Use before substantial design, research or implementation work when the outcome or scope is unclear.','Brief one onboarding review using the existing component library and mark every material unknown.','Free SKILL.md and editable Markdown template','https://karimashraf666.github.io/resources/workbench/skills/agent-task-brief/SKILL.md'),
 ('skill-context-handoff','Agent context handoff','AI skills','shared saas commerce banking ai','Preserve decisions, evidence, file state and next actions across long sessions and handoffs.','Use before compaction, a requested session transition or a change of approach after repeated failures.','Hand a bounded task to a teammate using the template, then check whether they can continue without repeating the audit.','Free SKILL.md and editable Markdown template','https://karimashraf666.github.io/resources/workbench/skills/agent-context-handoff/SKILL.md'),
 ('skill-extension-review','Agent extension review','AI skills','shared saas commerce banking ai','Assess an AI skill, plugin, mod or connector before adding it to a workflow.','Use when an extension promises efficiency but its execution, access, context loading or maintenance cost is unclear.','Review one candidate at a named version and record what remains uninspected before recommending a pilot.','Free SKILL.md and editable Markdown template; review does not install anything','https://karimashraf666.github.io/resources/workbench/skills/agent-extension-review/SKILL.md'),
]
claude_references = [
 ('claude-mistakes-video','23 Claude workflow mistakes','Articles & guidance','shared saas commerce banking ai','Jay E / RoboNuggets discusses habits that affect context, output quality and usage.','Use as a discussion starter; check changing product details against current documentation. The companion PDF requires community access.','Pick one relevant habit, propose a bounded workflow change and verify it on your own task.','Public video and transcript; linked community guide has separate access','https://www.youtube.com/watch?v=gvESqM6s0kM'),
 ('claude-practices','Claude Code working practices','Articles & guidance','shared saas commerce banking ai','Official guidance on task context, verification, session management and reusable workflows.','Use when defining how a team briefs and checks agent-assisted implementation work.','Choose one real task and define a completion check that the agent can actually run.','Public Anthropic documentation; commands require a compatible Claude Code version','https://code.claude.com/docs/en/best-practices'),
 ('claude-usage','Claude usage and context costs','Articles & guidance','shared saas commerce banking ai','Official guidance for interpreting usage, cache statistics and context costs.','Use when a workflow consumes unexpected usage or a proposed optimization needs evidence.','Record the client, model, available usage data and output quality before changing one workflow variable.','Public Anthropic documentation; subscription usage and API estimates differ','https://code.claude.com/docs/en/costs'),
 ('claude-mcp','MCP connector setup and trust','Articles & guidance','shared saas commerce banking ai','Official reference for connecting tools, inspecting access and understanding tool discovery.','Use before proposing a new connector or changing a team integration.','Compare one bounded connector use case with the existing workflow and document permissions and a rollback path.','Public Anthropic documentation; workspace and provider permissions apply','https://code.claude.com/docs/en/mcp'),
]
first_skill = next(i for i, resource in enumerate(resources) if resource[2] == 'AI skills')
resources[first_skill:first_skill] = claude_skills
resources.extend(claude_references)
claude_resource_ids = {r[0] for r in [*claude_skills, *claude_references]}
claude_skill_folders = dict(zip([r[0] for r in claude_skills], ['claude-workflow','agent-task-brief','agent-context-handoff','agent-extension-review']))

prompts = [
 ('states', 'Expand an interaction-state specification', 'Turn a bounded brief into a reviewable matrix of states and recovery paths.', '''Act as a product design partner. Use the supplied brief and existing component rules.
Input: [user task], [platform], [existing pattern], [backend signals], [constraints].
Create a table: state, trigger, visible feedback, available action, data preserved, recovery, accessibility/RTL check, acceptance test.
Distinguish confirmed backend behavior from assumptions. Include interruptions and uncertain outcomes when relevant. Do not invent capabilities or auto-retry rules.
Finish with open questions for design, engineering and QA. Mark all suggested behavior as a proposal for human review.''', 'Review triggers and retry behavior with engineering before using the output as a specification.'),
 ('evidence', 'Synthesize research with traceable evidence', 'Keep observations and interpretation separate while drafting findings.', '''Use only the approved, anonymized notes below. Every note has an evidence ID.
Group observations into themes without inventing quotes, sample sizes or prevalence.
For each theme provide: evidence IDs, observation, interpretation, contradictory evidence, confidence limits and a question to investigate.
Then propose opportunities and explain which evidence supports each. Separate proposed solutions from findings.
If the notes do not support a claim, say insufficient evidence.
Input: [research question] [notes with evidence IDs].''', 'Check every evidence reference and preserve disagreements; a plausible summary is not validation.'),
 ('review', 'Review an AI-assisted prototype', 'Create a structured review against an agreed brief and component system.', '''Review the supplied prototype and brief. Use the actual component system and acceptance criteria supplied here.
Check task completion, labels, permissions, loading/error/empty states, recovery, responsive behavior, Arabic/English content and accessibility.
For each observable issue provide: location, expected behavior, actual behavior, impact, proposed severity, reproduction steps and a verification check.
Separate observed issues from untested risks. Do not declare a flow tested if you have only seen screenshots.
Input: [brief] [component rules] [prototype/screens] [test results].''', 'Run the important interactions yourself and agree issue severity with the team.'),
 ('handoff', 'Prepare a component contribution brief', 'Make a proposal understandable to design, engineering and system owners.', '''Draft a component proposal from the supplied facts.
Include recurring user need, existing patterns considered, why reuse/extension is or is not sufficient, anatomy, properties, states, content rules, accessibility, RTL, design-to-code mapping, owner, test cases and rollout.
Include alternatives and tradeoffs. Highlight gaps as open questions. Do not claim the proposal has been adopted or measured.
Input: [problem] [examples] [current library] [constraints] [proposed behavior].''', 'The system owner and engineering partner decide whether to extend, add or reject the proposal.'),
]

templates = {
 'decision-record.md': '''# Design decision record
Status: Proposed / Accepted / Superseded
Owner:
Reviewers and decision date:
Related journey, design file and issue:

## Problem and user impact
## Evidence and constraints
Link observations and evidence IDs. Separate assumptions.
## Options considered
For each: user impact, delivery cost, accessibility and tradeoffs.
## Decision and rationale
## Acceptance checks
## Rollout, rollback and dependencies
## What would change this decision?
## Follow-up measure, baseline and review date
''',
 'component-contribution.md': '''# Component or pattern contribution
Owner:
Engineering partner:
Status: Proposed

## Recurring need and examples
## Existing patterns evaluated
Reuse / Extend / Add, with rationale.
## Anatomy and properties
## States and recovery
Trigger | Feedback | Action | Preserved data | Acceptance test
## Tokens and design-to-code mapping
## Usage, content and exceptions
## Accessibility and Arabic/RTL checks
## Test evidence and unresolved issues
## Adoption, migration and deprecation plan
## Reviewers and release owner
''',
 'design-qa.csv': 'Journey,Build or design URL,Device and language,Expected behavior,Actual behavior,Impact,Severity,Owner,Status,Evidence link,Verification steps,Review date\n,,,,,,,,Not reviewed,,,\n',
 'state-matrix.csv': 'Pattern,Platform,State,Trigger,Visible feedback,Available action,Data preserved,Recovery,Accessibility and RTL check,Acceptance test,Owner\n,,,,,,,,,,\n',
 'adoption-review.md': '''# Design system adoption review
Scope and sampled journeys:
Owner and review date:

## Baseline
Sample size, time period and method. Do not infer coverage from component count.
## Pattern usage
Expected pattern | observed use | exception reason | owner | next action
## Recurring quality issues
Severity, user impact, evidence and frequency in the sample.
## Delivery friction
Where designers or engineers detach, override or rebuild components and why.
## Priorities
One bounded improvement, expected benefit and a follow-up measure.
## Decisions and accepted exceptions
## Next review
''',
 'industry-pattern-review.md': '''# Industry pattern review
Industry and user task:
Pattern and reference URL:
Research / guidance / observed example:

## What this pattern solves
## How our users and context differ
## What we can reuse
## What requires adaptation
Platform, language, permissions, risk, policy and backend capabilities.
## States and failure paths
## Test plan and evidence needed
## Decision, owner and next review
''',
 'ai-context-pack.md': '''# AI workflow context pack
Task and intended output:
User, platform and language:
Approved inputs and evidence IDs:
Existing components, token names and content rules:
Confirmed backend capabilities:
Constraints and unknowns:
Acceptance criteria:
Things the assistant must not invent:
Human reviewer and verification method:

## Workflow
Bound the task -> supply approved context -> generate a draft -> review evidence and behavior -> test -> record the decision.
''',
 'team-pilot.md': '''# One-week team pilot
## Choose one recurring problem
Journey, user impact and current baseline:
Design owner:
Engineering/QA partner:
Existing tools and components:

## Day 1: agree the need
Inspect current work and select the smallest useful pattern.
## Days 2-3: specify and build
Write states and acceptance checks; agree a decision and owner.
## Days 4-5: review and learn
Check implementation and adoption; record remaining issues.

## Decision
Keep / Adapt / Stop, with evidence.
## Next step
Owner, review date and measure. Roll out beyond the pilot only after the team agrees.
''',
 'ai-workflows.md': '# AI-assisted design workflows\n\n' + '\n\n'.join('## '+p[1]+'\n\n'+p[2]+'\n\n'+p[3]+'\n\nReview: '+p[4] for p in prompts),
 'README.md': '''# Design Workbench team kit

Reusable templates by Karim Ashraf for product design teams. Start with one journey and use your existing tools. These templates can be edited, copied and shared within your team. Third-party resources are linked separately and retain their own licenses and access requirements.

## Minimal working setup
- Figma: existing components, native variables, properties and prototypes.
- Implementation: the team's existing code library and component review environment.
- Team records: put these templates in your shared document, issue tracker or repository.
- AI assistance: use approved context and a bounded prompt, then review and test the output.

## Pick by task
- Decide across teams: decision-record.md.
- Propose a reusable pattern: component-contribution.md and state-matrix.csv.
- Review delivery: design-qa.csv.
- Improve adoption: adoption-review.md.
- Adapt an industry pattern: industry-pattern-review.md.
- Guide an AI assistant: ai-context-pack.md and ai-workflows.md.
- Introduce a workflow: team-pilot.md.
- Run AI design workflows: skills/ (SKILL.md files for Claude Code, Codex and compatible agents).

## Per-resource packages
Each resource has an editable HTML team worksheet, a CSV worksheet for spreadsheets, and a Markdown working guide for AI agents in resource-guides/. Start from AGENT-INDEX.md to choose an agent guide. resource-catalog.json provides the source URL and file mapping for every resource; resource-catalog.csv is a portable human-readable index.

CSV templates can be imported into a spreadsheet. Markdown templates can be pasted into your team's existing documentation tool. Copy the templates to the team's workspace; browser drafts on the portfolio page are local to each person's browser, not shared collaboration. Resource worksheets are self-contained HTML: their fields and brief exports work offline when opened from the extracted kit. Neighboring CSV/MD links require the accompanying files.
''',
}
for name, text in templates.items():
    (KIT / name).write_text(text, encoding='utf-8')

packages = build_resource_packages(KIT, resources)
catalog = [dict(zip(['id','name','type','industries','purpose','when','practice','access','url'], r)) | packages[i] | ({'checked':'2026-10-15'} if r[0] in claude_resource_ids else {}) for i,r in enumerate(resources)]
(KIT / 'resource-catalog.json').write_text(json.dumps({'checked':'2026-10-12','catalogUpdated':'2026-10-15','resources':catalog}, indent=2, ensure_ascii=False), encoding='utf-8')
with (KIT / 'resource-catalog.csv').open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Resource','Type','Industries','Purpose','When to use','Team practice','Access','Source URL','Human worksheet','CSV template','AI agent guide'])
    labels = {'banking':'Banking and finance','saas':'B2B SaaS','commerce':'Commerce','ai':'AI products','shared':'Shared practices'}
    for i,r in enumerate(resources):
        writer.writerow([r[1],r[2],'; '.join(labels[x] for x in r[3].split()),*r[4:],packages[i]['humanTemplate'],packages[i]['csvTemplate'],packages[i]['agentGuide']])
with zipfile.ZipFile(KIT / 'design-workbench-team-kit.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for name in [*templates, 'resource-catalog.json', 'resource-catalog.csv', 'AGENT-INDEX.md']:
        z.write(KIT / name, 'design-workbench/' + name)
    for path in sorted((KIT/'resource-guides').glob('*')):
        z.write(path, 'design-workbench/resource-guides/' + path.name)
    for path in sorted((KIT/'skills').rglob('*')):
        if path.is_file(): z.write(path, 'design-workbench/skills/' + path.relative_to(KIT/'skills').as_posix())
# Standalone bundle of the hosted AI design skills (third-party skills stay on GitHub).
with zipfile.ZipFile(KIT / 'design-ai-skills.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted((KIT/'skills').rglob('*')):
        if path.is_file(): z.write(path, path.relative_to(KIT/'skills').as_posix())

# Complete per-skill packages keep supporting files beside the entrypoint.
downloads = KIT / 'skill-downloads'
downloads.mkdir(exist_ok=True)
for folder in claude_skill_folders.values():
    with zipfile.ZipFile(downloads / f'{folder}.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for path in sorted((KIT / 'skills' / folder).rglob('*')):
            if path.is_file(): z.write(path, path.relative_to(KIT / 'skills').as_posix())

def esc(s): return html.escape(s, quote=True)
cards = '\n'.join(f'''<article class="bench-card bench-resource" data-resource="{r[0]}" data-type="{esc(r[2])}" data-industries="{r[3]}">
 <p class="eyebrow">{esc(r[2])}</p><h3>{esc(r[1])}</h3><p>{esc(r[4])}</p>
 <div class="bench-links"><a data-source-link href="{esc(r[8])}" target="_blank" rel="noopener noreferrer">{'Get skill source' if r[2] == 'AI skills' else 'Open resource'} ↗<span class="visually-hidden">: {esc(r[1])}</span></a><button class="bench-favorite" type="button" aria-pressed="false" aria-label="Save {esc(r[1])}" hidden>☆</button></div>
 <details><summary>When to use &amp; team practice</summary><p>{esc(r[5])}</p><p><strong>Try with the team:</strong> {esc(r[6])}</p></details>
 <p class="bench-rule">{esc(r[7])}</p><div class="bench-resource-files"><a href="resources/workbench/resource-guides/{r[0]}-worksheet.html">Use team worksheet →<span class="visually-hidden">: {esc(r[1])}</span></a><a href="resources/workbench/resource-guides/{r[0]}-agent.md" download>Companion AI guide · MD ↓<span class="visually-hidden">: {esc(r[1])}</span></a></div>
</article>''' for r in resources)
for resource in claude_skills:
    rid,title = resource[:2]
    folder = claude_skill_folders[rid]
    save_button = f'<button class="bench-favorite" type="button" aria-pressed="false" aria-label="Save {esc(title)}"'
    package_link = f'<a href="resources/workbench/skill-downloads/{folder}.zip" download>Skill ZIP ↓<span class="visually-hidden">: {esc(title)}</span></a>'
    cards = cards.replace(save_button, package_link + save_button)

prompt_html = '\n'.join(f'''<details class="bench-prompt"><summary>{esc(p[1])}<small>{esc(p[2])}</small></summary><div class="bench-prompt-body"><pre id="prompt-{p[0]}">{esc(p[3])}</pre><p><strong>Human check:</strong> {esc(p[4])}</p><button class="bench-copy" type="button" data-copy="prompt-{p[0]}" hidden>Copy prompt</button></div></details>''' for p in prompts)

template_links = [
 ('decision-record.md','Decision record','Align on options, tradeoffs, ownership and a review date.','MD'),
 ('component-contribution.md','Component contribution','Propose a reusable pattern with states and acceptance checks.','MD'),
 ('design-qa.csv','Design QA log','Track expected behavior, findings, owners and verification.','CSV'),
 ('state-matrix.csv','Interaction-state matrix','Map triggers, feedback, preserved data and recovery.','CSV'),
 ('adoption-review.md','System adoption review','Find exceptions, recurring issues and delivery friction.','MD'),
 ('industry-pattern-review.md','Industry pattern review','Adapt a reference to your users, platform and constraints.','MD'),
 ('ai-context-pack.md','AI context pack','Give an assistant component rules, evidence and acceptance criteria.','MD'),
 ('team-pilot.md','One-week team pilot','Try one improvement with partners before broader adoption.','MD'),
 ('design-ai-skills.zip','AI design skills',f'{len(list((KIT / "skills").glob("*/SKILL.md")))} reusable skills for design, motion, Claude workflows, task briefs, handoffs and extension reviews.','ZIP'),
]
links = '\n'.join(f'<a class="bench-template" href="resources/workbench/{name}" download><span><strong>{title}</strong><small>{desc}</small></span><span>{kind} ↓</span></a>' for name,title,desc,kind in template_links)

page = '''<!doctype html>
<html lang="en">
<head>
 <meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />
 <title>Design Workbench | Karim Ashraf</title>
 <meta name="description" content="A reusable product design workbench: industry UX patterns, design systems, plugins, AI workflows and practical templates for teams." />
 <meta property="og:title" content="Design Workbench | Karim Ashraf" /><meta property="og:description" content="Useful patterns. Reusable practice. Resources and tools for product design teams." />
 <meta property="og:type" content="website" /><meta property="og:url" content="https://karimashraf666.github.io/workbench.html" /><meta property="og:image" content="https://karimashraf666.github.io/assets/og-portfolio.png" />
 <meta name="twitter:card" content="summary_large_image" /><meta name="theme-color" content="#f4f1ea" />
 <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='12' fill='%23f4f1ea'/><text x='31' y='45' font-family='Georgia,serif' font-size='40' text-anchor='middle' fill='%2315201c'>K</text></svg>" />
 <link rel="stylesheet" href="styles.css?v=20261006" /><link rel="stylesheet" href="workbench.css?v=20261012" />
</head>
<body class="bench-page" id="top">
 <a class="skip-link" href="#library">Skip to resource library</a>
 <header class="site-header"><div class="header-inner"><a class="brand" href="index.html" aria-label="Karim Ashraf portfolio home">Karim Ashraf<span>+</span></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" aria-label="Primary navigation"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="workbench.html" aria-current="page">Workbench</a><a href="blog.html">Blog</a><a href="index.html#contact">Contact</a></nav></div></header>
 <main>
 <section class="bench-hero" aria-labelledby="bench-title"><div><p class="eyebrow">Design workbench / Karim Ashraf</p><h1 id="bench-title">Useful patterns.<br /><em>Reusable practice.</em></h1><p class="hero-deck">Resources, tools and working practices for making product decisions clearer and helping a team deliver them well. Explore by industry, find a useful pattern, and take a template into your next review.</p><div class="button-row"><a class="button" href="#library">Explore the library</a><a class="button secondary" href="resources/workbench/design-workbench-team-kit.zip" download>Download team kit ↓</a></div></div>
 <aside class="bench-board" aria-label="A repeatable team workflow"><p class="eyebrow">From question to shared practice</p><h2>Make the next decision easier.</h2><ol><li><span>01</span><div><strong>Find the relevant pattern</strong><small>Match the task, industry and constraints.</small></div></li><li><span>02</span><div><strong>Define the behavior</strong><small>States, feedback, recovery and ownership.</small></div></li><li><span>03</span><div><strong>Review the implementation</strong><small>Check real behavior and document findings.</small></div></li><li><span>04</span><div><strong>Share what works</strong><small>Keep the decision and reusable guidance.</small></div></li></ol></aside></section>
 <div class="bench-jump"><nav aria-label="Workbench sections"><a href="#library">01 / Resource library</a><a href="#tools">02 / Practical tools</a><a href="#team-kit">03 / Team kit</a><a href="#practices">04 / Working practices</a></nav></div>
 <section class="bench-section" id="library" aria-labelledby="library-title"><div class="bench-intro"><p class="eyebrow">01 / Resource library</p><div><h2 id="library-title">The right reference for the problem in front of you.</h2><p>Industry patterns, useful articles, UI kits and tools. Each resource includes a use case and a practical way to apply it with a team.</p></div></div>
 <div id="library-controls" hidden><div class="bench-search-row"><label class="bench-field" for="resource-search">Search the library<input id="resource-search" type="search" placeholder="Try: recovery, Arabic, checkout, tokens…" /></label><label class="bench-field" for="resource-type">Resource type<select id="resource-type"><option value="all">All resource types</option><option>Systems &amp; UI kits</option><option>UX patterns</option><option>Articles &amp; guidance</option><option>Plugins</option><option>Tools</option><option>AI skills</option></select></label></div>
 <div class="bench-filters" role="group" aria-label="Filter by industry"><button class="bench-filter" data-industry="all" aria-pressed="true">All industries</button><button class="bench-filter" data-industry="banking" aria-pressed="false">Banking &amp; finance</button><button class="bench-filter" data-industry="saas" aria-pressed="false">B2B SaaS</button><button class="bench-filter" data-industry="commerce" aria-pressed="false">Commerce</button><button class="bench-filter" data-industry="ai" aria-pressed="false">AI products</button><button class="bench-filter" data-industry="shared" aria-pressed="false">Shared practices</button><button class="bench-filter" id="saved-only" aria-pressed="false">Saved items</button></div><div class="bench-result-bar"><p id="resource-count" role="status" aria-live="polite"></p><button class="bench-small-button" id="clear-filters" type="button">Clear filters</button><button class="bench-small-button" id="export-shortlist" type="button">Export saved list ↓</button></div></div>
 <div class="bench-grid" id="resource-grid">__CARDS__</div><p id="resource-empty" class="bench-empty" hidden>No matching resources. Try another term or clear the filters.</p><div class="bench-actions"><button id="show-more" class="bench-small-button" type="button" hidden>Show more resources</button></div><p class="bench-note">References stay with their original authors. Kit, plugin and integration access depends on the provider and your workspace. Use patterns as a starting point and adapt them to your users and implementation.</p></section>
 <div class="bench-band"><section class="bench-section" id="tools" aria-labelledby="tools-title"><div class="bench-intro"><p class="eyebrow">02 / Practical tools</p><div><h2 id="tools-title">Turn a review into a useful team artifact.</h2><p>Draft a state specification, record a quality review, or make a decision explicit. Export the result to your team's existing workspace.</p></div></div>
 <noscript><p>Interactive tools need JavaScript. The resource library and downloadable templates below remain available.</p></noscript>
 <div class="bench-tool" id="interactive-tools" hidden><div class="bench-tabs" role="tablist" aria-label="Practical design tools"><button class="bench-tab" id="tab-states" role="tab" aria-selected="true" aria-controls="panel-states" tabindex="0">State specification</button><button class="bench-tab" id="tab-qa" role="tab" aria-selected="false" aria-controls="panel-qa" tabindex="-1">Quality review</button><button class="bench-tab" id="tab-decision" role="tab" aria-selected="false" aria-controls="panel-decision" tabindex="-1">Decision brief</button></div>
 <section class="bench-panel" id="panel-states" role="tabpanel" aria-labelledby="tab-states"><h3>Specify the states people actually encounter.</h3><p>Select relevant states and create an editable specification. Complete the triggers, messages and acceptance checks before sharing it.</p><form id="state-form"><div class="bench-form-grid"><label class="bench-field" for="state-name">Pattern or journey<input id="state-name" name="name" placeholder="Example: transfer confirmation" maxlength="200" /></label><label class="bench-field" for="state-owner">Owner<input id="state-owner" name="owner" placeholder="Design + engineering partner" maxlength="200" /></label><label class="bench-field" for="state-platform">Platform<select id="state-platform" name="platform"><option>Mobile app</option><option>Web app</option><option>Shared tablet</option></select></label><label class="bench-field" for="state-language">Language<select id="state-language" name="language"><option>Arabic + English</option><option>English</option><option>Arabic</option></select></label><label class="bench-field wide" for="state-context">Task and confirmed constraints<textarea id="state-context" name="context" placeholder="What is the user trying to do? What can the system confirm?" maxlength="5000"></textarea></label></div><fieldset><legend>States to specify</legend><div class="bench-state-choices" id="state-choices"></div></fieldset><div class="bench-actions"><button class="button" type="submit">Create specification</button><button class="bench-small-button" id="state-example" type="button">Load a practice example</button></div></form><div class="bench-preview"><label class="bench-field" for="state-output">Editable specification<textarea id="state-output" rows="12" placeholder="Create a specification, then complete and edit it here."></textarea></label></div><div class="bench-actions"><button class="bench-small-button" data-copy="state-output" type="button">Copy specification</button><button class="bench-small-button" id="state-export" type="button">Download Markdown ↓</button></div></section>
 <section class="bench-panel" id="panel-qa" role="tabpanel" aria-labelledby="tab-qa" hidden><h3>Review quality with evidence and an owner.</h3><p>Mark the checks you have reviewed. Coverage is not a pass score: record findings, evidence and unresolved issues separately.</p><div class="bench-form-grid"><label class="bench-field" for="qa-journey">Journey / component<input id="qa-journey" maxlength="200" placeholder="What are you reviewing?" /></label><label class="bench-field" for="qa-build">Build or design reference<input id="qa-build" maxlength="1000" placeholder="Version or link" /></label><label class="bench-field" for="qa-owner">Review owner<input id="qa-owner" maxlength="200" placeholder="Who owns this review?" /></label><label class="bench-field" for="qa-scope">Device and language<input id="qa-scope" maxlength="200" placeholder="Example: Android, Arabic, large text" /></label></div><div class="bench-qa-heading"><span>Review coverage</span><strong id="qa-count" role="status" aria-live="polite">0 / 16 reviewed</strong></div><progress id="qa-progress" max="16" value="0" aria-label="Quality review coverage"></progress><div class="bench-checklist" id="qa-checklist"></div><div class="bench-form-grid"><label class="bench-field wide" for="qa-findings">Findings and evidence<textarea id="qa-findings" rows="4" placeholder="Expected vs actual behavior, user impact, severity, evidence and owner." maxlength="10000"></textarea></label><label class="bench-field wide" for="qa-blockers">Unresolved issues and next action<textarea id="qa-blockers" placeholder="What needs to happen next, who owns it, and how will you verify it?" maxlength="10000"></textarea></label></div><div class="bench-actions"><button class="button" id="qa-export" type="button">Download review ↓</button><button class="bench-small-button" id="qa-reset" type="button">Reset checks</button></div></section>
 <section class="bench-panel" id="panel-decision" role="tabpanel" aria-labelledby="tab-decision" hidden><h3>Give the team a decision it can revisit.</h3><p>Capture evidence, alternatives and responsibility. Keep unresolved questions visible.</p><form id="decision-form"><div class="bench-form-grid"><label class="bench-field" for="decision-title">Decision title<input id="decision-title" name="title" maxlength="200" placeholder="Example: extend the existing status pattern" /></label><label class="bench-field" for="decision-owner">Owner and reviewers<input id="decision-owner" name="owner" maxlength="200" /></label><label class="bench-field wide" for="decision-problem">Problem and user impact<textarea id="decision-problem" name="problem" maxlength="5000"></textarea></label><label class="bench-field wide" for="decision-evidence">Evidence, constraints and unknowns<textarea id="decision-evidence" name="evidence" maxlength="5000"></textarea></label><label class="bench-field" for="decision-options">Options and tradeoffs<textarea id="decision-options" name="options" maxlength="5000"></textarea></label><label class="bench-field" for="decision-choice">Proposed decision and rationale<textarea id="decision-choice" name="choice" maxlength="5000"></textarea></label><label class="bench-field" for="decision-checks">Acceptance and follow-up checks<textarea id="decision-checks" name="checks" maxlength="5000"></textarea></label><label class="bench-field" for="decision-rollout">Rollout, dependencies and review date<textarea id="decision-rollout" name="rollout" maxlength="5000"></textarea></label></div><div class="bench-actions"><button class="button" type="submit">Create decision brief</button></div></form><div class="bench-preview"><label class="bench-field" for="decision-output">Editable decision brief<textarea id="decision-output" rows="10" placeholder="Create a brief, then edit it here."></textarea></label></div><div class="bench-actions"><button class="bench-small-button" data-copy="decision-output" type="button">Copy brief</button><button class="bench-small-button" id="decision-export" type="button">Download Markdown ↓</button></div></section>
 <div class="bench-save-note"><p id="draft-storage-note">Drafts and saved resources stay in this browser. Download them to share with a team.</p><p class="bench-live" id="bench-status" role="status" aria-live="polite"></p></div></div></section></div>
 <section class="bench-section" id="team-kit" aria-labelledby="kit-title"><div class="bench-intro"><p class="eyebrow">03 / Team kit</p><div><h2 id="kit-title">Reusable files. A common way to work.</h2><p>Copy these into the team's existing documentation or issue tracker. Assign an owner, keep evidence attached, and adapt the level of detail to the decision.</p></div></div><div class="bench-templates">__TEMPLATES__</div><div class="bench-actions"><a class="button" href="resources/workbench/design-workbench-team-kit.zip" download>Download the complete kit ↓</a><a href="resources/workbench/README.md">Read the kit guide</a></div><div class="bench-evidence"><div><h3>Keep the library portable.</h3><p>Take the resource catalog with you, and export your saved shortlist from the library. The files work independently of this page.</p></div><a class="button secondary" href="resources/workbench/resource-catalog.json" download>Download catalog ↓</a></div></section>
 <div class="bench-band"><section class="bench-section" id="practices" aria-labelledby="practice-title"><div class="bench-intro"><p class="eyebrow">04 / Working practices</p><div><h2 id="practice-title">A small stack. A repeatable workflow.</h2><p>Start with the tools a team already uses. Add a tool when it solves a specific recurring problem and someone can own the workflow.</p></div></div><div class="bench-grid bench-stack"><article class="bench-card"><p class="eyebrow">01 / Design</p><h3>Figma foundations</h3><p>Native components, properties, variables and prototypes in the existing library.</p><p class="bench-rule"><strong>Team output:</strong> one agreed pattern with complete behavior.</p></article><article class="bench-card"><p class="eyebrow">02 / Implementation</p><h3>One shared reference</h3><p>Use the actual coded component library and its review environment. Add mapping when it helps.</p><p class="bench-rule"><strong>Team output:</strong> design and code names that correspond.</p></article><article class="bench-card"><p class="eyebrow">03 / Quality</p><h3>Evidence and ownership</h3><p>A shared QA log, acceptance checks and decisions in the team's current workspace.</p><p class="bench-rule"><strong>Team output:</strong> findings with owners and verification.</p></article><article class="bench-card"><p class="eyebrow">04 / AI assistance</p><h3>Bounded context</h3><p>Use an approved assistant with component rules, evidence and an explicit task.</p><p class="bench-rule"><strong>Team output:</strong> a reviewed draft, then a tested artifact.</p></article></div>
 <div class="bench-subheading"><h3>AI workflows you can reuse</h3><p>Supply the context pack, run a bounded task, and keep the human checks attached.</p></div>__PROMPTS__<div class="bench-actions"><a href="resources/workbench/ai-workflows.md" download>Download all prompts ↓</a></div>
 <div class="bench-subheading"><h3>Introduce the workbench through one useful pilot.</h3></div><div class="bench-plan"><article><p class="eyebrow">Understand</p><h3>Choose a recurring issue.</h3><p>Inspect an existing journey with a designer and engineer. Pick a pattern that causes uncertainty, inconsistency or rework.</p></article><article><p class="eyebrow">Make it concrete</p><h3>Agree behavior and checks.</h3><p>Use the state specification and decision brief. Keep the work bounded and record dependencies and ownership.</p></article><article><p class="eyebrow">Share and improve</p><h3>Review the real result.</h3><p>Check implementation and team use. Keep, adapt or stop the approach based on what the pilot shows.</p></article></div><div class="bench-evidence"><div><h3>See the product context behind the practice.</h3><p>Bluworks explores different operational contexts. Inveasy explains AI uncertainty and correction. The case studies show the decisions behind the work.</p></div><div class="bench-links"><a href="bluworks.html">Bluworks →</a><a href="one-more-thing.html">Inveasy →</a></div></div></section></div>
 </main><footer class="site-footer"><div class="footer-inner"><a href="index.html">Karim Ashraf / Portfolio</a><a href="#top">Back to top ↑</a><span>© <span data-year></span></span></div></footer>
 <script src="script.js?v=20261006"></script><script src="workbench.js?v=20261012"></script>
</body></html>
'''
page = page.replace('__CARDS__', cards).replace('__TEMPLATES__', links).replace('__PROMPTS__', prompt_html)
page = page.replace('href="resources/workbench/resource-catalog.json" download', 'href="resources/workbench/resource-catalog.csv" download')
page = page.replace('<meta name="twitter:card"', '<link rel="alternate" type="text/markdown" href="resources/workbench/AGENT-INDEX.md" title="AI agent resource index" /><meta name="twitter:card"')
page = page.replace('Each resource includes a use case and a practical way to apply it with a team.', 'Each resource includes a human worksheet, a CSV template, and a Markdown working guide for AI agents.')
page = page.replace('<p>Industry patterns, useful articles, UI kits and tools. ', '<p>Industry patterns, useful articles, UI kits, tools and AI design skills. ')
page = page.replace('<a href="resources/workbench/README.md">Read the kit guide</a>', '<a href="resources/workbench/README.md">Read the kit guide</a><a href="resources/workbench/AGENT-INDEX.md">Browse AI agent guides →</a>')
(ROOT / 'workbench.html').write_text(simplify_workbench(page), encoding='utf-8')

# Add a consistent entry point without overwriting prior task changes.
for path in ROOT.glob('*.html'):
    if path.name == 'workbench.html': continue
    text = path.read_text(encoding='utf-8')
    if 'href="workbench.html"' not in text:
        text = text.replace('<a href="blog.html">Blog</a>', '<a href="workbench.html">Workbench</a><a href="blog.html">Blog</a>')
        text = text.replace('<a href="blog.html" aria-current="page">Blog</a>', '<a href="workbench.html">Workbench</a><a href="blog.html" aria-current="page">Blog</a>')
        path.write_text(text, encoding='utf-8')
print(f'Built workbench with {len(resources)} resources, {len(template_links)} templates and {len(prompts)} AI workflows.')
