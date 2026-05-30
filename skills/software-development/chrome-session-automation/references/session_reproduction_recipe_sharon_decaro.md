# LinkedIn Messaging Session Details — Sharon DeCaro Profile Case Study

This reference file logs the real-world DOM structure, classes, and CDP-handling parameters discovered and verified during the live campaign session on May 27, 2026.

---

## Verified LinkedIn Profile Page Structure (Profile 2)

- **Language:** Portuguese (Brazil)
- **Profile Page URL:** `https://www.linkedin.com/in/sharondecaro/`
- **Active Connection URN Location:** Extracted from the `profileUrn` query parameter in the page source:
  `profileUrn=urn%3Ali%3Afsd_profile%3AACoAAAFXzQYBZPsyWysekWP8uvdjGovWPEC_ojQ`

---

## Messaging Compose Page DOM Layout

- **URL navigated directly:**
  `https://www.linkedin.com/messaging/compose/?profileUrn=urn%3Ali%3Afsd_profile%3AACoAAAFXzQYBZPsyWysekWP8uvdjGovWPEC_ojQ`

- **Textarea Container (contenteditable):**
  - **Tag:** `DIV`
  - **Dynamic Classes:** `msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate`
  - **Role Attribute:** `textbox`
  - **Aria Label:** `Write a message…` (or `Escreva uma mensagem…` depending on language)

- **Submit/Send Button:**
  - **Tag:** `BUTTON`
  - **Dynamic Classes:** `msg-form__send-button artdeco-button artdeco-button--1`
  - **Text:** `Send` (or `Enviar`)
  - **Disabled Attribute:** Starts as `disabled=""` (must be updated via `input` event trigger on the contenteditable container or programmatically set `disabled = false`).

---

## Exact Executed JS Payload

```javascript
((msg) => {
    const el = document.querySelector('div[contenteditable=true], .msg-form__contenteditable, textarea');
    if (!el) return { success: false, error: "textbox_not_found" };
    
    // Inject and format text
    el.innerHTML = "<p>" + msg.replace(/\\n/g, "<br>") + "</p>";
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    
    const sendBtn = document.querySelector('.msg-form__send-button, button[type=submit]');
    if (!sendBtn) return { success: false, error: "send_button_not_found" };
    
    sendBtn.disabled = false;
    sendBtn.click();
    return { success: true };
})("Your Escaped Message Text Here...")
```
