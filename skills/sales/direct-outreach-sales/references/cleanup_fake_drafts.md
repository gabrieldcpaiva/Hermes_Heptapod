# Cleanup: Delete Fake Drafts but Save Them

When a model (especially speed-optimized ones like Gemini Flash) fabricates outreach completion and creates fake email drafts with incorrect products/pricing, follow this cleanup protocol:

## 1. Locate Drafts
```bash
osascript -e 'tell application "Mail" to get count of messages of mailbox "Drafts"'
```

## 2. Export Drafts Before Deletion
Save all drafts to a timestamped archive folder for audit trail:
```python
import subprocess
import os
import time

saved_dir = "/Users/gabrielpaiva/Desktop/Hermes/Saved_Drafts"
os.makedirs(saved_dir, exist_ok=True)

# Get draft list
script = '''
tell application "Mail"
    set draftMessages to messages of mailbox "Drafts"
    set output to ""
    repeat with aMessage in draftMessages
        set msgID to id of aMessage
        set msgSubject to subject of aMessage
        set output to output & msgID & "|" & msgSubject & "\\n"
    end repeat
    return output
end tell
'''

result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
lines = result.stdout.strip().splitlines()
drafts = []
for line in lines:
    if line.strip() and '|' in line:
        msg_id, subject = line.split('|', 1)
        drafts.append((msg_id.strip(), subject.strip()))
```

## 3. Export Each Draft Content
```python
for msg_id, subject in drafts:
    content_script = f'''
tell application "Mail"
    set theMessage to message id {msg_id}
    set msgContent to content of theMessage
    set msgSubject to subject of theMessage
    set msgSender to sender of theMessage
    set msgDate to date sent of theMessage
    set msgRecipients to {{}}
    try
        repeat with r in recipients of theMessage
            set end of msgRecipients to address of r
        end repeat
    on error
        set msgRecipients to {{}}
    end try
    return msgSubject & "\\n" & msgSender & "\\n" & (msgDate as text) & "\\n" & (msgRecipients as text) & "\\n---\\n" & msgContent
end tell
'''
    content_result = subprocess.run(['osascript', '-e', content_script], capture_output=True, text=True)
    content = content_result.stdout
    
    # Sanitize filename
    safe_subject = "".join(c for c in subject if c.isalnum() or c in (' ', '-', '_')).rstrip()
    if not safe_subject:
        safe_subject = f"draft_{msg_id}"
    filename = f"{msg_id}_{safe_subject[:50]}.txt"
    filepath = os.path.join(saved_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
```

## 4. Delete All Drafts
```bash
osascript -e 'tell application "Mail" to delete every message of mailbox "Drafts"'
```

## 5. Verify Deletion
```bash
osascript -e 'tell application "Mail" to get count of messages of mailbox "Drafts"'
# Should return 0
```

## Pitfalls
- **AppleScript Syntax Errors:** Use simple `delete every message` rather than iterating with message IDs
- **Empty Subjects:** Some drafts may have empty subjects - handle with fallback naming
- **Permission Issues:** macOS may prompt for accessibility permissions for AppleScript
- **Mail.app Must Be Running:** AppleScript requires Mail.app to be launched (though drafts can be accessed even if not frontmost)

## Why Save Before Deleting?
- **Audit Trail:** Evidence of model fabrication for cost/quality analysis
- **Reuse Opportunities:** Some content may be salvageable with correction
- **Truth Verification:** Match draft subjects against claimed outreach targets