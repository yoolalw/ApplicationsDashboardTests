# User Guide

This guide explains the visible parts of Applications Dashboard and the main workflows available to users.

## Top Bar

The top bar (left to right) holds the app title, the language selector, the notification **bell**, and the **New App** button.

- **Language selector**: the default language is English; the selected language is stored locally and restored on next launch. Supported: English, Portuguese, Chinese, German, Spanish, Japanese.
- **Bell**: opens the [Alert Center](#alert-center). A red badge shows the number of unread alerts, polled every ~6 seconds. The bell only appears when the Alert Center feature is enabled.
- **New App**: opens the instance form as a side panel.

![Language selector](images/language-selector.png)

## Dashboard

![Dashboard overview](images/dashboard-overview.png)

The dashboard is the main page. Each configured instance appears as a card or as a list row, depending on the layout selected in **Settings > Style**.

Each instance shows:

- Instance name.
- Current status (running / stopped / failed).
- Open link action, shown **only** when the instance has a detected port or a configured web link. Instances without either (for example a `ping` command) do not show this action.
- Start or stop action.
- Edit action.

Clicking an instance selects it and opens the terminal/log panel beside the list when logs are available.

### Layout Modes

The presentation can be switched in **Settings > Style > Instance presentation**:

- **Cards**: large cards with clear status space (default).
- **List**: a compact row layout for monitoring many instances at once.

![Dashboard list layout](images/dashboard-list.png)

### Terminal Panel (three-dot menu)

When the terminal/log panel is open, its **⋯** button reveals actions for that instance:

- **Detach to floating window** — opens the same log view in a compact popup window (`?floating=<instance-id>`) so it can be watched independently of the main dashboard.
- **Open in system terminal** — launches the instance's command in a new terminal window using `cmd /k` on Windows, Terminal.app via `osascript` on macOS, or `x-terminal-emulator`/`gnome-terminal`/`xterm` on Linux. Working directory and command line come from the instance configuration.
- **Restart terminal** — stops the running process (if any) and starts it again from scratch.

## Creating or Editing an Instance

![Application form](images/app-form.png)

Use **New App** to create an instance. Use the gear icon on a card or the edit action in Settings to edit one.

Basic settings include:

- Name.
- Command or executable.
- Arguments.
- Port.
- Working directory.
- **Web link** (optional): a custom URL opened by the instance link action. When empty, the link falls back to the detected local port.
- **Store inside internal folder** (optional): when enabled, the instance runs from a sanitized subfolder of the panel's managed folder, ignoring the free-text Directory input.
- **Auto-start when panel launches**: instances flagged here launch automatically with the panel, in dependency order.
- Dependencies.
- Shell execution mode.

Advanced settings include:

- Alternative ports.
- Secondary directory.
- Advanced command and arguments.
- Advanced shell mode.

Advanced settings must be enabled during creation. They are locked after the instance is created to preserve stability. When editing an instance that was created without advanced mode, the advanced section is hidden entirely, since it cannot be changed.

## Sidebar

The sidebar shows shortcuts to the main pages. Advanced-feature entries only appear when their individual toggle **and** the Advanced Features master toggle are on.

- **Home**: returns to the service dashboard.
- **HomePage**: opens the HomePage in the user's browser. Depending on the General settings, this is either the internal page served by the application or a custom URL.
- **AI Chat** *(advanced)*: opens the local AI chat page.
- **API Tester** *(advanced)*: sends configurable HTTP requests and inspects the response.
- **Tests and Connectivity** *(advanced)*: probes a device or service by IP and port using TCP, HTTP, HTTPS, or ping.
- **Mini Web Server** *(advanced)*: publishes any local folder as a static site on a chosen port.
- **Scripts** *(advanced)*: general Python / JavaScript / Rust script runner.
- **Patch Files**: shows version notes and the project patch summary.
- **Settings**: opens system and instance settings.
- **About system**: shows project information and GitHub links.

## Settings

### Enable / Disable Apps

Lists every configured instance. From this tab users can enable/disable, edit, and remove instances. Disabled instances do not appear on the main dashboard.

### System Logs

![System logs](images/settings-logs.png)

The System logs tab records dashboard events: instance creation, updates, start/stop, imports, backups, and errors. Logs are always stored in English so exports stay consistent across interface languages.

Export formats: **CSV, TXT, JSON, NDJSON, LOG**. The export dialog can filter by instance, limit records, choose a format, and clear exported logs after download.

### General

![Settings general tab](images/settings-general.png)

The General tab is divided into categories:

- **HomePage**: chooses how the HomePage sidebar button behaves.
  - **Internal server**: opens the page served by the application itself, without an external Apache server.
  - **Custom URL**: opens an address typed by the user (the URL field is enabled only in this mode).
  - **Template page** (internal mode only): shows whether the default template or an uploaded page is in use, and provides actions to **Upload** a custom HTML page, **Preview** the current page, and **Reset to default**.
- **Advanced Features**: a **master toggle**. When off, every advanced feature page and toggle disappears (the Advanced Features tab itself is hidden), and the backend endpoints for those features return 403. Individual settings are preserved and come back untouched when the master is turned on again.
- **Internal API**: choose the panel's HTTP port and whether to accept LAN connections (`0.0.0.0`) or stay on localhost only (`127.0.0.1`). Changes take effect at next launch.
- **Internal instances folder**: shows the managed folder path, lets you create/delete subfolders, and explains that instances with "Store inside internal folder" enabled run from a subfolder here.
- **Auto-start**: the **Select instances** button opens a popup where you check which instances should launch with the panel; the list of current auto-start instances is shown as chips below the button.
- **Instance settings**: JSON import and backup download.
- **System overview**: total, visible, and disabled instances.

API keys are saved only in local settings and are not sent to the browser.

The internal HomePage explains how the dashboard works and lists the configured instances with their live status, following the selected layout, theme, and accent color. An uploaded template replaces it entirely and is served exactly as provided.

![Internal HomePage](images/internal-homepage.png)

Saving from any tab persists every program setting together.

### Style

![Style settings](images/settings-style.png)

The Style tab controls:

- Instance presentation: card or list layout.
- Light or dark theme.
- Accent color presets.
- Custom accent color as a six-character hexadecimal code.

When a custom color is too light, the app adjusts button text contrast for readability.

### Advanced Features

Individual toggles for each advanced tool: AI Chat, API Tester, Tests and Connectivity, Mini Web Server, general Scripts, and the Alert Center. Each toggle controls whether its sidebar entry appears and whether its backend endpoints accept requests. Toggle values are always preserved even when the master toggle in General is off.

AI Chat's provider, model, base URL, and API key sit next to its toggle, hidden when AI Chat is off.

**The whole Advanced Features tab disappears when the master toggle is off.**

## Advanced Features

Every page below is only reachable when both the master toggle and its individual toggle are enabled.

### AI Chat

![AI chat](images/ai-chat.png)

AI Chat is a simple chat page that uses the provider configured in the Advanced Features tab.

Supported provider modes: **OpenAI, Google Gemini, Anthropic, OpenAI-compatible API**.

The server limits the conversation context sent to the provider to reduce unnecessary token usage.

### API Tester

Sends configurable HTTP requests (any method, custom headers, optional body) to any URL and shows the response status, elapsed time, headers, and body (auto-formatted for JSON). Useful for probing local APIs without leaving the panel.

### Tests and Connectivity

Verifies whether a device or service is reachable from this machine. Choose an **IP or host**, a **port**, and a **protocol**:

- **TCP** — attempts a TCP handshake to `host:port`.
- **HTTP / HTTPS** — sends a HEAD request.
- **PING** — runs the system `ping` command (`-n` on Windows, `-c` on Linux/macOS); port not needed.

Results include reachability, elapsed time, protocol details, and the raw output. A small history strip keeps the last runs handy.

### Mini Web Server

Publishes any local folder as a static site on a configurable port using an isolated Express instance. Pick a **root folder** and a **port**, then Start. The status card shows the URL, port, folder, and start time. **Open in browser** launches the exposed URL. The folder is public on the chosen port — don't point it at directories with sensitive files.

### Scripts

General script runner for **Python**, **JavaScript**, and **Rust**. Save named snippets, edit them in a dark editor, and hit **Run** to see stdout, stderr, exit code, and elapsed time. Scripts persist to `scripts.json`; each run writes to an ephemeral file inside `instances/.scripts-tmp/` that is deleted after execution.

Requires the corresponding runtime installed on the host: `python`/`python3`, `node`, or `rustc`.

### Alert Center

Opens from the bell in the top bar. Lists in-memory alerts with severity (info / warning / error), source, timestamp, and message. Actions:

- **Mark read** (per alert) — clears the badge for that entry.
- **Mark all read** — clears the badge for everything.
- **Clear all** — removes every alert from the store.

Every `error`-type system log automatically raises an alert, and script failures raise a `warning`.

## Patch Files

![Patch files](images/patch-files.png)

Patch Files contains:

- Release notes from `patch-notes.json`.
- Project patch summary from `PROJECT_PATCH_SUMMARY.md`.

## About System

![About system](images/about-system.png)

The About page includes:

- Main project description.
- Local control summary.
- Instance management summary.
- Patch history summary.
- GitHub profile link.
- Repository link.
- Created by Victor Samuel / Victor-477.
