# CHANGELOG — Hermes Heptapod

The durable log of changes to this repo. If a doc gets eaten by a silent sync, this file is the receipt.

Format: dated entry, named mission, what shipped, what was decided, what's still owed.

---

## 2026-06-03 — Genesis Construct (Day 1)

**Mission:** Bring structure to a 7-product system. Ship the operational layer (5 products) to Gumroad. Open the repo to the public so the work is durable.

**Shipped to main (5 commits, 4 seconds):**

| Path | Size | Role |
|---|---|---|
| `README.md` | 4,898 B | "How Hermes works with Gabriel" — new entry point |
| `docs/PARTNERSHIP.md` | 4,738 B | The 8 working agreements |
| `docs/VOICE_RULES.md` | 6,071 B | Banned words, required patterns, the burner-asset voice |
| `milestones/README.md` | 1,460 B | The milestones system |
| `milestones/2026-06-03_genesis_construct.md` | 6,157 B | First mission log |

**Decisions locked:**

- 5 products sold individually at $37 + complete-system bundle at $197 (premium tier, matches the 7-product architecture)
- Tripwire framing: the 5 individual products are the demo of the work; the $197 bundle is the actual money
- Source of truth: `https://open-zinnia-jdg4.here.now/` — never deviate without checking this page
- The Genesis Construct product files live locally in `02_Awaiting_Approval/`, NOT in this repo (products ≠ canon)

**Still owed:**

- Tier 2 docs: `CHANGELOG.md` (this file), `docs/12_RULES.md`, `agents/hermes.md`, `agents/jules.md`
- Publish 5 listings + 1 bundle to Gumroad (target: 2026-06-04 06:00 BRT)
- Post 5 Reddit threads + 5 Twitter threads (target: launch day)
- Decide on Jules' PR #1 (currently open, 2 commits behind main, his README is superseded by the new root)

**Risks tracked:**

- `ghp_In...RDhw` GitHub token leaked in chat — must rotate
- Gumroad requires designer-ready cover art (5 covers + 1 bundle cover) — designer not yet contracted
- The 4-hour launch window (11pm BRT → 6am BRT) is tight; no margin for redline iteration

---

## How to Use This File

When a mission ends, append a new dated section. Keep the format. Future-you (or future-Hermes) should be able to read the last 3 entries and reconstruct what happened, what was decided, and what's still owed.

If a doc disappears from main, the entry here tells you what was there.
