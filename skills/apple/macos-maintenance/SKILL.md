---
name: macos-maintenance
description: macOS disk space analysis, cache pruning, and general system diagnostics.
category: apple
tags:
  - macos
  - maintenance
  - disk-cleanup
  - diagnostics
---

# macOS Maintenance & Disk Cleanup

A playbook for diagnosing, analyzing, and reclaiming disk space on macOS systems without disrupting user data or deleting critical local files.

## Diagnostics & Investigation Workflow

When the user runs out of space, slow performance occurs, or disk space needs to be mapped:

1. **Check Filesystem Usage**
   ```bash
   df -h
   ```
   Identify which volume is full (typically `/System/Volumes/Data` mapped to `/`).

2. **Map Home Directory Hogs**
   Analyze top-level directories under the user's home path:
   ```bash
   du -hd 1 ~ 2>/dev/null | sort -hr
   ```

3. **Drill Down into the User Library**
   Almost always, the major source of junk is hidden inside `~/Library`. Analyze its top-level folders:
   ```bash
   du -hd 1 ~/Library 2>/dev/null | sort -hr
   ```
   Typically, the culprits live in:
   - `~/Library/Application Support` (app data/persistent caches)
   - `~/Library/Caches` (transient caches)
   - `~/Library/Containers` (sandboxed macOS app containers)
   - `~/Library/Group Containers` (shared app containers)

4. **Identify Deep Subfolder Hogs**
   Run a high-resolution subfolder analysis across the main data/cache directories:
   ```bash
   du -hd 2 ~/Library/Application\ Support ~/Library/Caches ~/Library/Containers 2>/dev/null | sort -hr | head -n 30
   ```

5. **Search for Gigantic Files**
   Locate files larger than 100MB in the user's directory:
   ```bash
   find ~ -type f -size +100M -exec du -sh {} + 2>/dev/null | sort -hr | head -n 20
   ```

---

## Safe Cache Reclamation Targets

These are high-yield, safe targets that can be deleted to reclaim gigabytes of space immediately.

### 1. Spotify Offline Caches (Yield: 5 GB – 30 GB)
Spotify aggressively caches streamed audio tracks.
- **Cache paths:**
  - `~/Library/Caches/com.spotify.client`
  - `~/Library/Application Support/Spotify/PersistentCache`
- **Safety:** 100% safe. Spotify will automatically recreate these paths and re-fetch files as needed.

### 2. Browser Website IndexedDB & Databases (Yield: 5 GB – 20 GB)
Web apps running in Safari/Chrome (e.g., Venice.ai, large chat platforms, local web interfaces) use IndexedDB to store heavy local records.
- **Safari Path:** `~/Library/Containers/com.apple.Safari/Data/Library/WebKit/WebsiteData/Default/`
- **Diagnostic Step:** Check subfolders here. Look for folders with hash names and inspect the `origin` file inside them to map them to web domains:
  ```bash
  strings ~/Library/Containers/com.apple.Safari/Data/Library/WebKit/WebsiteData/Default/<HASH_DIR>/origin
  ```
- **Safety:** Generally safe if the user uses cloud-synced accounts, but clear Venice.ai or database folders with an explanation of what they are (local chat histories/files will be reset to cloud state).

### 3. Homebrew Cache (Yield: 1 GB – 5 GB)
Homebrew retains downloads of downloaded formula/cask packages.
- **Cache path:** `~/Library/Caches/Homebrew`
- **Safety:** 100% safe. Run:
  ```bash
  brew cleanup --prune=all
  ```

### 4. Headless/Automated Browser Profiles (Yield: 1 GB – 10 GB)
AI browser automation tools or Chromium frameworks download massive "Optimization Guide" on-device models or heavy profiles.
- **Cache paths:**
  - `~/.gemini/antigravity-browser-profile/OptGuideOnDeviceModel` (often holds multiple 4GB+ on-device model files)
- **Safety:** High. These can be removed safely, though Chromium will re-download model binaries if its AI features are triggered again.

### 5. Google Chrome & General App Caches (Yield: 1 GB – 5 GB)
- **Caches:**
  - `~/Library/Caches/Google/Chrome`
  - `~/Library/Caches/com.openai.atlas` (ChatGPT macOS app)
  - `~/Library/Caches/com.openai.codex` (Codex app)
  - `~/Library/Caches/@accomplishdesktop-updater` (or other Electron app updaters)

---

## Pitfalls & Defensive Rules

- **NEVER blindly wipe Application Support folders.** Wiping `/Application Support` subfolders can lose offline databases (e.g., Notion offline edits, local Obsidian vaults, crypto wallets, password managers, local projects). Only delete paths confirmed to be transient caches or updater directories.
- **Check if the App is Running first.** Never delete caches for a currently open application. Check the process list and ask the user to close it, or close it safely:
  ```bash
  pgrep -f "Spotify" && killall "Spotify"
  ```
- **Do not delete Playwright binaries** (`~/Library/Caches/ms-playwright`) if the user is actively running local browser automation scripts or browser tools, as this triggers slow re-downloads. Always verify active developer tooling first.
- **Verify Apple Mail usage before targeting mail folders.** If a user doesn't use Apple Mail, their `~/Library/Mail` will be tiny (~2MB) and is not worth touching. Wiping a heavy Mail folder should only be done via Mail's built-in "Erase Deleted Items" or after ensuring they use an alternate IMAP/Webmail platform.

---

## Process Management & Force-Killing Misbehaving Apps

When macOS applications or background processes (e.g., Apple Mail, browser instances, runaway helpers, or duplicate daemons) lock up, freeze, or spam the user with error pop-ups:

### 1. Identify Target Processes
Locate the misbehaving process using a case-insensitive lookup:
```bash
ps aux | grep -i "Mail"
```

### 2. Direct Force-Kill (Immediate Relief)
When the user expresses frustration, skip long diagnostic chats or graceful shutdowns. Execute direct termination immediately:
- **Using `killall` (Direct app names):**
  ```bash
  killall Mail
  killall "Google Chrome"
  ```
- **Programmatic Force-Kill (Path-based fallback):**
  Identify and terminate target apps safely by checking their path:
  ```python
  import subprocess, os, signal
  p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
  out, _ = p.communicate()
  for line in out.decode("utf-8", errors="ignore").split("\n"):
      if "Applications/Mail.app" in line and "grep" not in line:
          pid = int(line.split()[1])
          os.kill(pid, signal.SIGKILL)
  ```

### 3. Verification
Verify that the target process is dead and no duplicates or orphaned processes remain:
```bash
pgrep -f "Mail"
```
