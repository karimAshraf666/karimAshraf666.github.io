# Portable agent skills

Each named folder contains a SKILL.md entrypoint. Keep its supporting files and relative paths together. These are reusable working instructions, not integrations that grant file or account access.

For local Claude Code, copy a chosen folder into `~/.claude/skills/`. For local Codex, use `~/.codex/skills/`. Start a new session or use the client's supported reload mechanism, then check that the skill appears. Project-specific instructions and the user's request still apply.

Claude web and Cowork use skills enabled for the account; copying into a local folder does not enable them there. Use the client's current skill-upload controls for a chosen folder/package. Where a client does not support skills, supply SKILL.md and any referenced files as task context.

The Claude workflow, task brief, context handoff and extension review are original adaptations by Karim Ashraf, informed by Jay E / RoboNuggets' tutorial and official documentation. They are not copies of the creator's proprietary skills or companion PDF. Source links and review dates are in the files.

No API key, model router, recurring task or permission change is required to use these four workflows. Relevant commands and product behavior depend on the client and version; inspect current documentation before changing configuration.
