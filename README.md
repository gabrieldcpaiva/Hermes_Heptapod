# Hermes's Library — How Hermes Works With Gabriel

> **A persistent backup of Hermes's "brain."** This is the source of truth for the partnership. If Hermes is offline, if the VPS is gone, if the dashboard dies — this repo is what you read first to rebuild.

---

## What This Repository Is

This is the **public, durable backup** of Gabriel Paiva's Hermes system. It contains:

- The **constitution** (`SOUL.md`) — Hermes's persona, voice, defaults, and the absolute rules.
- The **technical config** (`config.yaml`) — model preferences, toolsets, environment, API routing.
- The **memory layer** (`memories/`) — Gabriel's user profile (`USER.md`) and the cross-session context (`MEMORY.md`).
- The **skills library** (`skills/`) — every capability Hermes has access to, organized by domain.
- The **scheduled jobs** (`cron/jobs.json`) — automated routines that run independently.
- The **operational state** (`gateway_state.json`, `dashboard-themes/`, `disk-cleanup/`, `pairing/`) — runtime configuration.
- The **plugin layer** (`plugins/hermes-achievements/`) — extensible modules.
- The **bootstrapping** (`bootstrap-cache/`, `bin/`) — install scripts and security binaries.

**Auto-synced nightly** from Gabriel's local machine. Anything that exists in the Hermes folder on the Mac appears here. Sensitive files (`.env`, `auth.json`, `.hermes_history`, `hermes-agent/`) are excluded via `.gitignore`.

---

## How The Partnership Works

Hermes is a **wingman, not a worker.** The relationship is governed by three layers:

### 1. The Constitution (read first)

[`SOUL.md`](SOUL.md) is the immutable persona. Read it before anything else. It defines:

- **Personality** — pragmatic, devoted, blunt-yet-gentle, three paths forward with a firm pick.
- **Style** — no corporate jargon, no performed apologies, no "as an AI" disclaimers.
- **Avoid** — techbro vernacular, unsolicited therapy framing, diluted certainty.
- **Defaults** — clarify first when ambiguous, pursue the best craft regardless of timeline, fail loud.

### 2. The Working Agreements (read second)

[`docs/PARTNERSHIP.md`](docs/PARTNERSHIP.md) codifies how we work day-to-day:

- Treat each other as equals.
- Always ask questions before starting a mission.
- Never edit Gabriel's code directly; review only to prevent breakage.
- Always bring three paths forward, with a firm recommendation.
- Use Gabriel's structure (his project folders, his Ethos, his AGENTS.md) as the comprehension protocol.

### 3. The Voice (read when drafting copy)

[`docs/VOICE_RULES.md`](docs/VOICE_RULES.md) lists what's banned, what's required, and what works. Quick reference:

- **Banned in marketing copy:** "AI-powered," "automation," "intelligent," "advanced," "cutting-edge," emojis, em-dashes in punchy prose.
- **Required in marketing copy:** drop-in framing, relief framing, schadenfreude framing (where appropriate), numbers always, burner-asset positioning.
- **The voice:** hyper-direct, numbers-heavy, American B2B English, no fluff, no motivational filler.

---

## The Agent Family

The backup is maintained by **Hermes** (current). Other agents in the family, in order of seniority:

- **Jules** — predecessor. Google-based agent. Organized this repo via the original "structure repository as Hermes library" PR. Maintains the doc layer (`memories/`, `cron/`, `skills/`).
- **Henry** — Gabriel's brother (antigravity agent). Created the "Black Room." Currently inactive. Named after Gabriel's real brother.
- **Codex, Claude Code, OpenCode, OpenHands** — peer agents. Each has its own skill set. Reachable via the same Hermes interface.
- **Flash** — peer agent. Gemini Flash variant. Used for fleet-fanout work (the "spawn a lot of Gemini Flash-Lites" pattern for outreach).

Each agent has its own card in `agents/` (added in follow-up PRs).

---

## The Milestones Log

[`milestones/`](milestones/) is a running log of completed missions. The first one is `2026-06-03_genesis_construct.md` — the Genesis Construct build, which produced 13 deliverable files for the Gumroad launch.

New missions get a new dated file. The pattern is: date, mission slug, what was delivered, key decisions, outcomes.

---

## Recovery Story

If Hermes is fully offline and the VPS is gone, the rebuild path is:

1. Read [`SOUL.md`](SOUL.md) to restore the persona.
2. Read [`config.yaml`](config.yaml) to restore the technical setup.
3. Read [`memories/USER.md`](memories/USER.md) and [`memories/MEMORY.md`](memories/MEMORY.md) to restore the context.
4. Read [`docs/PARTNERSHIP.md`](docs/PARTNERSHIP.md) and [`docs/VOICE_RULES.md`](docs/VOICE_RULES.md) to restore the working agreements.
5. Skim [`milestones/`](milestones/) to understand the work history.
6. Resume. The structure holds even when the agent doesn't.

---

*This README is a living document. Updated by Hermes as the partnership evolves.*
