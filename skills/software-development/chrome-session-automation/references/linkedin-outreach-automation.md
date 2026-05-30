---
name: linkedin-automation
description: "Automate LinkedIn direct messaging and outreach safely by reusing active logged-in Chrome session cookies via headless CDP."
version: 1.0.0
author: Hermes
category: social-media
---

# LinkedIn Automation

LinkedIn aggressively blocks standard automated browsers (like clean Playwright/Selenium instances) and new login attempts from automated scripts. To automate direct outreach safely without triggering bot detection, CAPTCHAs, or account restrictions, you must reuse the user's active, logged-in Google Chrome session cookies on their local machine.

This skill provides a complete, robust, and zero-touch method to copy the logged-in Chrome profile cookies, launch an isolated headless Chrome instance with remote debugging enabled, navigate directly to messaging compose interfaces, and automate typing and sending messages safely.

## Prerequisites

- macOS (or Linux/Windows with adjusted paths)
- Google Chrome installed on the host
- Python 3.10+ with `websockets` library installed

---

## Step-by-Step Workflow

### Step 1: Locating the Active Profile Cookies
Google Chrome on macOS stores profile databases in `~/Library/Application Support/Google/Chrome/`.
- Standard profile: `Default`
- Multi-profile setups: `Profile 1`, `Profile 2`, `Profile 3`, etc.

To locate the active profile containing LinkedIn cookies, run a SQLite check on the `Cookies` database:
```python
import sqlite3
import os

# Check both default and numbered profiles
profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4"]
for p in profiles:
    path = f"/Users/{os.getlogin()}/Library/Application Support/Google/Chrome/{p}/Cookies"
    if os.path.exists(path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key FROM cookies WHERE host_key LIKE '%linkedin%'")
        rows = cursor.fetchall()
        if rows:
            print(f"Active Profile Found: {p} ({len(rows)} LinkedIn cookies)")
```

### Step 2: Preparing the Isolated Temporary Profile
Chrome blocks remote debugging (`--remote-debugging-port`) when pointing directly to the active standard user data directory. You must copy the `Cookies` database of the active profile to a temporary profile directory to launch safely.

```python
import shutil
import os

temp_dir = "/tmp/chrome_profile_temp"
os.makedirs(f"{temp_dir}/Default", exist_ok=True)

src_cookies = f"/Users/{os.getlogin()}/Library/Application Support/Google/Chrome/{active_profile}/Cookies"
dest_cookies = f"{temp_dir}/Default/Cookies"
shutil.copy(src_cookies, dest_cookies)
```

### Step 3: Closing Running Chrome and Launching Debug Chrome
On macOS, Google Chrome locks the cookies database when running. You must quit the running instance gracefully, launch the debug headless Chrome, perform the scrape/send, and then restore the user's browser window seamlessly so they do not lose their active tabs.

**CRITICAL CRASH MITIGATION (Zombie Chrome Clean-Up):** If Chrome was terminated abruptly or a previous script crashed mid-run, background Google Chrome zombie processes can persist. These background processes will hold locks on your `--remote-debugging-port` and profile folder, causing new instances to fail or return empty debugger targets lists (`[]`). You MUST actively find and cleanly terminate any leftover processes before launch:

```python
import subprocess
import os
import signal
import time

# Terminate normal running app
subprocess.run(["osascript", "-e", 'quit application "Google Chrome"'])
time.sleep(3)

# Search for and SIGKILL background zombie Chrome processes
p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.decode("utf-8", errors="ignore").split("\n"):
    if "Google Chrome" in line and "grep" not in line and "script.py" not in line:
        parts = line.split()
        if len(parts) > 1:
            pid = int(parts[1])
            try:
                os.kill(pid, signal.SIGKILL)
            except Exception:
                pass
time.sleep(2)

# Remove any dangling lock files
lock_paths = [
    f"/Users/{os.getlogin()}/Library/Application Support/Google/Chrome/SingletonLock",
    f"{temp_dir}/SingletonLock"
]
for lp in lock_paths:
    if os.path.exists(lp):
        try:
            if os.path.islink(lp) or os.path.exists(lp):
                os.unlink(lp) if os.path.islink(lp) else os.remove(lp)
        except Exception:
            pass

# Launch headless debug Chrome
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
proc = subprocess.Popen([
    chrome_path,
    "--remote-debugging-port=9222",
    f"--user-data-dir={temp_dir}",
    "--window-size=1280,1024",
    "--headless=new"
])
time.sleep(4)
```

