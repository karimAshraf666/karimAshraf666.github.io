---
name: agent-context-handoff
description: Preserve decisions, evidence and work state before compaction, an AI session handoff or a recovery from repeated failed approaches. Use for long-running work with Claude or another agent.
---

# Agent context handoff

Capture enough verified state for the next agent to take the next action without redoing the investigation. Read current changes and recent user direction before writing; do not rely on an older summary when the working state has changed.

Use [handoff.md](handoff.md) to record the objective, accepted decisions, source locations, completed work, file/branch state, actual checks, unresolved issues and next action. Preserve exact definitions, confidential-asset restrictions and existing authorization when relevant. Distinguish observation, hypothesis and untested proposal.

Keep the handoff concise by linking artifacts and evidence. Do not paste secrets, private messages or raw research into a public artifact. Preserve unrelated user changes and identify them separately from task edits.

When a repeated failure needs a new approach, record what failed and what evidence changed. A transition is useful only if the next attempt starts with a better constraint or hypothesis. Do not repeatedly rerun the same failing action without new information.

Before a reset or rewind, preserve needed work and inspect the restore scope. Claude Code checkpoints do not cover shell changes or external actions; use the appropriate scoped backup or recovery mechanism. Never reset a dirty repository or delete a conversation merely to improve context efficiency.

Return the handoff and the next concrete action. Continue the current task unless the user requested a transition; do not create a new chat or message another one without authorization.

Original adaptation by Karim Ashraf, informed by [the RoboNuggets tutorial](https://www.youtube.com/watch?v=gvESqM6s0kM), [Claude Code session guidance](https://code.claude.com/docs/en/best-practices#manage-your-session) and [checkpoint limitations](https://code.claude.com/docs/en/checkpointing). Reviewed 15 October 2026.
