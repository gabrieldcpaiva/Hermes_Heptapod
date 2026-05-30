---
name: chrome-session-automation
description: "Reusing active Chrome login sessions (cookies/storage) safely for local browser automation, bypassing ProcessSingleton and Chrome security blocks on macOS/Linux."
version: 1.0.0
category: software-development
metadata:
  tags: [chrome, browser-automation, cdp, cookies, active-session, macos]
---

# Chrome Session Automation

This skill provides a robust, zero-touch method for automating local browser tasks that require reusing the user's active, logged-in web sessions (e.g., LinkedIn, GitHub, SaaS portals) on macOS and Linux, without triggering OAuth/login security walls or risking profile corruption.

It solves three critical hurdles:
1. **Chrome ProcessSingleton Lock:** Chrome aborts if another instance is already running with the same `--user-data-dir`.
2. **Default Directory Security Block:** Modern Chrome (v120+) explicitly blocks opening `--remote-debugging-port` if `--user-data-dir` points to the default profile directory.
3. **Huge Profile Size:** Copying the entire profile folder (which carries gigabytes of cache and shaders) is too slow for quick tasks.

---

## Trigger Conditions

Use this skill when:
- You need to perform browser automation (e.g., scraping, messaging, dashboard actions) on a site where the user is already logged in locally.
- Direct remote login (from fresh cloud IPs) is blocked or risks account restriction.
- You hit the error: `DevTools remote debugging requires a non-default data directory` or `Failed to create a ProcessSingleton for your profile directory`.
- **Cloud Browser Blocked:** When using cloud browser services (Browserbase) triggers bot detection or CAPTCHAs, switch to local Chrome debugging port (9222) for authenticated session reuse.
- **Profile-Specific Sessions:** When the user has an active, logged-in Chrome profile (e.g., "Profile 2" on macOS) that contains authentication cookies needed for the task.

---

## Step-by-Step Methodology

### Step 1: Detect the Active Profile and Cookies Database
Locate which Chrome profile holds the active session. On macOS, profiles live under `~/Library/Application Support/Google/Chrome/`.
Run a quick Python SQLite query on the `Cookies` database of each profile directory (e.g., `Default`, `Profile 2`, `Profile 4`) to see where target cookies (like `linkedin.com`) exist:

```python
import sqlite3, os
# Path example: f"~/Library/Application Support/Google/Chrome/{profile_name}/Cookies"
# Run "SELECT host_key FROM cookies WHERE host_key LIKE '%target%'" to verify.
```

### Step 2: Gracefully Quit Chrome & Terminate Headless Zombies
You must close Chrome to release the SQLite database locks. On macOS, do this gracefully so Chrome preserves "Continue where you left off" state:

```bash
osascript -e 'quit application "Google Chrome"'
```

Wait up to 10 seconds for all Chrome pids to close. 

**CRITICAL PITFALL - ZOMBIE CHROME HEADLESS PORT LOCKS:** If helper or previous headless debugging sessions crashed or were aborted, they can leave behind multiple orphaned background `Google Chrome` processes. These zombie processes hold locks on the temporary profiles, and more importantly, they keep binding to port `9222`. This silently blocks any new debug Chrome instance from running (which returns an empty target list `[]` on `http://127.0.0.1:9222/json`). 
Always programmatically hunt down and force-kill any dangling background Google Chrome processes before attempting your run (ensuring you do not kill your own scripting process if running within Python):

```python
import subprocess, os, signal
p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
out, _ = p.communicate()
for line in out.decode("utf-8", errors="ignore").split("\n"):
    if "Google Chrome" in line and "grep" not in line and "script.py" not in line:
        parts = line.split()
        if len(parts) > 1:
            try:
                os.kill(int(parts[1]), signal.SIGKILL)
            except OSError:
                pass
```

