# Preserve work across a session transition

Use at a natural milestone, before compaction, or after repeated corrections reveal a bad approach. This is a continuity record, not a new task or authorization to reset a conversation.

```markdown
# Working handoff
Objective and current user direction:
Decisions, reasons, clearance status, permitted use and authorized destinations:
Verified facts and source locations:
Completed changes and artifact paths:
Current files, branch and unrelated work to preserve:
Checks actually run and their results:
Hypotheses, failed approaches and unresolved questions:
Existing authorization and any pending user decision:
Next concrete action:
```

Exclude secrets and raw private transcripts from a public handoff. Link authorized records instead. Preserve exact names, metric definitions and compatibility constraints when they matter; an approximate summary can change the task.

In Claude Code, use the supported compaction or rewind interface when appropriate. Inspect what rewind will restore first. Claude's checkpoints cover its direct file edits; shell edits and external side effects require their own recovery path. Preserve dirty user work and prefer a scoped diff or backup over resetting an entire repository.

In other clients, supply the handoff to the existing conversation or a user-requested new one. Never claim a new chat or successful recovery was created unless verified.

References: [checkpointing](https://code.claude.com/docs/en/checkpointing), [session management](https://code.claude.com/docs/en/best-practices#manage-your-session).
