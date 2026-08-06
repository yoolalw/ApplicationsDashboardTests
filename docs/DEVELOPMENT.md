# Development

This document explains how to work on the project locally.

## Requirements

- **Any of**: Windows, Linux, or macOS.
- Node.js 20 or newer.
- npm.
- For the Scripts advanced feature: `python`/`python3`, `node`, and/or `rustc` on the host, matching the languages you plan to run.

## Install

```bash
npm install
```

The `electron` postinstall downloads the Electron runtime binary. If `node_modules/electron/dist/` is missing after install (rare — usually a network issue during postinstall), run `node node_modules/electron/install.js` to force it.

## Run Locally

Development server (Vite middleware + Express):

```bash
npm run dev
```

Desktop app (production build + Electron shell):

```bash
npm run desktop
```

Production server after build:

```bash
npm run build
npm run start
```

## Scripts

| Script | Purpose |
| --- | --- |
| `npm run dev` | Starts the Express/Vite development server. |
| `npm run lint` | Runs TypeScript validation without emitting files. |
| `npm run build` | Builds the React frontend and bundles the Node server into `dist/`. |
| `npm run start` | Runs `dist/server.cjs`. |
| `npm run desktop` | Builds and opens the Electron desktop app. |
| `npm run package` | Unified packager: build + Windows portable/ZIP + Linux tar.gz in one command (see `scripts/package.cjs`). |
| `npm run package:win` | Runs the Windows portable script over an existing `dist/`. |
| `npm run package:win:full` | Build + Windows portable in one step. |
| `npm run package:win:zip` | Build + Windows portable + ZIP. |
| `npm run package:linux` | Build + Linux `tar.gz` via electron-builder (works from any host). |
| `npm run package:mac` | Build + macOS `.app` via electron-builder — **only runs on macOS**. |
| `npm run package:all` | Build + all three targets (macOS host required for the mac step). |
| `npm run clean` | Removes `dist`. |

## Architecture

The application has three major parts:

- **React frontend** in `src/` (Vite + React 19 + Tailwind).
- **Express backend** in `server.ts` with helpers in `server/`.
- **Electron shell** in `electron/main.cjs`.

The Electron app reads `settings.json` before boot to pick up the persisted internal API port and network-access policy, sets environment variables, then starts the local backend and loads the UI from the local server over `127.0.0.1`.

## Backend Modules

| Path | Purpose |
| --- | --- |
| `server.ts` | Route orchestration, process management, scripts runner, alerts, mini web server, connectivity, HomePage rendering. |
| `server/appImport.ts` | Validates and normalizes imported instance JSON. |
| `server/defaultApps.ts` | Default app list used when `apps.json` is missing. |
| `server/fileUtils.ts` | Safe JSON/text file helpers. |
| `server/patchNotes.ts` | Patch notes and project summary parsing. |
| `server/settingsUtils.ts` | Program settings defaults, normalizers, and `isFeatureEffectivelyEnabled(master, individual)` helper. |
| `server/systemLogs.ts` | System log filtering and export serialization. |
| `server/types.ts` | Shared backend types: `AppConfig`, `ProgramSettingsFile`, `Script`, `Alert`, `SystemLogEntry`. |

## Frontend Structure

| Path | Purpose |
| --- | --- |
| `src/App.tsx` | Main shell, navigation, state, floating-window mode, unread-alerts polling. |
| `src/components/AppCard.tsx` | Service card (card layout). |
| `src/components/AppListItem.tsx` | Compact service row (list layout). |
| `src/components/AppForm.tsx` | Instance create/edit panel including auto-start and internal-folder options. |
| `src/components/LogViewer.tsx` | Terminal/log view with the three-dot menu (detach, system terminal, restart). |
| `src/components/SettingsView.tsx` | Settings page and tabs, master toggle, auto-start selector popup. |
| `src/components/settings/` | Smaller Settings dialog components (logs export, instance import). |
| `src/components/AIChatView.tsx` | AI Chat page. |
| `src/components/ApiTesterView.tsx` | API Tester page. |
| `src/components/ConnectivityTesterView.tsx` | Tests and Connectivity page. |
| `src/components/WebServerView.tsx` | Mini web server page. |
| `src/components/ScriptsView.tsx` | Scripts runner page. |
| `src/components/AlertCenterView.tsx` | Alert center page. |
| `src/components/PatchFilesView.tsx` | Patch notes and project summary view. |
| `src/components/AboutView.tsx` | About system page. |
| `src/i18n.ts` | Interface translations and language options. |
| `src/i18n/patchTextTranslations.ts` | Translated Patch Files and patch summary text. |

Secondary views are code-split with `React.lazy` and Suspense so only the pages the user opens are loaded.

## Screenshots

Generate documentation screenshots:

```bash
npm run build
npx electron scripts\capture-readme-screenshots.cjs
```

The script saves images to `docs/images/`, including the dashboard (card and list layouts), the instance form, the settings tabs, the internal HomePage, and the other system pages. It temporarily seeds demo instances only at runtime and does not modify `apps.json`.

## Generated Files

The following folders are generated and ignored:

- `build/`
- `dist/`
- `release/`
- `.cache/`
- `node_modules/`

The following local files are also generated at runtime and ignored:

- `settings.json` (program preferences and API key).
- `homepage.html` (uploaded custom HomePage template).
- `scripts.json` (saved user scripts).
- `instances/` (internal folder for instance files and script temp files).

Do not commit generated folders or local runtime files.

## Electron Dependency

The Windows portable script copies the Electron runtime from `node_modules/electron/dist`, so the Electron binary must be downloaded during `npm install`. The packaging script (`scripts/package-portable.cjs`) fails fast with a clear message if the binary or the production build is missing, retries `removeDir` a few times to tolerate Windows file locks, and normalises pre-1980 timestamps so `Compress-Archive` accepts them.

## Cross-Platform Packaging

`electron-builder` 26 refuses macOS builds from non-macOS hosts. The recommended path for a full three-platform release is the GitHub Actions workflow at [`.github/workflows/release.yml`](../.github/workflows/release.yml), which runs each target on `windows-latest`, `ubuntu-latest`, and `macos-latest`.

From a single Windows host you can still produce both **Windows portable** and **Linux tar.gz** (`npm run package` does both). AppImage packaging fails on Windows because it needs POSIX symlinks — that's why the Linux target defaults to `tar.gz`.
