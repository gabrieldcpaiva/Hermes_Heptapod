# Skills Library

This directory is the repository of Hermes's capabilities. It contains all the tools, scripts, and workflows that Hermes has access to or has learned.

## Structure

Skills are organized into domain-specific folders to keep things clean and accessible.

### Key Categories

*   **`productivity/`**, **`software-development/`**, **`sales/`**, etc.: These folders group related skills. For example, `sales` might contain specific warm-outreach scripts or product placement workflows.
*   **`.hub/`** & **`.bundled_manifest`**: Core system files that define how these skills are loaded and managed by Hermes.
*   **`.curator_state`** & **`.usage.json`**: Tracking files used by Hermes to manage the state and usage of these skills.

If Hermes learns a new capability or if Gabriel writes a new script for Hermes to use, it should be categorized and placed within the appropriate subdirectory here.
