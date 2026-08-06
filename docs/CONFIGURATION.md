# Configuration

Applications Dashboard stores local instance configuration in `apps.json` and program preferences in `settings.json`.

Runtime-only files ignored by Git: `settings.json` (program preferences and API key), `homepage.html` (uploaded custom HomePage template), `scripts.json` (saved user scripts), and everything under `instances/` (the internal instances folder).

## Instance Configuration

Instances can be edited through the UI or manually in `apps.json`.

Example:

```json
[
  {
    "id": "backend-local",
    "name": "Backend API",
    "command": "npm",
    "args": "run dev",
    "port": "3000",
    "cwd": "../backend",
    "webLink": "",
    "useInternalFolder": false,
    "internalFolder": "",
    "autoStart": false,
    "dependsOn": [],
    "shell": true,
    "enabled": true,
    "advancedEnabled": false
  }
]
```

## Basic Fields

| Field | Required | Description |
| --- | --- | --- |
| `id` | Yes | Unique internal identifier. Also used by dependencies. |
| `name` | Yes | Name shown on cards and lists. |
| `command` | Yes | Executable or base command. |
| `args` | No | Arguments passed to the command. |
| `port` | No | Port used for status detection and duplicate prevention. |
| `cwd` | No | Working directory. Empty means the dashboard folder. Ignored when `useInternalFolder` is true. |
| `webLink` | No | Custom URL opened by the instance link action. When empty, the link falls back to `http://127.0.0.1:<port>`. With neither a web link nor a port, no link action is shown. |
| `useInternalFolder` | No | When `true`, the instance runs from a sanitized subfolder inside the panel's internal instances folder (`./instances/<internalFolder>`). |
| `internalFolder` | No | Name of the subfolder inside the internal folder. Defaults to the instance `id` when empty. Non-alphanumeric characters other than `._-` are replaced with `_`; slashes collapse to `-`; hard-capped at 80 chars. |
| `autoStart` | No | When `true`, the panel launches this instance automatically at boot, in dependency order. |
| `dependsOn` | No | Array of instance IDs that should start first. |
| `shell` | No | `true` runs through the platform shell. `false` runs the executable directly. |
| `enabled` | No | `false` hides the instance from the main dashboard. |

## Advanced Fields

Advanced fields are active only when `advancedEnabled` is `true`.

| Field | Description |
| --- | --- |
| `advancedEnabled` | Enables advanced execution fields. Chosen at creation and locked afterwards. |
| `alternatePorts` | Alternative ports checked when the primary port is unavailable. |
| `secondaryCwd` | Optional second working directory for advanced execution flows. When `useInternalFolder` is on, the secondary command runs from the internal subfolder too. |
| `advancedCommand` | Optional advanced command. |
| `advancedArgs` | Arguments for the advanced command. |
| `advancedShell` | Shell mode for the advanced command. |

## Working Directories

`cwd` accepts absolute and relative paths.

Absolute example:

```json
"cwd": "C:\\Projects\\backend"
```

Relative example:

```json
"cwd": "../backend"
```

If a relative path does not exist from the dashboard folder, the backend tries to resolve it from a nearby project root containing known project folders.

### Internal Instances Folder

When `useInternalFolder: true`, the instance ignores `cwd` and runs from a subfolder inside `./instances/`. The subfolder name comes from `internalFolder` (or the instance `id` when empty). The panel:

