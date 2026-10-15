# Usage and client notes

Checked 15 October 2026. Recheck live documentation before changing settings or quoting prices. These are decision aids, not automatic configuration.

| Question | Working rule |
| --- | --- |
| Which client? | Detect Claude Code versus Cowork versus web chat. Do not send CLI commands to an interface that does not support them. |
| Which model/effort? | Keep the user's chosen model. For a new selection, compare scope, difficulty, latency and quality using a representative task. Use deeper effort when its observed benefit warrants it. |
| Is caching helping? | Inspect actual reported cache statistics where available. A model switch may require a new cached prefix. Effort changes depend on model, request format and feature support; do not promise they always preserve cache. |
| What is the cost? | Separate API token estimates, subscription limits and actual billed credits. Record unavailable attribution as unknown. |
| Long pause? | Preserve a useful milestone or handoff. Do not create keep-alive calls by default; they create activity and consumption. For an explicit request, explain the tradeoff and use the client's authorized scheduling workflow. |
| Too much context? | Narrow reads, remove irrelevant branches from the working summary, and load relevant references on demand. Save decisions before a reset. |
| Too many extensions? | Inspect the installed tools and actual loading behavior. Tool discovery and deferred schemas vary by version. Do not assume each extension loads its entire content on every request. |
| Old sessions? | Check the client's current retention behavior and workspace policy before suggesting changes. Do not set a universal one-year retention period or promise recovery of deleted history. |

Claude Code commands such as `/context`, `/usage`, `/compact`, `/rewind` and `/btw` are client/version-specific. Confirm availability before using them. A status-line modification, model router or paid tool is an optional project with its own scope, not a dependency of this workflow.

Local personal skills under `~/.claude/skills/` serve local Claude Code sessions. Cowork and cloud sessions use account-enabled skills, and cloud sessions can also use committed project skills. Local installation does not mean the skill was enabled on the user's Claude account.

Primary references: [costs](https://code.claude.com/docs/en/costs), [model configuration](https://code.claude.com/docs/en/model-config), [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [skill locations and client coverage](https://code.claude.com/docs/en/skills).
