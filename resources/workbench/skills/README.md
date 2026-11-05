# Portable agent skills

Each named folder contains a SKILL.md entrypoint. Keep its supporting files and relative paths together. These are reusable working instructions, not integrations that grant file or account access.

For local Claude Code, copy a chosen folder into `~/.claude/skills/`. For local Codex, use `~/.codex/skills/`. Start a new session or use the client's supported reload mechanism, then check that the skill appears. Project-specific instructions and the user's request still apply.

Claude web and Cowork use skills enabled for the account; copying into a local folder does not enable them there. Use the client's current skill-upload controls for a chosen folder/package. Where a client does not support skills, supply SKILL.md and any referenced files as task context.

The Claude workflow, task brief, context handoff and extension review are original adaptations by Karim Ashraf, informed by Jay E / RoboNuggets' tutorial and official documentation. They are not copies of the creator's proprietary skills or companion PDF. Source links and review dates are in the files.

No API key, model router, recurring task or permission change is required to use these four workflows. Relevant commands and product behavior depend on the client and version; inspect current documentation before changing configuration.

Brand art direction and product context review are Karim's adaptations of the linked talks. Their source notes separate speaker examples from reusable guidance. The motion graphics skill includes renderer and iteration notes with links to official framework documentation. Copy each complete folder, including references; a SKILL.md file alone can leave required context behind.

Brand art direction helps develop and test an identity before an approved look is codified with Design DNA. Product context review helps choose a useful next action from the available evidence. Both preserve the current project's decisions and tools. A motion brief can use the motion skill without starting video production or installing a renderer.


The 5 November 2026 repository adaptations add UI dimensional specifications and references for screenshot/task review, semantic token mapping, coordinated identity production and measured-sheet motion. See [source review and limits](../resource-guides/design-source-adoption.md). Awwwards has a [public research recipe](../resource-guides/awwwards-research.md); its optional MCP server was not installed.
