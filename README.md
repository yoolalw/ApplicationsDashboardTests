# Applications Dashboard

Applications Dashboard is a cross-platform desktop control panel for running local applications, services, scripts, and terminal commands from one interface. It packages for **Windows**, **Linux**, and **macOS**.

Current documented version: **3.0.0**.

The project is designed for development and operation environments where databases, APIs, frontends, Node-RED flows, worker processes, and support tools need to be started, monitored, stopped, and documented with less friction.

## What It Does

- Registers local applications as reusable service cards.
- Starts and stops commands from the dashboard, with an auto-start selector for launch-time instances.
- Shows process status and live terminal logs, with a three-dot menu to detach into a floating window, open in the system terminal, or restart the terminal.
- Switches the dashboard between a card layout and a compact list layout.
- Opens each instance through its detected port or an optional custom web link.
- Supports dependencies between instances.
- Stores instance files inside a managed internal folder so the panel does not touch arbitrary user directories when the user does not need it to.
- Allows instance import/export through JSON backups.
- Keeps system logs with CSV, TXT, JSON, NDJSON, and LOG export formats.
- Surfaces errors in a central **Alert Center** with severity, source, timestamp, and mark-as-read.
- Serves an internal HomePage from the application itself, with no external Apache, and lets you replace it with an uploaded template or a custom URL.
- Ships **advanced features** that can be enabled per-feature and gated by a master toggle: AI Chat, API Tester, Tests & Connectivity probe, Mini Web Server, and general Scripts runner (Python / JavaScript / Rust).
- Lets the user choose the panel's HTTP port and whether LAN clients can reach it.
- Provides Settings, HomePage, Patch Files, About, and the enabled advanced-feature pages via a sidebar.
- Supports English as the primary language, plus Portuguese, Chinese, German, Spanish, and Japanese.
- Packages as a portable Windows executable, a Linux `tar.gz`, or a macOS `.app` bundle (macOS build requires a macOS host — an electron-builder policy).

## Screenshots

### Dashboard (cards)

![Dashboard overview](docs/images/dashboard-overview.png)

### Dashboard (list)

![Dashboard list layout](docs/images/dashboard-list.png)

### Internal HomePage

![Internal HomePage](docs/images/internal-homepage.png)

### Instance Form

![Application form](docs/images/app-form.png)

### Language Selector

![Language selector](docs/images/language-selector.png)

### Settings

![Settings general tab](docs/images/settings-general.png)

### Patch Files

![Patch files](docs/images/patch-files.png)

More screenshots and page tours are available in [docs/USER_GUIDE.md](docs/USER_GUIDE.md).

## Documentation

| Document | Purpose |
| --- | --- |
| [User Guide](docs/USER_GUIDE.md) | Every page and user-facing workflow, including advanced features. |
| [Configuration](docs/CONFIGURATION.md) | `apps.json`, instance fields, advanced options, program settings, JSON import/export. |
| [Localization](docs/LOCALIZATION.md) | Language system and how translations are maintained. |
| [Development](docs/DEVELOPMENT.md) | Project structure, scripts, backend/frontend modules, screenshots. |
| [Testing](docs/TESTING.md) | Validation commands, endpoint smoke tests, manual QA flows. |
| [Release Guide](docs/RELEASE.md) | Windows / Linux / macOS packaging and GitHub release publishing. |
| [Security](docs/SECURITY.md) | Local-command, API key, script runner, LAN exposure, and configuration safety notes. |
| [Roadmap](ROADMAP.md) | Version-by-version summary from 2.7 through 3.0. |

## For End Users

Download the platform-specific release from GitHub Releases and extract it:

- **Windows**: `APPDashboard-windows-portable.zip` → run `APPDashboard.exe` inside the extracted folder. Do not run the `.exe` outside its folder — the portable build needs the Electron support files beside it.
- **Linux**: `APPDashboard-linux-x64.tar.gz` → extract and run `./application-dashboard` from inside the folder.
- **macOS**: extract the `.app` and drag it to `Applications`. First launch: right-click → **Open** to accept the unsigned bundle.

Node.js is not required to use a published release.

## For Developers

Install dependencies:

```bash
npm install
```

Validate the code:

```bash
npm run lint
npm run build
```

Run the local server:

```bash
npm run dev
```

Open the desktop app:

```bash
npm run desktop
```

Package the application:

```bash
# Windows portable + ZIP (Windows host)
npm run package:win:zip

# Linux tar.gz (any host)
npm run package:linux

# macOS .app (macOS host only, per electron-builder policy)
npm run package:mac

# Unified Windows portable + Linux tar.gz in one command
npm run package
```

For a cross-platform release via CI, use the workflow in [`.github/workflows/release.yml`](.github/workflows/release.yml).

## Project Structure

```text
.
|-- .github/workflows/     # Cross-platform release workflow (win + linux + mac)
|-- docs/                  # User, developer, release, testing, security, localization docs
|-- electron/              # Electron desktop entry point (main.cjs)
|-- instances/             # (runtime) internal folder for instance files; gitignored
|-- public/                # Static assets copied into the build
|-- scripts/               # Packaging, screenshot, and i18n scripts
|-- server/                # Backend helper modules
|-- src/                   # React frontend
|-- abrir-painel.cmd       # Windows launcher
|-- abrir-painel.sh        # POSIX launcher (Linux/macOS)
|-- apps.json              # Local instance configuration
|-- patch-notes.json       # Version history rendered in the app
|-- PROJECT_PATCH_SUMMARY.md
|-- ROADMAP.md
|-- server.ts              # Express API and local process orchestration
`-- package.json
```

Runtime-generated files kept out of Git: `settings.json` (program preferences and API key), `homepage.html` (uploaded custom HomePage), `scripts.json` (saved user scripts), and everything under `instances/`.

## Latest Validation

The 3.0.0 release was validated with:

```bash
npm run lint
npm run build
npx electron scripts\verify-i18n.cjs
npx electron scripts\capture-readme-screenshots.cjs
npm run package:win:full       # Windows portable, on this Windows host
npm run package:linux          # Linux tar.gz, from the same Windows host
```

macOS builds run on macOS runners via the CI workflow in `.github/workflows/release.yml`. `electron-builder` 26 refuses macOS builds from non-macOS hosts.
