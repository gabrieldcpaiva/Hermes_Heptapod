# Gateway Recovery & Headless Dashboard Pitfalls

## 1. Silent Platform Deactivation via .env Wipe
During major system or package updates, the active environment file (`~/.hermes/.env`) can occasionally be initialized or partially cleared (e.g. leaving only a single new key). 

### Symptoms
- The gateway starts without errors but does not connect to Telegram (or other messaging platforms).
- `hermes config` reports `Telegram: not configured`.
- Gateway logs show:
  `WARNING gateway.run: No messaging platforms enabled. Gateway will continue running for cron job execution.`
  or
  `WARNING gateway.run: No user allowlists configured. All unauthorized users will be denied.`

### Recovery Recipe
1. Check the automatic pre-update state snapshots under `~/.hermes/state-snapshots/`.
2. Find the most recent snapshot directory (e.g., `~/.hermes/state-snapshots/2026xxxx-xxxxxx-pre-update/`).
3. Read the original `.env` file from the snapshot and extract key variables such as `TELEGRAM_BOT_TOKEN`, `TELEGRAM_HOME_CHANNEL`, `OPENROUTER_API_KEY`, and others.
4. Merge the missing keys back into active `~/.hermes/.env`.
5. Restart the gateway service:
   ```bash
   hermes gateway restart
   ```

---

## 2. Broken config.yaml Silently Ignored
If `config.yaml` contains any YAML parsing errors (e.g. unquoted characters, or a markdown-formatted link like `[url](url)` written into a URL field), the parser will fail.

### Symptoms
- `hermes doctor` shows:
  `Failed to parse ~/.hermes/config.yaml: while parsing a block mapping... Falling back to default config — every user override is being IGNORED.`

### Recovery Recipe
Do not attempt to write directly to `config.yaml` if protected by system guards. Use the command-line tool to overwrite the broken key with clean raw text:
```bash
hermes config set model.base_url https://generativelanguage.googleapis.com/v1beta
```

---

## 3. Launching the Dashboard from Non-Interactive Agents
Running `hermes dashboard` starts a blocking web server process (`uvicorn`). When invoked by an automated agent inside a foreground `terminal()` call, the process blocks until timeout and is then forcefully killed, preventing the port from binding.

### Best Practice for Agents
Always launch the dashboard as a persistent background daemon:
- Use the `background=true` parameter in the `terminal` tool.
- Omit `notify_on_complete=true` (since it never exits).
- Pass `--no-open` and `--skip-build` to prevent browser open blocks and slow builds:
  ```bash
  hermes dashboard --no-open --skip-build
  ```
- Verify binding with `lsof -i :9119`.
