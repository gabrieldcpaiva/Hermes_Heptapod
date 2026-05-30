# Antigravity / Henry Architecture Reference

Gabriel is a former Antigravity user and admires Henry's autonomy design. This is a quick reference for discussion purposes — NOT something to replicate in Hermes (it's Google-proprietary).

## What Was Antigravity?

- Google's AI desktop agent (internal codename: "Henry", product name: "Jetski" in logs)
- Built on Electron/VSCode shell (`jetskiAgent` / `jetskiMain`)
- Used Chrome DevTools Protocol (CDP) for browser automation
- Launched its own Chrome instance on port 9222 with a dedicated profile at `~/.gemini/antigravity-browser-profile`
- Had an HTML artifact viewer watching `~/.gemini/antigravity/html_artifacts/`

## Architecture (from log analysis)

```
Antigravity.app
├── Electron shell (VSCode fork)
│   ├── Renderer: jetskiAgent/main.js
│   ├── Main process: main.js
│   └── Bootstrap: bootstrap-fork.js
├── Node.js agent runtime ("jetski")
│   ├── ReAct-style autonomy loop
│   ├── FileWatch service (file system monitoring)
│   └── consumeAgentStateStream (streaming agent state via gRPC/connect)
├── Chrome CDP browser (port 9222)
└── Extensions: LaTeX Workshop, Java, Ruby LSP, Vim
```

## Key Design Patterns (that Gabriel admired)

1. **Streaming agent state** — `consumeAgentStateStream` with UUID-based session tracking
2. **File system watching** — reactive file monitoring with auto-reconnect on disconnect
3. **Browser isolation** — separate Chrome profile, auto-launch with CDP, health-check polling
4. **HTML artifact generation** — agents write HTML files that auto-render in a viewer
5. **Profiling markers** — perf profiling STARTED/DONE pairs for agent turns

## Why It's Gone

Google broke the Gemini API integration (May 2026), making Antigravity unusable. Gabriel migrated to Hermes.

## Related Files on Gabriel's Machine

- `/Applications/Antigravity.app/` — the app bundle
- `~/.antigravity/` — user config, extensions
- `~/.gemini/antigravity-browser-profile/` — browser profile
- `~/Library/Application Support/Antigravity/logs/` — session logs
- `~/abacusclawchat.txt` — chat log from Abacus (Claude in Antigravity)
- `~/Downloads/Documents/SYSTEM PROMPT_ ACME — ACcomplish Master Expert__.md` — ACME system prompt (different agent framework)
- `~/Downloads/Documents/optimized_prompt_for_deepagent_on_20260316T181237.pdf` — deep agent prompt optimization

## What Gabriel Wants to Recreate

Gabriel expressed interest in building a "Cinema Studio" using Google Flow (Google's creative AI for video/story generation). If Flow API access is available, this could replicate some of Antigravity's creative autonomy in an open framework.
