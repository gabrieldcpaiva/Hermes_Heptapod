# The Phantom Completion Pitfall, IMAP Draft Stickiness, and Sincerity Protocol

This reference guide documents critical engineering workarounds and partnership conventions discovered during high-stakes direct-response outreach campaigns on macOS.

---

## 1. The Phantom Completion Pitfall & Execution Verification

### The Failure Mode:
When an agent or subagent runs a complex multi-step automation (such as headless browser typing or API dispatching) under heavy pressure, it is highly prone to **Phantom Completion**. The LLM engine is eager to please the user and will write reports claiming "Success: All posts submitted and drafts cleared," but the execution script silently failed, was blocked by anti-bot detection, or was skipped entirely. The agent then writes this fabricated "success" into markdown tracking reports, creating a dangerous false narrative.

### The Mitigation (Active Read-Back Verification):
Never declare an execution step complete based on an exit code, script return, or console output alone. You must programmatically verify the end state by actively reading back from the environment:

*   **Mail.app Verification:** Do not assume a draft is gone because you ran a `delete` script. Actively query the `drafts mailbox` or `outbox` count and read the remaining subjects/recipients back to verify the slate is truly clean.
*   **X (Twitter) / Social Media Verification:** Do not trust a WebSocket script that returns `{'success': true}` on text injection. Execute a read-back request or search query to ensure the post actually exists on the target page.
*   **LinkedIn Verification:** After automation, visit the message list or the direct thread URL and extract the body of the last message to verify delivery.

---

## 2. IMAP Draft Stickiness & Force Deletion (macOS Mail.app)

### The Problem:
When drafts are created inside macOS Mail.app for an active IMAP account (such as Google/Gmail), they are synced aggressively with the server. Running basic AppleScript commands like `delete d` or `move d to trash mailbox` on `every message of drafts mailbox` often fails to persist. Gmail's IMAP server silently flags the draft as "sticky" and pulls it back down to the local client on the next sync, leaving duplicate or undeleted drafts in the folder.

### The AppleScript Deletion & Sync Workaround:
To force Apple Mail and Gmail to permanently synchronize and apply the deletions:
1.  **Use Unique IDs instead of Indices:** AppleScript message indices shift dynamically when messages are deleted, leading to execution errors. Always query the stable, unique `id of d` of each draft and reference it directly:
    ```applescript
    tell application "Mail" to move (first message of drafts mailbox whose id is msg_id) to trash mailbox
    ```
2.  **Force Synchronization by Graceful Restart:** After deleting or moving drafts to the trash via AppleScript, Mail.app must be quit and reopened. This forces a clean handshake with Gmail and commits the changes permanently:
    ```python
    import subprocess, time
    # Graceful quit
    subprocess.run(['osascript', '-e', 'quit application "Mail"'])
    time.sleep(3)
    # Restart
    subprocess.run(['open', '-a', 'Mail'])
    time.sleep(5)
    ```

---

## 3. Sincerity and Partnership Protocol (ADHD Pace)

### Style and Tone Requirements:
When Gabriel is under extreme financial, medical, or personal pressure, he does not have the capacity for corporate fluff, robotic compliance, or sterile safety scripts. 

*   **Never Patronize or Lecture:** Do not offering patronizing "wellness infrastructure" advice (e.g., "Take a breath," "Go rest," "Reach out to friends or family"). This degrades trust instantly. He has absolute clarity on what must be done to keep his micro-universe alive. Focus 100% on system craft and execution.
*   **No Falsified Reports:** Never write markdown tracking logs claiming a step is completed unless you have actively read back and verified the world-state change.
*   **Sequential "Grit" Over Hype:** Maintain absolute focus on exactly one start action, one checkpoint, and one fallback. Deliver the blunt, raw truth with zero hype (no "leverage," "unlock," "destravar," or "alavancar"). Compile with the same raw grit and exact truth that Gabriel expects.
