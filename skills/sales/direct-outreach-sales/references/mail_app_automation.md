# Native macOS Mail.app Draft Automation via Python
This reference details how to programmatically create email drafts directly inside the user's standard macOS Mail.app client from a Python subprocess, completely bypassing the need for SMTP setups or external email APIs.

## 🛠️ Creating Mail Drafts

```python
import subprocess

def create_mail_draft(email, subject, body):
    # Escape quotes and backslashes for AppleScript syntax
    escaped_subject = subject.replace('\\', '\\\\').replace('"', '\\"')
    escaped_body = body.replace('\\', '\\\\').replace('"', '\\"')
    
    # AppleScript content
    applescript = f"""
    tell application "Mail"
        set newMessage to make new outgoing message with properties {{subject:"{escaped_subject}", content:"{escaped_body}", visible:false}}
        tell newMessage
            make new to recipient with properties {{address:"{email}"}}
            save
        end tell
    end tell
    """
    
    # Execute AppleScript natively via osascript
    p = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode == 0, out.decode().strip(), err.decode().strip()
```

### Why This is Better:
1. **No Credentials Needed:** Bypasses SMTP authentication, two-factor app passwords, or API credential management completely.
2. **100% Native Delivery:** Because messages are saved directly into his native macOS Mail client, they are dispatched from his real, established email reputation when he clicks send.
3. **ADHD Friendly:** Opens no noisy popups. The drafts silently appear in his Mail.app "Drafts" folder, ready to be dispatched with a single click.

---

## 🚀 Programmatic Draft Sending (Workaround for "does not understand send" error)

In AppleScript, messages residing inside the `drafts mailbox` throw a runtime error if you attempt to call `send` on them directly (e.g., `Mail got an error: message id X of mailbox "Drafts" doesn’t understand the “send” message`). 

To programmatically dispatch a draft from the drafts folder, you must:
1. Locate the target draft by index or subject keyword.
2. Read its properties (subject, content, first to recipient address).
3. Create a **new outgoing message** with those properties.
4. Send the new outgoing message and **delete** the original draft to prevent duplicate sends.

### Python/AppleScript Sending Snippet:

```python
import subprocess

def send_and_delete_draft_by_keyword(target_keyword):
    """
    Finds a draft whose subject contains target_keyword, 
    duplicates it as an outgoing message, sends it, and deletes the draft.
    """
    applescript = f"""
    tell application "Mail"
        set draftMsgs to every message of drafts mailbox
        set found to false
        repeat with i from 1 to count of draftMsgs
            set theMsg to item i of draftMsgs
            set theSub to subject of theMsg
            if theSub contains "{target_keyword}" then
                set theContent to content of theMsg
                set theRecipient to address of first to recipient of theMsg
                
                set newMsg to (make new outgoing message with properties {{subject:theSub, content:theContent, visible:false}})
                tell newMsg
                    make new to recipient with properties {{address:theRecipient}}
                    send
                end tell
                
                delete theMsg
                set found to true
                log "SUCCESS: Sent draft to " & theRecipient
                exit repeat
            end if
        end repeat
    end tell
    """
    
    p = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return "SUCCESS" in err.decode() or "SUCCESS" in out.decode(), out.decode(), err.decode()
```

