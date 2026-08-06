# Security Notes

Applications Dashboard is a local command runner. Treat configuration as executable behavior.

## Local Commands

Each instance can run a local command or executable. Review configuration before starting any service.

Be especially careful with:

- `shell: true`.
- Commands imported from JSON.
- Absolute paths from untrusted sources.
- Arguments that include scripts, network calls, or destructive operations.

## Import Safety

JSON import is intended for trusted backups and known project configurations.

Before importing:

- Read the commands.
- Check working directories.
- Check dependency chains.
- Check `autoStart` and `useInternalFolder` values — imported instances may be flagged to start automatically or to write to the panel's internal folder.
- Decide whether replacing all current instances is safe.

## Deleting Instances

Deleting an instance is available only from Settings. This keeps destructive actions away from the main dashboard cards.

## Advanced Settings

Advanced settings are locked after creation. This reduces the chance of changing execution behavior accidentally after an instance is already in use.

## Advanced Features Master Toggle

Every optional feature (AI Chat, API Tester, Tests and Connectivity, Mini Web Server, general Scripts) is gated by two flags: its own toggle **and** the master toggle in **Settings > General**. When either is off, the backend endpoint returns `403`, the sidebar entry disappears, and the Advanced Features tab hides itself entirely — the individual configuration values are preserved for when the feature is re-enabled.

Use the master toggle as a quick way to lock down every optional surface at once (for demos, shared machines, or reduced attack surface).

## API Keys

AI API keys are stored in local settings and are sent only from the backend to the configured provider when AI Chat is used.

The public settings endpoint reports only whether a key is configured. It does not return the key to the browser.

## Internal API — LAN Exposure

By default the panel HTTP server binds to `127.0.0.1` (loopback only). Enabling **Allow remote connections** in **Settings > General > Internal API** switches the bind address to `0.0.0.0`, making every advanced-feature endpoint, the internal HomePage, and all instance controls reachable from other devices on the local network.

Before enabling remote access:

- Trust every device that shares the network segment.
- Remember that endpoints like `/api/scripts/:id/run` and `/api/apps/:id/start` can execute arbitrary code on this machine.
- Consider firewalling the panel port when the LAN is not fully trusted.

Changes take effect at next launch.

## Script Runner

The Scripts page runs user code through the host's `python`/`python3`, `node`, or `rustc` interpreters. Anyone who can reach the `/api/scripts/*` endpoints (locally by default, LAN if remote access is enabled, and only when both the master toggle and `scriptsEnabled` are on) can execute arbitrary code on this machine.

Do not enable the Scripts feature on machines you do not fully control, and do not enable it together with remote access on an untrusted LAN.

Script sources persist in `scripts.json`. Executions write to `instances/.scripts-tmp/` and are removed after the run.

## Internal Instances Folder

The `POST /api/internal-folder/mkdir` and `DELETE /api/internal-folder/entry` endpoints refuse any path that resolves outside `./instances/`. Names are sanitized before use (slashes collapse to `-`, other unsafe characters become `_`, hard cap at 80 characters).

Instances with `useInternalFolder: true` run from a subfolder inside `./instances/` regardless of what `cwd` says, which limits how far into the user's filesystem an imported instance can reach.

## Mini Web Server

The mini web server exposes the folder chosen in its page over HTTP on a configurable port bound to `127.0.0.1`. The folder is served as-is:

- Do not point it at directories with sensitive files, credentials, or SSH keys.
- The server refuses to bind on the panel's own port.
- Stopping the mini server releases the port immediately.

## HomePage Template

The internal HomePage can be replaced by uploading an HTML file. The uploaded page is stored locally as `homepage.html` and served exactly as provided, **without sanitization**.

Only upload templates you trust. Treat the uploaded HTML as code that runs in the browser when the HomePage is opened.

## System Logs and Alert Center

System logs are local records. Exported logs can include instance names, command-related messages, and error details. The internal HomePage also lists instance names and commands. The Alert Center mirrors every `error`-type system log into an in-memory alert list.

Review exported files before sharing them.

## Portable Builds

The portable executables use local files next to the launcher — `APPDashboard.exe` (Windows), `application-dashboard` (Linux), or the `.app` bundle (macOS) — including user data and cache directories. Keep the full extracted folder together.
