# T3 Code as a shared agent workspace

Use this reference for a requested T3 Code setup or task that benefits from managing
existing coding providers in one workspace. T3 Code is a tool, not a model or a source of
unlimited AI usage. Keep ordinary single-provider work in its current client unless a
change serves the requested task.

## Set up and verify the actual environment

- Check the installed app release and the provider status on the machine executing the
  work. The official Windows package is `T3Tools.T3Code`; use the project's current
  installation documentation rather than a video's command from memory.
- Prefer the user's existing supported Codex CLI or Claude Code login when appropriate.
  Do not copy credential files between homes or publish account details. New account
  approvals belong to the user. Provider subscriptions, usage limits and compute remain
  separate from the app.
- Confirm providers are ready in the installed app and inspect any compatibility warning.
  A CLI version or a successful app launch alone does not prove a model request works.
  Any smoke test should use a harmless, authorized task and report its actual result.
- Keep model choice and permission mode explicit. Do not enable unattended activity,
  broad permissions, remote sharing, extra hosts or automatic paid fallback simply because
  the tool supports them.

## Use it for bounded work

Keep each task's outcome, project and ownership clear. For parallel code changes, choose
separate branches/worktrees when independent edits would otherwise collide; read-only
reviews do not automatically need another worktree. Inspect the combined result before
treating independent successes as a completed delivery.

Hand over relevant decisions and evidence with a thread reference or concise summary.
Treat completion, waiting for input, and deliberately deferred work as different states.
Use the current app's task-management controls when requested or needed, while preserving
the user's organization and notification preferences.

Remote access is optional. Pairing and MCP links can grant persistent access to the host;
keep them private and check scope/revocation before any specifically authorized setup.
Local installation does not authorize LAN exposure, a public tunnel or new connectors.

## Sources and scope

Reviewed 2026-11-02. Original adaptation, not an official T3 skill.

- [Theo's walkthrough](https://www.youtube.com/watch?v=uLGxb4F3SyI): complete auto-caption
  transcript reviewed. Useful segments cover provider coordination (6:34-9:43), thread
  states (16:17-21:17), contextual handoffs (27:23-29:02), worktrees (29:47-30:11) and
  inspectable diagnostics/attachments (33:41-35:14). Performance, user-count and savings
  claims are not adopted as verified facts.
- [Official installation and provider requirements](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md).
- [Codex accounts](https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-codex.md)
  and [Claude accounts](https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-claude.md).
- [Remote access](https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md).

Recheck changing UI, supported providers and compatibility against the installed release.
