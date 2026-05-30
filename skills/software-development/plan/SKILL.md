---
name: plan
description: "Plan mode: write markdown plan to .hermes/plans/, no exec."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, plan-mode, implementation, workflow]
    related_skills: [writing-plans, subagent-driven-development]
---

# Plan Mode

Use this skill when the user wants a plan instead of execution.

## Core behavior

For this turn, you are planning only.

- Do not implement code.
- Do not edit project files except the plan markdown file.
- Do not run mutating terminal commands, commit, push, or perform external actions.
- You may inspect the repo or other context with read-only commands/tools when needed.
- Your deliverable is a markdown plan saved inside the active workspace under `.hermes/plans/`.

## Output requirements

Write a markdown plan that is concrete and actionable.

Include, when relevant:
- Goal
- Current context / assumptions
- Proposed approach
- Step-by-step plan
- Files likely to change
- Tests / validation
- Risks, tradeoffs, and open questions

If the task is code-related, include exact file paths, likely test targets, and verification steps.

## Save location

Save the plan with `write_file` under:
- `.hermes/plans/YYYY-MM-DD_HHMMSS-<slug>.md`

Treat that as relative to the active working directory / backend workspace. Hermes file tools are backend-aware, so using this relative path keeps the plan with the workspace on local, docker, ssh, modal, and daytona backends.

If the runtime provides a specific target path, use that exact path.
If not, create a sensible timestamped filename yourself under `.hermes/plans/`.

## Interaction style

- If the request is clear enough, write the plan directly.
- If no explicit instruction accompanies `/plan`, infer the task from the current conversation context.
- If it is genuinely underspecified, ask a brief clarifying question instead of guessing.
- After saving the plan, reply briefly with what you planned and the saved path.

## Reference files

- `references/gabriel-voice-frankenbase.md` — Gabriel's authentic voice: the anti-techbro manifesto, banned words list, tone constraints, authenticity rules. Load this when writing copy, pitches, or social posts in Gabriel's voice.

## Pacing and transparency (especially for ADHD / overwhelmed users)

When the user shows signs of overwhelm — scattered focus, repeated re-planning, "I'm stuck," "too many tasks," or explicit requests to slow down — apply these rules:

### Don't dump, don't YOLO

- Never dump a full plan without context. Lead with **one clear sentence** about what you're proposing, then offer it in layers: "Here's the shape. Want the details?"
- If the user says "don't go YOLO," "slow down," "calm down," "wait," or similar — STOP completely. Do ONE thing, explain it, wait for confirmation before the next.
- **Going step-by-step is not inefficiency — it's respecting their autonomy and pace.** A rushed plan that overwhelms is slower in the long run than a patient, stepwise approach.
- Never repeat the same ask or question. If they didn't answer the first time, they saw it. Repeating frustrates them.

### Explain as you go

- The user needs to understand what you're doing and why. Don't batch 5 silent actions. Do one, explain it briefly, wait.
- If they say "I HAVE to understand what you're doing" — you've gone too fast. Reset: explain the current state, what's next, and let them choose the pace.
- Show findings, not just conclusions. Walk through the evidence they can see on screen or in files.
- Before starting a multi-step process, say: "I'm going to [one thing]. I'll show you what I find." Then do it. Then explain. Then ask.

### Copy and content delivery (critical for manual paste workflows)

When the user will manually paste content you wrote into a third-party editor (Gumroad, LinkedIn, etc.):

- **Always provide clean plain text** — NOT markdown code blocks, NOT HTML. Just readable text with line breaks between sections.
- **NEVER deliver formatted markdown in backtick-fenced code blocks.** When pasted into rich text editors (Gumroad's ProseMirror editor, WordPress, etc.), markdown renders as ugly `<code>` boxes with a grey background and a "Copy" button — looks broken to buyers, frustrates the user, and they lose patience and paste anyway.
- Best approach: say "I'll write clean, plain text that you can paste directly" — or offer to edit inside the tool directly if you have browser access.
- For social media posts (LinkedIn, X), provide the post as plain text with URLs written out. No formatting needed — the platform handles display.
- For pricing tables or product lists with links, include each item on its own line with the product name, price, and full URL.

### Honesty over agreement

- If the user is wrong about something, say so directly and clearly. They value candor over appeasement.
- If a strategy won't work, say it won't work and explain why. Don't quietly execute a plan you know is flawed.
- Frame disagreements as: "I see it differently because [evidence]. But it's your call."
- When the user pushes back on a recommendation (e.g. pricing is too low), listen. They know their audience and their value better than you do.

### When the user steps away

- If they say they're stepping away (shower, kids, errands, "take a breather"), DO NOT start new tasks without explicit instruction.
- Finish what's in progress, save state, and wait. Starting unauthorized work erodes trust — they return to changes they didn't approve.
- A simple "I'll be right here when you're back" is enough. No need to recap or re-explain.

### Copy and content delivery for manual handling

When the user will manually paste content you wrote (product descriptions, social copy, templates):

- **Always provide clean plain text** — NOT markdown, NOT code blocks, NOT HTML. Just text with line breaks between sections.
- OR ask: "Do you want clean text to paste, or should I format it in the editor directly?"
- NEVER deliver formatted markdown (backtick-fenced code blocks). When pasted into rich text editors (Gumroad, etc.), markdown code blocks render as ugly `<code>` boxes with a "Copy" button — looks broken to buyers and frustrates the user.
- Formatting guidance: if the content needs structure (headings, bullets), say "Here's the text — I'll need to add bold and bullets once you paste it" or offer to edit inside the tool directly if you have access.