### Step 4: Connecting via CDP and Direct Messaging Compose
Navigating directly to profile pages and clicking the "Message" button can fail due to complex event listeners or dynamic layout translation (e.g. Portuguese "Enviar mensagem" vs English "Message"). 

Instead, extract the recipient's `profileUrn` from their profile page HTML, and navigate **directly** to the messaging compose URL:
`https://www.linkedin.com/messaging/compose/?profileUrn=urn:li:fsd_profile:{URN}`

```python
import urllib.request
import json
import websockets

# Get active tab websocket url
with urllib.request.urlopen("http://127.0.0.1:9222/json") as resp:
    targets = json.loads(resp.read().decode())
ws_url = [t.get("webSocketDebuggerUrl") for t in targets if t.get("type") == "page"][0]

async with websockets.connect(ws_url) as ws:
    # Navigate to compose
    payload = {
        "id": 1,
        "method": "Page.navigate",
        "params": {"url": f"https://www.linkedin.com/messaging/compose/?profileUrn=urn:li:fsd_profile:{urn}"}
    }
    await ws.send(json.dumps(payload))
    await ws.recv()
    time.sleep(8) # Wait for compose workspace to mount
```

### Step 5: Injecting Message and Sending
LinkedIn's compose area is a React/Ember `contenteditable` div. You must set its `innerHTML` and dispatch the `input` event so the frontend state updates and enables the Send button before clicking it.

```python
    message_text = "Your personalized outreach text here..."
    
    js_code = \"\"\"
    ((msg) => {
        const el = document.querySelector('div[contenteditable=true], .msg-form__contenteditable, textarea');
        if (!el) return { success: false, error: "textbox_not_found" };
        
        el.innerHTML = "<p>" + msg.replace(/\\\\n/g, "<br>") + "</p>";
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
        
        const sendBtn = document.querySelector('.msg-form__send-button, button[type=submit]');
        if (!sendBtn) return { success: false, error: "send_button_not_found" };
        
        sendBtn.disabled = false;
        sendBtn.click();
        return { success: true };
    })("%s")
    \"\"\" % message_text.replace('"', '\\"').replace('\n', '\\n')
    
    payload = {
        "id": 2,
        "method": "Runtime.evaluate",
        "params": {
            "expression": js_code,
            "returnByValue": True
        }
    }
    await ws.send(json.dumps(payload))
    response = await ws.recv()
```

### Step 6: Restoring Normal Chrome
Close the debugging process and relaunch normal Chrome so the user's active session is restored seamlessly with all their tabs.

```python
proc.terminate()
proc.wait()
subprocess.Popen([chrome_path])
```

---

## Pitfalls

