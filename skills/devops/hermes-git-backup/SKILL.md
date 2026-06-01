---
name: hermes-git-backup
description: Back up Hermes configuration to a Git remote (e.g., GitHub) while excluding secrets and sensitive files.
version: 1.0.0
author: Hermes
---

## When to Use
You want to version‑control your Hermes configuration (`~/.hermes`) for backup, reproducibility, or collaboration, **without** exposing API keys, tokens, or other secrets.

## Prerequisites
- Git installed (`git --version` works).
- A remote repository already created (e.g., on GitHub, GitLab, or a self‑hosted Gitea).
- Write access to that remote.
- Hermes is running or at least its configuration directory exists.

## Steps
1. **Enter the Hermes directory**  
   ```bash
   cd ~/.hermes
   ```

2. **(Re)initialize a clean Git repo** – this removes any accidental history that might contain secrets.  
   ```bash
   rm -rf .git   # delete existing repo if present
   git init
   ```

3. **Ensure a robust `.gitignore`** – at minimum include the patterns below.  
   If the file does not exist, create it; otherwise, verify it contains these lines (add any missing).  
   ```gitignore
   # Secrets and sensitive data
   .env
   *.key
   *.pem
   *secret*
   *token*
   *credential*
   auth.json
   channel_directory.json
   processes.json

   # Logs
   logs/
   *.log

   # Cache and temporary data
   cache/
   .sandboxes/
   node/
   images/
   image_cache/
   audio_cache/
   *_cache.json
   context_length_cache.yaml

   # Database and state files
   state.db
   state.db-shm
   state.db-wal
   kanban.db
   *.db
   *.db-*
   sessions/
   pastes/
   shared/
   state-snapshots/
   models_dev_cache.json
   provider_models_cache.json
   ollama_cloud_models_cache.json
   interrupt_debug.log

   # Config backups (may contain secrets)
   config.yaml.bak.*

   # PID and lock files
   *.pid
   *.lock

   # macOS
   .DS_Store

   # Hermes specific
   hermes-agent/   # embedded repo – treat as submodule if needed, else ignore
   .hermes_history
   .skills_prompt_snapshot.json
   ```

4. **Stage all non‑ignored files**  
   ```bash
   git add .
   ```

5. **Verify what will be committed** (secrets should NOT appear)  
   ```bash
   git status --porcelain
   git diff --cached --name-only | grep -E "\.(env|key|pem|token|credential)" && echo "WARNING: potential secret staged!" || echo "OK"
   ```
   If a secret file appears staged, unstage it with:
   ```bash
   git rm --cached <file>
   ```
   Then add the file to `.gitignore` (if not already) and repeat the verification.

6. **Commit**  
   ```bash
   git config user.name "Your Name"   # set once per repo if not already
   git config user.email "you@example.com"
   git commit -m "Initial commit: Hermes config (secrets excluded via .gitignore)"
   ```

7. **Add the remote** (replace URL with your own)  
   ```bash
   git remote add origin https://github.com/youruser/your-repo.git
   ```

8. **Push to remote**  
   ```bash
   git push -u origin main   # or master, depending on your default branch
   ```

9. **(Optional) Verify on the remote** – visit the repository URL and confirm that only non‑secret files are present.

## Pitfalls & How to Avoid Them
- **Accidentally committing secrets** – always run `git status --porcelain` and visually check for files like `.env`, `auth.json`, `.hermes_history`. If you see any, run `git rm --cached <file>` and add the file to `.gitignore` before committing.
- **Embedded repository warnings** – Hermes ships with a `hermes-agent/` subdirectory that is itself a Git repo. If you get warnings about adding an embedded repo, either ignore them (they are safe) or add `hermes-agent/` to `.gitignore` and treat it as a submodule separately.
- **Force‑pushing history** – never rewrite history after you have pushed; if you must remove a secret that slipped, delete the file, add it to `.gitignore`, `git commit --amend`, then `git push --force` **only** if you are certain no one else has cloned the repo.
- **Remote authentication** – use HTTPS with a personal access token, or SSH keys, depending on your remote’s settings. Do not embed passwords in the URL.
- **Divergent histories** – If the remote already has commits that are not in your local repo (e.g., after a force push or separate init), git will reject pushes. First try `git pull origin main --allow-unrelated-histories` to merge the histories. If you intentionally want to replace the remote history (e.g., you are resetting the backup), use `git push -f origin main` **only after confirming** you won't lose needed data.
- **Divergent histories** – If the remote already has commits that are not in your local repo (e.g., after a force push or separate init), git will reject pushes. First try `git pull origin main --allow-unrelated-histories` to merge the histories. If you intentionally want to replace the remote history (e.g., you are resetting the backup), use `git push -f origin main` **only after confirming** you won't lose needed data.

## Verification
After pushing, clone the repository to a temporary location and ensure:
- No `.env`, `auth.json`, `.hermes_history`, or other secret files are present.
- Essential files like `config.yaml`, `skills/`, `cron/`, `memories/` exist.
- The Hermes agent can still start from this clone (optional test).

## Related Skills
- `hermes-agent` – for configuring Hermes itself.
- `git` – generic Git workflow (if you need a more general reference).

---