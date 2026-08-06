# Release Guide

This guide is for maintainers publishing Applications Dashboard on GitHub Releases.

## 1. Prepare

Install dependencies:

```bash
npm install
```

Confirm the version in:

- `package.json`
- `package-lock.json`
- `patch-notes.json`
- `PROJECT_PATCH_SUMMARY.md`
- App footer and Settings version display

## 2. Validate

Run:

```bash
npm run lint
npm run build
npx electron scripts\verify-i18n.cjs
```

If UI documentation changed, regenerate screenshots:

```bash
npx electron scripts\capture-readme-screenshots.cjs
```

## 3. Package

### Windows (portable)

Generate the portable build and ZIP:

```bash
npm run package:win:zip
```

Output folder: `release/APPDashboard/` (with `APPDashboard.exe` inside).
ZIP file: `release/APPDashboard-windows-portable.zip`.

### Linux (tar.gz)

From any host (Windows, Linux, macOS):

```bash
npm run package:linux
```

Output file: `dist/APPDashboard-linux-x64.tar.gz` (~120 MB). Extract and run `application-dashboard` from inside the folder. On Windows hosts the target is `tar.gz` because `AppImage` needs POSIX symlinks; if you package on Linux itself, `AppImage` also works.

### macOS (dir → .app)

`electron-builder` 26 refuses macOS builds from Windows or Linux hosts. You must package on a **macOS** machine or a macOS GitHub Actions runner:

```bash
npm install
npm run package:mac
```

Output folder: `dist/mac/Applications Dashboard.app`. The app is unsigned (`identity: null`); users can right-click → Open on first launch to bypass Gatekeeper, or you can sign it locally.

### All three at once (from a macOS host)

```bash
npm run package:all
```

### One-shot Windows + Linux from the same host

```bash
npm run package
```

Runs the build once, then produces the Windows portable + ZIP and the Linux `tar.gz` in a single command (macOS still needs its own runner).

### GitHub Actions

`.github/workflows/release.yml` runs one job per OS (`windows-latest`, `ubuntu-latest`, `macos-latest`), each calling `npm ci` and its respective `package:*` script, and uploads the artifacts. Trigger it manually from the Actions tab, passing the tag as input.

## 4. Test the Packaged Apps

### Windows

Open `release/APPDashboard/APPDashboard.exe` and check:

- Window opens.
- Application icon is correct. The packaging script embeds it from `public/ind40-logo.png`; the build also requires the Electron binary in `node_modules/electron/dist`.
- Dashboard loads.
- Local API responds at `http://127.0.0.1:3764/api/apps`.
- Patch notes report the expected version.
- Settings opens, language selector works, a test instance starts and stops.

### Linux

Extract the tarball and run:

```bash
tar -xzf dist/APPDashboard-linux-x64.tar.gz
cd APPDashboard-linux-x64
./application-dashboard
```

### macOS

Open `dist/mac/Applications Dashboard.app`. Right-click → **Open** on the first launch to accept the unsigned bundle.

## 5. Publish on GitHub

1. Open **Releases**.
2. Draft a new release.
3. Create a tag such as `v3.0.0`.
4. Attach every platform artifact: `APPDashboard-windows-portable.zip`, `APPDashboard-linux-x64.tar.gz`, and the macOS `.app` (or a zipped copy).
5. Add a short summary from `patch-notes.json`.

Suggested release text:

```text
Download the archive for your platform and extract it. On Windows, run APPDashboard.exe inside the extracted folder. On Linux, run ./application-dashboard. On macOS, drag the .app to Applications; right-click → Open on first launch.

Node.js and the source code are not required to use this release version.
```

## Important

Do not publish only the Windows `.exe`. Electron needs the support files in the portable folder.

Do not commit generated folders:

- `build/`
- `dist/`
- `release/`
- `.cache/`
