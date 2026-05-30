# Reddit & X (Twitter) Rich Text Editor Automation (Lexical / Draft.js)

Automating rich text editors (RTEs) like Facebook's Lexical and Draft.js on highly protected platforms (Reddit, X) using headless/headful Chrome CDP presents major challenges. Traditional DOM manipulation (setting `innerText`, `innerHTML` or sending simple events) either crashes the framework or leaves the "Submit" buttons disabled.

Below are the exact, verified, battle-tested workarounds for both platforms.

---

## 🎯 Modern X (Twitter) — Draft.js/Lexical

X uses Draft.js/Lexical. Directly setting `innerHTML` or `innerText` on the text box causes an uncaught internal React exception, which permanently freezes the composer state and keeps the "Reply" button disabled.

### The Solution: Native `execCommand` + CDP Keypress
1. **Focus the element** using normal JS focus/click:
   ```javascript
   const el = document.querySelector('[data-testid="tweetTextarea_0"]');
   el.focus();
   el.click();
   ```
2. **Natively insert the text** using the browser's `execCommand` (which is intercepted correctly by Draft.js/React):
   ```javascript
   document.execCommand('insertText', false, "Your pitch message here...");
   ```
3. **Trigger state update via hardware keypress:** To force Draft.js to re-evaluate and enable the reply button `[data-testid="tweetButtonInline"]`, you must dispatch a physical, native keystroke (e.g. a Space or Backspace) using the Chrome DevTools Protocol `Input.dispatchKeyEvent` method:
   ```python
   # Send raw keydown for space (virtual keycode 32)
   await ws.send(json.dumps({
       "id": 100,
       "method": "Input.dispatchKeyEvent",
       "params": {
           "type": "rawKeyDown",
           "text": " ",
           "unmodifiedText": " ",
           "key": " ",
           "windowsVirtualKeyCode": 32
       }
   }))
   await ws.recv()
   # Send keyup
   await ws.send(json.dumps({
       "id": 101,
       "method": "Input.dispatchKeyEvent",
       "params": {
           "type": "keyUp",
           "text": " ",
           "unmodifiedText": " ",
           "key": " ",
           "windowsVirtualKeyCode": 32
       }
   }))
   await ws.recv()
   ```
4. **Submit:** Click the reply button `document.querySelector('[data-testid="tweetButtonInline"]').click()`.

---

## 🤖 Modern Reddit — Shreddit Composer (Lexical)

Reddit uses Web Components (`<shreddit-composer>`) and Lexical. The actual rich text input slot `div[slot="rte"]` is **lazy-loaded** and does not exist in the DOM initially on page load. Furthermore, direct text typing can be completely blocked by Lexical's internal selection validations.

### The Solution: Click to Hydrate + Simulated Paste Event
1. **Click the composer shell** to trigger lazy-loading and element hydration:
   ```javascript
   const comp = document.querySelector('shreddit-composer');
   comp.focus();
   comp.click();
   ```
2. **Wait for hydration:** Sleep for `1.5` seconds to allow the web component to render `div[slot="rte"]`.
3. **Focus the newly-mounted editor:**
   ```javascript
   const el = document.querySelector('div[slot="rte"]');
   el.focus();
   ```
4. **Clear existing content:** Set `el.innerHTML = '<p class="first:mt-0 last:mb-0"><br></p>';` to reset the Lexical tree.
5. **Simulate Paste Event:** Create a `ClipboardEvent('paste')` carrying a mocked `DataTransfer` object. Lexical intercepts paste events perfectly, parses the plaintext, and updates its internal React state automatically:
   ```javascript
   const dt = new DataTransfer();
   dt.setData('text/plain', "Your high-value outreach message here...");
   
   const evt = new ClipboardEvent('paste', {
       bubbles: true,
       cancelable: true,
       clipboardData: dt
   });
   el.dispatchEvent(evt);
   ```
6. **Wait for state commit:** Sleep for `1.0` seconds to let Lexical process the document data and enable the submission triggers.
7. **Submit:** Click the slotted submit button `document.querySelector('button[slot="submit-button"]').click()`.