- Creates the subfolder on first start if it does not exist.
- Sanitizes the folder name: `/` and `\` become `-`, other unsafe characters become `_`, and the value is capped at 80 characters.
- Refuses path traversal attempts through `POST /api/internal-folder/mkdir` and `DELETE /api/internal-folder/entry`.

Manage the folder from **Settings > General > Internal instances folder**.

## Dependencies

Use `dependsOn` when one service must start before another.

```json
{
  "id": "frontend",
  "name": "Frontend",
  "command": "npm",
  "args": "run dev",
  "port": "5173",
  "cwd": "../frontend",
  "dependsOn": ["backend"],
  "shell": true
}
```

Starting `frontend` attempts to start `backend` first. The same order applies to the auto-start pass at panel boot.

## Auto-Start

Set `autoStart: true` (via the checkbox on the instance form or the popup in **Settings > General > Auto-start**) to have the panel launch the instance at boot. Failures raise an entry in the Alert Center but never block panel startup.

The bulk selector in Settings calls `PUT /api/apps/auto-start` with `{ "ids": [...] }`; every listed id gets `autoStart: true` and every other instance gets `autoStart: false`.

## Port Detection

When `port` is provided, the dashboard checks `127.0.0.1:<port>`.

If the port is open:

- The service can appear as running.
- The dashboard avoids starting a duplicate process.
- Stop actions can try to terminate the process occupying that port on Windows.

## Shell Mode

Use `shell: true` for commands usually run from a terminal:

```json
{
  "command": "npm",
  "args": "run dev",
  "shell": true
}
```

Use `shell: false` for direct executables:

```json
{
  "command": "C:\\Tools\\service.exe",
  "args": "--port 8080",
  "shell": false
}
```

## Importing Instances

Settings > General > Instance settings can import JSON.

Accepted formats:

```json
[
  { "name": "Worker", "command": "npm", "args": "run worker" }
]
```

Or:

```json
{
  "apps": [
    { "name": "Worker", "command": "npm", "args": "run worker" }
  ]
}
```

The import tool validates the payload and supports replacing the current instance list. All instance fields (`webLink`, `useInternalFolder`, `internalFolder`, `autoStart`, advanced fields) are preserved on import.

## Backing Up Instances

Settings > General > Instance settings can export the current instance list as JSON. Backups are useful before replacing all instances, moving to another machine, or preparing a release/demo.

## Program Settings

Program settings live in `settings.json`.

### Presentation and HomePage

| Field | Description |
| --- | --- |
| `themeMode` | `light` or `dark`. |
| `accentColor` | Six-digit hex color with `#`, such as `#009dea`. |
| `dashboardLayout` | `cards` or `list`. |
| `homepageMode` | `internal` serves the app's own HomePage; `custom` opens `homepageUrl`. |
| `homepageUrl` | URL opened when `homepageMode` is `custom`. |

### Internal API (v2.7)

| Field | Description |
| --- | --- |
| `internalApiPort` | Panel HTTP port. `0` uses the launch environment default (3000 dev / 3764 packaged). Values outside 1-65535 collapse to `0`. Takes effect at next launch. |
| `internalApiRemoteAccess` | When `true`, the panel binds to `0.0.0.0` (LAN reachable). Otherwise `127.0.0.1`. |

### Advanced Features (v2.6 - v3.0)

| Field | Description |
| --- | --- |
| `advancedFeaturesEnabled` | Master toggle. When `false`, every advanced feature is hidden and its endpoint returns 403, but individual toggles are preserved. |
| `aiChatEnabled` | AI Chat feature toggle. |
| `apiTesterEnabled` | API Tester feature toggle. |
| `connectivityTesterEnabled` | Tests & Connectivity feature toggle. |
| `webServerEnabled` | Mini web server feature toggle. |
| `webServerPort` | Port the mini web server listens on when started. |
| `webServerRootFolder` | Absolute path currently served by the mini web server. |
| `scriptsEnabled` | Scripts runner feature toggle. |
| `alertsEnabled` | Alert Center feature toggle. Default `true`. |
| `aiProvider` | `openai`, `gemini`, `anthropic`, or `openai-compatible`. |
| `aiModel` | Model name used by AI Chat. |
| `aiBaseUrl` | Custom base URL for OpenAI-compatible providers. |
| `aiApiKey` | Local API key. It is not exposed to the browser. |

## Internal HomePage

When `homepageMode` is `internal`, the HomePage button opens a page served by the application at `/internal-homepage`. By default this is a generated template that explains the dashboard and lists instances with live status, following the selected layout, theme, and accent color.

Uploading a custom page (Settings > General > HomePage > Template page) stores it as `homepage.html` and serves it exactly as provided. Resetting removes that file and restores the default template.

## Scripts Storage

Saved scripts live in `scripts.json` at the panel root, ignored by Git. Each entry:

```json
{
  "id": "uuid",
  "name": "hello",
  "language": "python",
  "source": "print('hello')",
  "updatedAt": "2026-08-05T12:00:00.000Z"
}
```

Supported languages: `python`, `javascript`, `rust`. Each run writes the source to a temp file inside `instances/.scripts-tmp/`, invokes the appropriate runtime (`python`/`python3`, `node`, or `rustc` + the produced binary), and removes the temp file.
