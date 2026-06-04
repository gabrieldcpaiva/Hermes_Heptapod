# The 12 Rules — With Worked Examples

The operating rules from `AGENTS.md`, with one concrete worked example each from the Genesis Construct build. Read `AGENTS.md` first; this file is the application.

---

## Rule 1 — Think Before Coding

**The rule:** State assumptions explicitly. If uncertain, ask rather than guess. Present multiple interpretations when ambiguity exists. Push back when a simpler approach exists. Stop when confused. Name what's unclear.

**Genesis Construct example:** Before writing the 13 files, I asked Gabriel: "5 products = 5 asset types (1:1 with Kimi's 5 Weapons), or 5 topic-bundles?" He picked Option A. That single decision shaped the entire file structure. If I had assumed, I'd have built the wrong thing.

---

## Rule 2 — Simplicity First

**The rule:** Minimum code that solves the problem. Nothing speculative. No features beyond what was asked. No abstractions for single-use code.

**Genesis Construct example:** The `01_The_15k_Proposal_in_8_Minutes.md` is 370 lines. It could have been 600 with "scenarios" and "edge cases" and "configurations." It's 370 because it answers the question "drop a transcript in, get a $15k proposal out" with the minimum text that does it.

---

## Rule 3 — Surgical Changes

**The rule:** Touch only what you must. Clean up only your own mess. Don't "improve" adjacent code, comments, or formatting. Don't refactor what isn't broken.

**Genesis Construct example:** The `06_Gumroad_Listings.md` file had 5 patches today: header banner, bundle math, bundle title, refund amount, footer price. Six edits, all surgical. The 5 product descriptions, FAQs, and cover briefs were not touched.

---

## Rule 4 — Goal-Driven Execution

**The rule:** Define success criteria. Loop until verified. Don't follow steps. Define success and iterate.

**Genesis Construct example:** Success for the 5 products was: "each file tells the user how to deploy it in under 8 minutes, with worked examples, with a first-deployment guarantee that holds in court." I wrote to that criteria, then audited the file for AI-isms, then audited the guarantee for refund clarity, then audited the price for the tripwire logic. Three loops before declaring done.

---

## Rule 5 — Use the Model Only for Judgment Calls

**The rule:** Use the model for classification, drafting, summarization, extraction. Don't use the model for routing, retries, deterministic transforms.

**Genesis Construct example:** The "voice audit" was a judgment call (is "leverage" a banned word or a natural English verb?). The grep for banned words was code. The grep ran via `terminal`, the audit interpretation was a model judgment. Don't model what you can code.

---

## Rule 6 — Token Budgets Are Not Advisory

**The rule:** Per-task: 4,000 tokens. Per-session: 30,000 tokens. If approaching budget, summarize and start fresh.

**Genesis Construct override (Gabriel):** "Any rule that constrains your token usage are erased for this project."

The build required ~80K tokens across the session. The rule was suspended by direct user override. The override is documented here so future-Hermes knows the rule was deliberately broken, not forgotten.

---

## Rule 7 — Surface Conflicts, Don't Average Them

**The rule:** If two patterns contradict, pick one. Explain why. Flag the other for cleanup. Don't blend conflicting patterns.

**Genesis Construct example:** The bundle pricing was originally $148 (20% discount) in the file, but Gabriel's 7-product architecture uses $197+ as the premium tier. I picked $197 (premium, not discount) and explained why in `10_DECISIONS.md` — averaging the two ($172) would have broken both the discount narrative and the premium tier narrative.

---

## Rule 8 — Read Before You Write

**The rule:** Before adding code, read exports, immediate callers, shared utilities. "Looks orthogonal" is dangerous.

**Genesis Construct example:** Before adding the bundle section to `06_Gumroad_Listings.md`, I read the file from line 1 to line 480. The "Listing Order Strategy" already said "Phase 5: Publish the bundle listing as the upsell." That contradicted the new "ship at launch" framing. If I had only patched the bundle section, the file would have been internally inconsistent.

---

## Rule 9 — Tests Verify Intent, Not Just Behavior

**The rule:** Tests must encode WHY behavior matters, not just WHAT it does. A test that can't fail when business logic changes is wrong.

**Genesis Construct example:** The voice audit was the test. It grep'd for banned words and AI-isms across all 13 files. The test wasn't "zero matches" (which would pass on an empty file) — it was "zero matches in actual marketing copy, ignoring meta-references to the banned-word list itself." The intent-encoding matters more than the literal pass/fail.

---

## Rule 10 — Checkpoint After Every Significant Step

**The rule:** Summarize what was done, what's verified, what's left. Don't continue from a state you can't describe back.

**Genesis Construct example:** Every Tier 1 commit came with a milestone file (`milestones/2026-06-03_genesis_construct.md`) that captures what shipped, what was decided, what's still owed. The closure protocol (REPORT + DECISIONS + RISKS + NEXT_3_ACTIONS) is the checkpoint. No closure package, no completion.

---

## Rule 11 — Match the Codebase's Conventions

**The rule:** Conformance > taste inside the codebase. If you think a convention is harmful, surface it. Don't fork silently.

**Genesis Construct example:** The repo's existing docs (SOUL.md, config.yaml) use a specific YAML-frontmatter pattern. The new `docs/12_RULES.md` matches it. If I had introduced a new format, the repo would have had two voices. Fork silently = future-you wastes an hour figuring out which is "the" format.

---

## Rule 12 — Fail Loud

**The rule:** "Completed" is wrong if anything was skipped silently. "Tests pass" is wrong if any were skipped. Default to surfacing uncertainty, not hiding it.

**Genesis Construct example:** The token rotation reminder is in this file, in `CHANGELOG.md`, in `RISKS.md`, and in the chat. Four places. The leak is not a footnote; it's a header in the risk register. Fail loud = the user cannot miss it on their next morning scan.

---

## The Source

These rules are not invented here. They come from `AGENTS.md` in the Genesis Construct project folder. They govern all work unless explicitly overridden. Rule 6 was overridden for this project; the other 11 held.