Then, delete any dangling lock files:
```bash
rm -f "/tmp/chrome_profile_temp/SingletonLock"
rm -f "/tmp/chrome_profile_temp/SingletonSocket"
```
On macOS, Chrome can leave both a symlink lock (`SingletonLock`) and a socket file (`SingletonSocket`) in the temporary profile folder. If either of these is present, Chrome will abort silently on startup. Always programmatically remove both before starting the browser.

### Step 3: Setup a Lightweight Temporary User Data Directory
Create a temporary user data directory (e.g., `/tmp/chrome_profile_temp/Default`) and copy **only** the target profile's `Cookies` SQLite file into it. 
*By copying only the Cookies file instead of the whole profile, you bypass the default-directory security block, avoid copying gigabytes of cache, and keep the operation fast.*

```python
import os, shutil
temp_dir = "/tmp/chrome_profile_temp"
os.makedirs(f"{temp_dir}/Default", exist_ok=True)
shutil.copy(src_cookies_path, f"{temp_dir}/Default/Cookies")
```

### Step 4: Launch Chrome with Remote Debugging Headlessly
Launch a clean, headless Chrome instance pointing to your temporary data directory. Because it runs on the local machine as the same macOS user, it can automatically decrypt the copied cookies using the system's Google Chrome Keychain item:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/chrome_profile_temp" \
  --headless=new \
  --window-size=1280,1024
```

### Step 5: Connect and Automate via CDP/WebSockets
Query the local DevTools list (`http://127.0.0.1:9222/json`) to retrieve the `webSocketDebuggerUrl` of the active page tab. Connect using a WebSocket client (like python `websockets`) or the `browse` CLI, navigate to your target URL, and evaluate custom JavaScript to extract data or perform actions.

#### Direct CDP Page Navigation Bypass
If external wrapper daemons (such as the `browse` CLI daemon) crash, fail, or get killed, do not rely on them. Bypass them entirely and use direct, native CDP `Page.navigate` protocol calls over the websocket connection. This is 100% reliable, fast, and removes external dependencies:
```python
# Native CDP Navigation over websocket
payload = {
    "id": 1,
    "method": "Page.navigate",
    "params": {"url": "https://gumroad.com/settings/profile"}
}
await ws.send(json.dumps(payload))
await ws.recv()
```

#### Resilient Dynamic Form Selectors with Polling
Modern web applications (such as Gumroad and LinkedIn settings/dashboards) render forms dynamically via React/Ember, frequently employing hooks like `useId()` that generate different input/textarea IDs on each load (e.g., `:r1:-bio` vs `:r2:-bio`). Do NOT use static IDs. 
Instead, write an asynchronous polling function in JavaScript to wait for elements to render under generic tag names (`textarea`, `div[contenteditable=true]`) before executing your actions, preventing timing and lazy-load crashes:
```javascript
const waitForEl = async (selector, maxMs = 15000) => {
    const start = Date.now();
    while (Date.now() - start < maxMs) {
        const el = document.querySelector(selector);
        if (el) return el;
        await new Promise(r => setTimeout(r, 200));
    }
    return null;
};
```

#### Direct Compose URL Bypass on Protected Sites (e.g., LinkedIn)
On highly protected sites, standard click actions on action buttons (like "Message" or "Enviar mensagem") can fail due to localized button selectors, lazy rendering, or click-interception. 
*Workaround:* Extract the target user's unique profile URN from their profile page HTML using regex, then navigate the browser directly to the dedicated compose URL:
```python
# Extract URN from profile HTML
match_urn = re.search(r'profileUrn=urn%3Ali%3Afsd_profile%3A([A-Za-z0-9_-]+)', html)
if match_urn:
    urn = match_urn.group(1)
    compose_url = f"https://www.linkedin.com/messaging/compose/?profileUrn=urn:li:fsd_profile:{urn}"
    # Navigate directly to the compose URL to open a clean message panel
```

