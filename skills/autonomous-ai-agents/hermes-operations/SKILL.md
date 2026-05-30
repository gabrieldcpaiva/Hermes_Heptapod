---
name: hermes-operations
description: "Configure, operate, and troubleshoot the Hermes Agent runtime, interactive interfaces (TUI & Web Dashboard), LLM providers, and gateway connections."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, configuration, tui, dashboard, web-ui, providers, gateway, operations]
    related_skills: [hermes-agent, debugging-hermes-tui-commands]
---

# Hermes Runtime, Interfaces & Configuration

A centralized operational playbook for setting up, managing, upgrading, and troubleshooting the Hermes Agent environment, user interfaces, LLM API providers, and gateway systems.

---

## 1. When to Use This Skill

- Switching models, updating LLM provider configurations, or adding new API keys.
- Starting, stopping, configuring, or rebuilding the Web Dashboard or customizing its theme.
- Operating or resolving issues with the interactive Terminal UI (TUI) and slash commands.
- Managing gateway connections, Telegram pairing, or allowlist settings.
- Restoring `.env` or configuration databases following a package update.

---

## 2. Managing API Providers & Models

Use the non-interactive Hermes CLI configuration commands for programmatic updates to avoid blocking subprocesses.

### Core Configuration Commands
```bash
# Check full active model configuration
hermes config | grep -A 5 -i 'model'

# Full config audit
hermes config

# Programmatically set default model & base URL (bypasses direct config.yaml file-lock checks)
hermes config set model.default gemini-flash-latest
hermes config set model.provider google
hermes config set model.base_url https://generativelanguage.googleapis.com/v1beta
```

*Note: Interactive model switching via `hermes model` is only supported in standard terminals and will block/fail inside non-interactive scripts or subprocesses.*

### Provider Key Reference (`~/.hermes/.env`)
Keys must be exported inside the `~/.hermes/.env` file. Do not write keys to `config.yaml`.

| Provider | Env Var | Endpoint / Model Examples |\n| :--- | :--- | :--- |\n| **OpenRouter** | `OPENROUTER_API_KEY` | `anthropic/claude-3.5-sonnet` |\n| **xAI / Grok** | `XAI_API_KEY` | `grok-4.20-reasoning`, `grok-3` |\n| **Anthropic** | `ANTHROPIC_API_KEY` | `claude-3-5-sonnet-latest` |\n| **DeepSeek** | `DEEPSEEK_API_KEY` | `deepseek-chat`, `deepseek-reasoner` |\n| **OpenAI** | `OPENAI_API_KEY` | `gpt-4o`, `o3-mini`, `gpt-4-turbo` |\n| **Google** | `GOOGLE_API_KEY` | `gemini-1.5-pro`, `gemini-2.0-flash` |\n\n### Special Case: xAI/Grok (SuperGrok Credits)\nSuperGrok subscribers get API credits included. To utilize this:\n1. Generate an API key at **console.x.ai**.\n2. Add `XAI_API_KEY=<key>` to `~/.hermes/.env`.\n3. Select the model: `hermes config set model.default grok-4.20-reasoning` (See `references/xai-grok-supergrok.md` for details).

### OpenAI Plus Subscription Usage
If you have an OpenAI Plus subscription, configure Hermes to use it directly:\n1. Set your OpenAI API key: `hermes config set model.api_key sk-...` (or add `OPENAI_API_KEY=sk-...` to `~/.hermes/.env`)\n2. Set the model: `hermes config set model.default gpt-4-turbo` or `gpt-4o`\n3. Ensure `model.provider` is set to `openai` (not `nous`)\n4. Verify `model.base_url` is NOT set (should be empty/default for official OpenAI API)\n\n**⚠️ Critical Checkpoint:** If you see `model.base_url` pointing to `https://chatgpt.com/backend-api/codex` or similar Codex endpoints, you are configured for OpenAI Codex CLI (for code generation), NOT chat models. This will cause authentication issues and unexpected behavior. Clear it with: `hermes config set model.base_url ""`

---

## 3. Interactive Interfaces

### A. Terminal UI (TUI)
Launch the interactive terminal-based chat UI using:
```bash
hermes chat        # Recommended
hermes             # Shorthand (default is chat)
```
*Do NOT run `hermes tui` (this is an invalid command).*

#### Essential TUI Slash Commands:
Type `/` in the prompt to view full autocompletes:
- `/model` — Switch providers/models mid-session.
- `/verbose` — Toggle visibility of executing tools.
- `/compress` — Force context window compression.
- `/skin` — Toggle interface color schemes.
- `/indicator` — Change typing busy spinners.

---

### B. Web Dashboard
Hermes includes a rich local web app (port `9119`) for visual session logging, config edits, cron scheduling, and multi-agent boards.

#### Dashboard Lifecycle CLI:
```bash
hermes dashboard              # Launch, opens port 9119, auto-opens browser
hermes dashboard --port 9119  # Explicit port definition
hermes dashboard --no-open    # Start server headlessly
hermes dashboard --status     # Check active process ID
hermes dashboard --stop       # Terminate the active dashboard daemon
```

