# Testing

Validation flow used for Applications Dashboard.

## Automated Checks

Run TypeScript validation:

```bash
npm run lint
```

Run a production build:

```bash
npm run build
```

Run the i18n smoke test (opens Electron and validates visible text for the six supported languages):

```bash
npx electron scripts\verify-i18n.cjs
```

Regenerate documentation screenshots (only when the UI changed):

```bash
npx electron scripts\capture-readme-screenshots.cjs
```

## API Smoke Test

After `npm run build`, start the compiled server:

```bash
npm run start
```

### Core endpoints

| URL | Expected |
| --- | --- |
| `http://127.0.0.1:3000/api/apps` | Visible enabled instances. |
| `http://127.0.0.1:3000/api/apps/all` | All instances (including disabled). |
| `http://127.0.0.1:3000/api/settings` | Public settings; API key never exposed. Includes `advancedFeaturesEnabled`, `aiChatEnabled`, `apiTesterEnabled`, `connectivityTesterEnabled`, `webServerEnabled`, `scriptsEnabled`, `alertsEnabled`, `internalApiPort`, `internalApiRemoteAccess`, and every other program setting. |
| `http://127.0.0.1:3000/api/patch-notes` | Current version, notes, patch summary. |
| `http://127.0.0.1:3000/api/system-logs` | System log entries. |
| `http://127.0.0.1:3000/api/homepage-template` | `{ "custom": false }` until a template is uploaded. |
| `http://127.0.0.1:3000/internal-homepage` | Generated HomePage HTML, or the uploaded template when one is present. |

### Advanced-feature endpoints (all return **403** when either the master toggle or the individual toggle is off)

| URL | Method | Purpose |
| --- | --- | --- |
| `/api/ai-chat` | `POST` | AI chat conversation turn. |
| `/api/api-tester` | `POST` | HTTP request proxy for the API Tester page. |
| `/api/connectivity-test` | `POST` | TCP / HTTP(S) / ping probe. |
| `/api/web-server/status` | `GET` | Mini web server state. |
| `/api/web-server/start` | `POST` | Start the mini web server on a folder/port. |
| `/api/web-server/stop` | `POST` | Stop the mini web server. |
| `/api/scripts` | `GET/POST` | List / create scripts. |
| `/api/scripts/:id` | `PUT/DELETE` | Update / remove a script. |
| `/api/scripts/:id/run` | `POST` | Execute a script and return `{stdout, stderr, exitCode, elapsedMs, ok}`. |

### Alert center

| URL | Method | Purpose |
| --- | --- | --- |
| `/api/alerts` | `GET` | Alerts + unread count. Returns `{alerts:[], unread:0}` when the feature flag is off. |
| `/api/alerts/:id/read` | `POST` | Mark one alert read. |
| `/api/alerts/read-all` | `POST` | Mark all read. |
| `/api/alerts/clear` | `POST` | Empty the store. |

### Internal instances folder

| URL | Method | Purpose |
| --- | --- | --- |
| `/api/internal-folder` | `GET` | Path and entries listing. |
| `/api/internal-folder/mkdir` | `POST` | Create a sanitized subfolder (rejects path traversal). |
| `/api/internal-folder/entry?name=X` | `DELETE` | Delete a subfolder/file (rejects path traversal and the root itself). |

### Instance actions

| URL | Method | Purpose |
| --- | --- | --- |
| `/api/apps/:id/start` | `POST` | Start (respects `dependsOn`). |
| `/api/apps/:id/stop` | `POST` | Stop. |
| `/api/apps/:id/open-terminal` | `POST` | Launch the command in the OS's default terminal (cross-platform). |
| `/api/apps/:id/enabled` | `PUT` | Toggle instance enablement. |
| `/api/apps/auto-start` | `PUT` | Bulk-set `autoStart` from `{ ids: string[] }`. |

## Manual UI Checklist

### Top bar

- Language selector switches all UI text.
- Bell icon appears next to the language selector when Alert Center is enabled, with a red unread badge that updates every few seconds.
- **New App** opens the create form.

### Dashboard

- Cards render correctly.
- List layout renders correctly when selected in Style settings.
- Start / stop buttons do not resize the card.
- Selecting an instance opens the terminal/log area.
- Disabled apps do not appear on the dashboard.
- The link action is hidden for instances without a port or web link.

### Terminal panel

- The **⋯** menu opens on click and closes on outside click.
- **Detach** opens a floating popup window with only the log for that instance (`?floating=<id>` URL).
- **Open in system terminal** launches a new OS terminal (cmd on Windows, Terminal on macOS, x-terminal-emulator/gnome-terminal/xterm on Linux) with the instance's command in the resolved `cwd`.
- **Restart** stops the running process (if any) and starts it again.