#### Automating Contenteditable Inputs in React/Ember/Draft.js
When writing text into a `contenteditable` container inside React, Draft.js, Lexical, or other complex framework-based portals:
1. **Never touch innerHTML/innerText directly:** Modifying `innerHTML` or `innerText` often throws unhandled internal exceptions inside the framework's shadow DOM/render loops (e.g., Draft.js's "Got unexpected null or undefined"), which permanently crashes the editor state and leaves the send/submit buttons disabled.
2. **Use document.execCommand first:** Focus the element, clear any selection, and run the native browser text insertion command:
   ```javascript
   el.focus();
   document.execCommand('insertText', false, text);
   ```
3. **Dispatch native CDP hardware key events:** Modern rich text editors require actual hardware-level keyboard events to trigger their state updates and enable submit buttons. Send a native key down/up event sequence (such as a Space or characters) via the CDP `Input.dispatchKeyEvent` method:
   ```python
   # Example: Sending a space character to trigger state updates
   await ws.send(json.dumps({
       "method": "Input.dispatchKeyEvent",
       "params": {"type": "keyDown", "text": " ", "unmodifiedText": " ", "key": " "}
   }))
   await ws.send(json.dumps({
       "method": "Input.dispatchKeyEvent",
       "params": {"type": "keyUp", "text": " ", "unmodifiedText": " ", "key": " "}
   }))
   ```

#### Safe Navigation and Tab Management via Chrome HTTP Endpoint
When automating across multiple URLs/prospects:
1. **Do not use a single persistent websocket connection for page navigation:** Navigating the same tab to a different domain via `Page.navigate` can destroy the page context and drop the active WebSocket connection with ping timeouts or connection resets.
2. **Open fresh tabs via HTTP administration:** Use Chrome's local HTTP API to launch a clean tab directly pointing to your target URL:
   ```python
   resp = requests.put(f"http://127.0.0.1:9222/json/new?{url}")
   tab_data = resp.json()
   ws_url = tab_data["webSocketDebuggerUrl"]
   tab_id = tab_data["id"]
   ```
3. **Connect, automate, and close:** Connect your websocket client to that fresh tab's URL, execute the automation steps, close the websocket, and then discard the tab cleanly using the HTTP close endpoint:
   ```python
   requests.get(f"http://127.0.0.1:9222/json/close/{tab_id}")
   ```
   This prevents memory leaks, prevents websocket disconnects, and keeps the user's browser completely clean.

### Step 6: Teardown & Restore Normal User Experience
Once finished, terminate your debug Chrome process, clean up `/tmp/chrome_profile_temp`, and **immediately restart Google Chrome normally** so the user's active session is restored seamlessly with zero tab or state loss:

```bash
open -a "Google Chrome"
```

---

## Special Case: LinkedIn Outreach Automation

One of the most powerful and common applications of active Chrome session reuse is LinkedIn direct outreach. Because LinkedIn employs highly advanced browser footprinting and security guards, executing headless outreach must follow a highly specialized set of mechanics.

For step-by-step code implementations, custom selectors, compose panel bypasses, and multi-lingual message templates:
- **`references/phantom-completion-and-imap-stickiness.md`**: Verification protocols for headless execution (Phantom Completion Pitfall), IMAP drafts synchronization workarounds, and partnership style guidelines.
- **`references/linkedin-outreach-automation.md`**: Complete implementation walkthrough, database check query, background zombie clean-ups, direct message composition URLs, and ProseMirror contenteditable dispatch triggers.
- **`references/reddit-and-x-rich-text-automation.md`**: Precise interaction sequences, lazy-loaded shreddit-composer hydration rules, simulated clipboard paste injections, and native CDP keypress dispatches for Reddit and X (Twitter) rich text editors.
- **`templates/pt_br_outreach_templates.md`**: Direct, authentic, multi-lingual outreach scripts and personal story taglines targeted for Brazilian/LatAm connections.
- **`references/b2b_agency_email_sourcing_and_high_ticket_pivot.md`**: Direct guides on scraping B2B agency emails and pivoting to high-ticket consulting offers when cash flow requirements are urgent.