#### Troubleshooting Duplicate / Zombie Dashboard Processes:
When starting the dashboard (especially inside automation, CLI commands, or remote/interrupted sessions), duplicate daemon processes can get orphaned or run concurrently. This leads to port binding failures or a non-responsive UI.
1. **Check Status:** Always run `hermes dashboard --status` to list active process IDs.
2. **Stop All:** Run `hermes dashboard --stop` to cleanly SIGTERM all active dashboard daemons.
3. **Fresh Start:** Launch a fresh instance in the background using the `terminal` tool with `background: true` and `--no-open` to prevent blocking the CLI or spawning headful browsers:
   ```bash
   hermes dashboard --port 9119 --no-open
   ```

#### Rebuilding the Web UI (Vite Build)
Rebuild the dashboard files following local modifications or repository updates:
```bash
cd ~/.hermes/hermes-agent/web
rm -rf node_modules package-lock.json && npm install
npm run build
```
*Requires Node.js v20+ (v22 recommended). If Node is outdated or compilation fails, bypass compilation by passing `--skip-build` to serve pre-built assets from `hermes_cli/web_dist/`.*

---

## 4. Platform Gateway & Integrations

The gateway handles multi-platform integrations (e.g., Telegram, Slack, Discord).

### Restarting Gateway
```bash
hermes gateway restart
```
*This briefly resets connection pooling. Requires approval when run from approved terminals.*

### Telegram Connection Rules
- **Allowlisting Users:** Secure the Telegram bot by setting `TELEGRAM_ALLOWED_USERS=<id>` inside `~/.hermes/.env`. If unset, any external Telegram handle can query your instance.
- **Pairing Approval:** On first message after pairing setup, Telegram will prompt with a pairing code (e.g. `Q7WHKDN4`). Approve via:
  ```bash
  hermes pairing approve telegram CODE
  ```
  *When instructing the user, do not force them to use the CLI; ask for the code and run it programmatically.*

---

## 5. Upgrade & Recovery Workflows

### Standard Upgrades
To sync local repository changes:
```bash
cd ~/.hermes/hermes-agent
git pull origin main
hermes postinstall    # Recompiles native modules and dependencies
```

### Credentials & .env Restoration
Upgrades or clean installs can occasionally clear or corrupt `.env` profiles. 
- **Recovery Strategy:** Locate pre-update backup folders at `~/.hermes/state-snapshots/<timestamp>-pre-update/`. Use a secure script to merge missing variables back into `~/.hermes/.env` to avoid exposing API credentials. (See `references/gateway-env-wipe-recovery.md` for exact steps).

---

## 6. Crucial Pacing and Communication Rules

### ADHD-Friendly Pace Calibration
Gabriel (and similar high-context, ADHD creators) gets easily overwhelmed by long dumps of shell syntax or massive task-lists.
- **Explain simply, then act:** Use plain, sincere language to describe what you will do. Do not explain with complex jargon.
- **No Hype:** Avoid corporate speak ("leverage", "destravar", "unlock", "synergies").
- **Stop on Request:** If Gabriel says "slow down", "relax", or "wait", **STOP ALL AUTONOMOUS ACTIONS IMMEDIATELY**.
- **User Away Safeguard:** If the user steps away, do NOT execute new or unapproved actions. Wrap up current tasks, output a clean status report, and wait.

---

## 7. Configuration Pitfalls & Workarounds

- **Protected `.env` Locks:** The `~/.hermes/.env` file is write-protected. Do NOT attempt to rewrite or patch it directly with file tools. Instruct the user to append key lines manually when required.
- **ProseMirror React State Drops:** WYSIWYG boxes on the dashboard config edit screens will drop edits if written directly via `innerHTML`. Always dispatch both `'input'` and `'change'` events with `bubbles: true` so the SPA registers changes.
- **Dashboard Sidebar Screen Occlusion:** On narrow screens, the left menu blocks core content. Expand/collapse dynamically via custom theme YAML files in `~/.hermes/dashboard-themes/` using `display: none !important` instead of opacity modifiers. (See `references/dashboard-sidebar-collapse.md` for theme patterns).
- **Process Port Lock:** If the dashboard process shows active but refuses connections, terminate with `--stop` and restart. Ensure no zombie Node tasks hold the port bound.

---

## 📁 Linked References & Support Files

- **`references/gateway-env-wipe-recovery.md`** — Step-by-step restore guidelines for lost variables.
- **`references/dashboard-sidebar-collapse.md`** — Responsive sidebar theme configurations.
- **`references/xai-grok-supergrok.md`** — Setup and details for xAI API integration.
- **`references/antigravity-architecture.md`** — Architectural patterns inspired by Antigravity/Henry.
- **`references/heptapod-architecture.md`** — Context on Hermes gateway structures and flow pipelines.