### Instance form

- Basic fields save correctly.
- The optional web link saves and is used by the link action.
- Enabling **Store inside internal folder** disables the Directory input and reveals the subfolder-name field.
- **Auto-start when panel launches** persists and drives the boot-time launcher.
- Advanced mode is available during creation.
- Advanced mode is locked after creation.
- The advanced section is hidden when editing an instance created without advanced mode.

### HomePage

- Internal mode opens the generated HomePage and lists instances with status.
- The internal HomePage follows the selected layout, theme, and accent color.
- Uploading a custom template replaces the page; resetting restores the default.
- Custom mode opens the configured URL and enables the URL field.

### Settings — Enable / Disable Apps

- Enabling/disabling instances updates the dashboard visibility.
- Edit works from Settings.
- Delete is available only in Settings.

### Settings — System logs

- Logs export in CSV, TXT, JSON, NDJSON, and LOG.
- Optional log cleanup works after export.

### Settings — General

- HomePage mode switches between internal and custom; the URL field is disabled in internal mode.
- Template page upload/preview/reset works.
- Advanced Features master toggle hides every advanced sidebar entry and its content when off, and the **Advanced Features tab disappears** entirely.
- Internal API port + Allow remote connections persist; hint reminds the user changes apply at next launch.
- Internal instances folder: create/delete subfolders works; the entries list refreshes; path-traversal names are rejected.
- Auto-start selector popup lists all instances with checkboxes; saving persists via `PUT /api/apps/auto-start`; the chip list below the button updates.
- Instance import accepts valid payloads and rejects invalid ones.
- Backup downloads the current instance list.

### Settings — Style

- Card and list layout selection applies to the dashboard.
- Light and dark themes apply.
- Accent color presets apply.
- Custom six-character hex color applies.
- Button text remains readable with light custom colors.
- Saving from Style also persists General tab changes.

### Settings — Advanced Features (only visible when the master toggle is on)

- Toggles for AI Chat, API Tester, Tests and Connectivity, Mini Web Server, Scripts, Alert Center — each hides/shows its sidebar entry independently.
- AI Chat settings (provider/model/URL/API key) appear only when AI Chat is on.
- Turning the master off in General bounces the user back to the General tab and hides the Advanced tab.

### Localization

- Language selection persists after reload.
- English remains the default.
- All six languages appear in the selector.
- Patch Files text follows the selected language when translations exist.

### Advanced feature pages

- **AI Chat** — not-configured state is shown when no API key is set; chat requests go through the backend only; conversation context stays bounded.
- **API Tester** — request builder sends and shows status, elapsed time, headers, and body (JSON auto-formatted); custom headers add/remove works.
- **Tests and Connectivity** — TCP handshake reports success/ECONNREFUSED; HTTP/HTTPS shows status; PING shows the raw output; port field disabled for PING; history strip populates.
- **Mini Web Server** — starting serves the folder on the chosen port; stopping releases it; refuses to bind on the panel port; refuses non-existent folders.
- **Scripts** — creates/saves/deletes; runs Python/JavaScript/Rust and shows stdout, stderr, exit code, elapsed time; failures raise a warning alert.
- **Alert Center** — errors from system logs raise entries; unread badge tracks unread count; mark-read / mark-all-read / clear-all work.

### Patch Files

- Version notes render.
- Project patch summary renders.

### About

- Project description appears.
- GitHub profile link works.
- Repository link works.

## Portable Executable Test

After packaging, the portable build is smoke-tested by launching it and checking the internal server:

```text
release/APPDashboard/APPDashboard.exe
http://127.0.0.1:3764/internal-homepage
http://127.0.0.1:3764/api/settings
```

The executable should also carry the embedded application icon and report the correct version in its file properties.

## Cross-Platform Package Test

```bash
# Windows portable + Linux tar.gz in one shot (from a Windows host):
npm run package

# Linux tar.gz alone (any host):
npm run package:linux

# macOS .app (macOS host only):
npm run package:mac
```

Inspect Linux tarball contents:

```bash
tar -tzf dist/APPDashboard-linux-x64.tar.gz | head
```

Expected to include `application-dashboard` (ELF binary), `chrome-sandbox`, `resources/`, and the `locales/` pack.

## 3.0.0 Validation Performed

```bash
npm run lint
npm run build
npx electron scripts\verify-i18n.cjs
npm run package:win:full
npm run package:linux
```

Covered TypeScript checks, the production build, the i18n smoke test for all six languages, the Windows portable executable (with embedded icon and internal-server smoke test), and the Linux tar.gz build produced from the same Windows host. macOS builds run on `macos-latest` via `.github/workflows/release.yml`.