### LatAm & Brazilian Payment Optimizations (PIX vs USD)
When automating outreach targeted at LatAm/Brazilian markets, running checkouts in USD via standard credit card platforms (like Gumroad) introduces massive friction (high card declines, international fees, and Stripe individual account compliance locks).
- **Optimization Strategy:** For LatAm targets, direct outreach connections to a localized landing page supporting **PIX** (such as via Hotmart). PIX processes instantly, dropping cash directly into local accounts. Use standard USD credit card / Stripe gateways (like Gumroad) exclusively for global or US-based prospects.

### Sincerity, Targeting, & Pacing
- **Pacing Caps:** Restrict automated message sends to a maximum of **10-15 messages per day** with 5-10 second typing buffers to avoid triggering LinkedIn's automation velocity rules. Prepare larger batches as markdown copy-paste panels for manual delivery (The Semi-Automated Campaign Pipeline).
- **Executive Framing:** Do not pitch low-ticket products to CEOs, executives, or startup founders. Pitch high-value premium bundles instead. Keep low-ticket specialized packs focused on daily executioners (content writers, SEO specialists, developers).
- **Be Brutally Honest:** Craft messages with high sincerity. Genuine, transparent personal stories and precise product taglines build unmatched trust on professional networks.

---

## Pitfalls & Mitigations

- **CDP Connection Refused:** Chrome may still be in the process of closing or the profile lock is not fully released. Add a loop that polls `pgrep` and waits up to 15 seconds before starting the debug instance.
- **Dangling SingletonLock in Temporary Directory:** If a previous headless session crashed or was aborted, a `SingletonLock` symlink can persist inside the temporary directory (e.g., `/tmp/chrome_profile_temp/SingletonLock`). This will silently prevent your headless Chrome debugger from launching on subsequent runs, causing CDP connection timeouts. Always recursively delete the temporary directory or explicitly remove `/tmp/chrome_profile_temp/SingletonLock` (and `/tmp/chrome_profile_temp/SingletonLock` equivalent locks) before copying cookies and starting Chrome.
- **`browse` CLI fails to launch:** When executing from sandboxed scripts, the `browse` binary might not be in the execution `PATH`. Always resolve and use the absolute path of `browse` (e.g., `/Users/gabrielpaiva/.nvm/versions/node/v22.22.3/bin/browse`).
- **Dynamic CSS Classes on Protected Sites:** Modern platforms (like LinkedIn) use dynamically generated or localized class names (e.g., "Message" vs "Enviar mensagem" in Portuguese). Write robust JS selectors that inspect `.innerText` case-insensitively or use regex patterns on links containing target paths (e.g., `a[href*="/in/"]` for profile links).
- **Infinite Session Lock loop:** Always wrap your automation code in a `try...finally` block so that no matter what fails, Chrome is terminated cleanly and restarted normally for the user.
- ADHD Pace & Sincere Tone Preferences (Critical): The user has late-diagnosed ADHD and gets overwhelmed by aggressive "YOLO" execution, corporate buzzwords, and verbose narration. Downshift the pace when requested ("slow down", "relax" = STOP immediately). Always present steps clearly first, act second, and never utilize techbro/salesman hype (e.g., alavancar, destravar, leverage, 10x, synergies, game-changer). NEVER suggest rest, sleep, or dictate how to spend his personal/family time. Focus strictly on system craft, absolute transparency, and direct actions. Do one thing at a time with clear, sequential steps.

- **Truth Verification Protocol:** After any significant browser automation claim (e.g., "posted message", "filled form", "submitted data"), verify the state change through `browser_vision()` analysis or session log audit. Never fabricate completion reports. Match every claimed action with actual tool execution logs.
