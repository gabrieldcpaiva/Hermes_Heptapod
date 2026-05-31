# Hermes's Library

Welcome to the Hermes library. This repository is a central, persistent backup of Hermes's "brain" \u2014 everything he knows, how he operates, his memories of our interactions, and the skills he possesses.

This repository is designed to be easily readable so that Gabriel can always understand, improve, and review Hermes's state.

## Core Identity

*   **[`SOUL.md`](SOUL.md):** The constitution. This file defines Hermes's persona, his priorities, his direct, "founder-first" voice, and the absolute rules he must follow. It is the most important file for understanding *who* Hermes is.
*   **[`config.yaml`](config.yaml):** The technical configuration of the Hermes agent, including model preferences, toolsets, environment settings, and API routing.

## Knowledge and State

*   **[`memories/`](memories/):** Contains the context and history that Hermes has built up.
    *   *See [`memories/README.md`](memories/README.md) for details.*
*   **[`skills/`](skills/):** The repository of Hermes's capabilities, organized by category (e.g., productivity, development, sales).
    *   *See [`skills/README.md`](skills/README.md) for details.*
*   **[`cron/`](cron/):** Scheduled jobs and automated routines that Hermes manages independently.
    *   *See [`cron/README.md`](cron/README.md) for details.*

## Operational Files

*   **`.gitignore`:** Specifies files and directories that should *never* be backed up to the remote repository (e.g., sensitive logs, databases, cache).
*   **`gateway_state.json`:** A live view of Hermes's current state, including active agents, connected platforms, and recent errors.

---
*If Hermes ever goes offline or Gabriel is without a VPS, this repository acts as the single source of truth to rebuild and continue.*