- **Do NOT attempt to use a default profile directly for CDP:** Google Chrome blocks remote debugging on the default user data directory. You will get the error: "DevTools remote debugging requires a non-default data directory. Specify this using --user-data-dir." Always copy cookies to a temporary directory.
- **Do NOT miss the 'input' event dispatch:** Simply changing `.innerHTML` or `.innerText` of the `contenteditable` box will NOT update LinkedIn's react/ember state. The "Send" button will remain disabled. You must dispatch `new Event('input', { bubbles: true })`!
- **Zombie Chrome Process Port Locks:** Headless Chrome instances that crash or fail to close cleanly linger as background zombie processes. This locks port `9222` and the temporary profile directory, resulting in empty targets lists (`[]`) on subsequent runs. Always kill background Chrome processes before launching a new debugging instance.
- **Dangling SingletonLock:** If Google Chrome was not terminated cleanly, the `SingletonLock` symlink can persist in either the standard host profile directory or your temporary profile directory (e.g., `/tmp/chrome_profile_temp/SingletonLock`). These leftover lock files will silently block headless Chrome from launching, resulting in empty target lists (`[]`) or connection refusals. Always ensure you delete both the standard lock and any temporary lock files before initiating headless debug runs.
- **Pacing limit:** To prevent LinkedIn from flagging your account for automated activity, limit automated sends to **maximum 10-15 messages per day** with realistic delay buffers (5-10 seconds between actions). Prepare the remaining outreach templates as pre-drafted "ready-to-send" markdown tables for manual copying and pasting.
- **The Phantom Completion Pitfall & Delivery Verification:** Automated browser scripts can silently fail (or only partially complete) while still returning a success exit code or writing "sent" to output tracking reports. Always run a programmatic validation by fetching the active messaging list (e.g., visiting `https://www.linkedin.com/messaging/` and extracting the body text) to verify that a thread with the recipient exists and contains the outreach message. Do not declare a message sent without verifying its delivery in the active inbox.
- **Flexible Snapshot Ref Extraction via Browse CLI:** LinkedIn's dynamic DOM frequently changes class names and button structures. When driving actions using the `browse` CLI, avoid hardcoded element selectors or index paths. Instead, capture a compact snapshot (`browse snapshot --compact`), then parse the text using flexible regex patterns (e.g., `r'\[([\d-]+)\]\s*(?:link|button):\s*Enviar mensagem'` for Portuguese or `r'\[([\d-]+)\]\s*(?:link|button):\s*Message'` for English) to dynamically extract the active ref (such as `@<ref_id>`) for reliable clicks.
- **Geographical Payment & Platform Optimization (PIX/Hotmart vs Stripe/Gumroad):**
  - **LatAm/Brazil:** International credit card checkouts in USD (like Gumroad) create severe purchasing friction due to local card limitations, international transaction fees, and high declination rates. More critically, Stripe payouts to Brazilian accounts (CPF/Individual Tax ID) can trigger multi-day compliance verification locks. For Brazil-targeted outreach, always direct connections to a localized landing page (like Netlify) integrated with a gateway (like Hotmart) that supports **PIX**. PIX transactions resolve instantly, placing immediate cash directly into the user's local account.
  - **Global/US:** Recommending credit card and PayPal-based checkout flows (Gumroad) is standard and remains highly effective for international connections.
- **Localization & Copy Strategy:** For international or localized audiences (such as Brazilian connections), always translate messages to their native language (e.g., Portuguese) to build a direct and authentic relationship. Avoid generic marketing hype or buzzwords (like 'leverage', 'unlock', '10x', 'synergy', 'alavancar', 'destravar'). Write like a craftsman, prioritizing brutal honesty, clean text formatting, and direct links without forced click-through loops or sales funnels. See the fully translated PT-BR personal story and product taglines template at `templates/pt_br_outreach_templates.md` for a known-good example.
- **Outreach Matching & Framing Strategy:**
  - **Do NOT pitch low-ticket products to high-ticket prospects:** Executives, CEOs, and busy startup founders value their time above minor price differences. Pitch them the comprehensive high-tier bundle (e.g., *The Full Arsenal* at $29) rather than individual $7-$9 kits.
  - **Focus low-ticket packs on creators and executioners:** Individual specialized kits (such as *Content Empire* or *SEO Domination* at $9) are highly relevant for content writers, developers, and technical executors who handle daily content pipelines.
  - **Lead with Sincerity and Transparency:** Include the full story and listing transparency (e.g., listing all individual packs in the template). Unfiltered, raw truth (e.g., physicist + photographer background, solo dad struggle, and exact medication costs) connects far more deeply than "softened" or corporate-style messages. Keep the story unfiltered and let the value speak for itself.

## 📁 Linked References & Support Files

- **`references/b2b_agency_email_sourcing_and_high_ticket_pivot.md`**: Guide for programmatic search engine scraping, crawling local domains to harvest verified business emails, and pivoting from low-ticket to high-ticket positioning (such as a systems operational/Airtable audit) during urgent cash flow requirements.

