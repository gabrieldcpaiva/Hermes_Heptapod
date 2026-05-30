---
name: hermes-dashboard
description: "Manage the Hermes Agent web dashboard: launch, check status, stop, configure, and use embedded TUI."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
tags: [hermes, dashboard, web-ui, configuration]
---

# Hermes Dashboard Skill

## Purpose
Manage the Hermes Agent web dashboard: launch, check status, stop, configure, and use embedded TUI.

## When to Use
You want to interact with the Hermes web UI for configuration, API key management, session browsing, or to run the embedded terminal UI (TUI) in a browser.

## Prerequisites
- Hermes Agent installed and available in PATH (`hermes` command).
- For embedded TUI (`--tui`), ensure `fastapi` and `uvicorn` are installed (they are installed by default when installing Hermes with dashboard extras).

## Steps

### 1. Launch the Dashboard
```bash
hermes dashboard
```
- Defaults to `http://127.0.0.1:9119`.
- Automatically opens in your default browser unless `--no-open` is used.

### 2. Check if Dashboard is Running
```bash
hermes dashboard --status
```
Lists any running dashboard processes with their PIDs.

### 3. Stop the Dashboard
```bash
hermes dashboard --stop
```
Stops all running dashboard processes.

### 4. Change Host or Port
- To use a custom port: `hermes dashboard --port <port>`
- To bind to all interfaces (use with caution, exposes API keys): `hermes dashboard --host 0.0.0.0 --insecure`
- To prevent auto‑open: add `--no-open`.

### 5. Enable Embedded TUI (Chat Tab)
```bash
hermes dashboard --tui
```
This enables the in‑browser Chat tab that runs `hermes --tui` via a PTY/WebSocket bridge.
Alternatively, set the environment variable `HERMES_DASHBOARD_TUI=1`.

### 6. Skip Build (for CI or environments without npm)
If you have a pre‑built `web_dist` directory, skip the build step:
```bash
hermes dashboard --skip-build
```
Pre‑build with: `cd web && npm run build`.

### 7. Troubleshooting
- **Dashboard fails to start**: Check logs at `~/.hermes/logs/gateway.log` and `~/.hermes/logs/gateway.error.log`.
- **Port already in use**: Kill the existing process (`kill <PID>`) or choose another port.
- **Blank screen / authentication loop**: Ensure you are accessing `http://127.0.0.1:<port>`; the dashboard blocks non‑loopback hosts unless `--insecure` is used.
- **Embedded TUI not showing**: Verify `--tui` flag is set and that the browser console shows no WebSocket connection errors.

## Configuration Notes
- The dashboard respects `~/.hermes/config.yaml` and `~/.hermes/.env`.
- Changes to config or environment variables require a dashboard restart to take effect.
- Dashboard theme can be changed via `hermes config set dashboard.theme <theme>` (options: default, midnight, ember, mono, cyberpunk, rose).

## Related Commands
- `hermes gateway status` – shows the gateway service that underlies the dashboard.
- `hermes tools` – ensure `web` toolset is enabled if you plan to use dashboard features that rely on web search (though the dashboard itself does not require it).

## Pitfalls
- Binding to `0.0.0.0` without `--insecure` will fail; the dashboard refuses to start on non‑loopback interfaces unless explicitly allowed.
- Forgetting `--tui` will leave the Chat tab disabled; the dashboard will show a placeholder message.
- Using `--skip-build` when no `dist` folder exists results in 404s for static assets.

## Verification
After launching, visit the URL shown in the terminal output. You should see the Hermes dashboard homepage with navigation for Config, API Keys, Sessions, and (if `--tui` enabled) Chat.

---
*This skill is intended for repeated use across sessions. Keep it updated with new dashboard features or changes in CLI flags.*