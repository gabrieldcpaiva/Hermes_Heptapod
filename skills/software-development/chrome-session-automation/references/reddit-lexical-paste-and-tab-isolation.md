# Reddit & Lexical Rich Text Editor Automation Walkthrough

This reference detail outlines the precise mechanics for automating rich-text posting on modern Reddit (Shreddit) and other Lexical-based web platforms using a local Chrome remote-debugging session, bypassing shadow DOM boundaries, lazy-loading hydration lag, and Lexical virtual DOM event blocks.

---

## 1. The Interaction Lifecycle of Modern Reddit (Shreddit)

Modern Reddit relies heavily on custom Web Components (`<shreddit-composer>`, `<reddit-rte>`) and Facebook's Lexical rich text framework. The editor elements do not exist in the DOM on initial page load.

### Step A: The Lazy-Loading Hydration Step
The rich-text input slot (`div[slot="rte"][contenteditable="true"]`) is lazy-loaded. If you attempt to select it immediately, it will fail.
You must programmatically click and focus the parent `<shreddit-composer>` shell first. This triggers the component to hydrate and dynamically appends the `div[slot="rte"]` slot to the light DOM.

```javascript
const comp = document.querySelector('shreddit-composer');
if (comp) {
    comp.focus();
    comp.click();
}
// MUST wait at least 1.5 seconds for Lexical components to mount
```

### Step B: The Clipboard Paste Bypass
In Lexical/Draft.js, directly modifying `innerHTML` or executing native `document.execCommand('insertText')` on an inactive selection state will result in Lexical calling `preventDefault()`, discarding the text, or throwing critical React render errors.

To bypass this safely, simulate a native clipboard paste event by constructing an artificial `DataTransfer` object and dispatching a `paste` event directly on the focused `contenteditable` container. Lexical intercepts this native-like gesture, parses the plain text, updates its virtual state, and automatically enables the "Submit" or "Comment" button.

```javascript
const el = document.querySelector('div[slot="rte"]');
el.focus();

// Clear placeholder or existing empty paragraphs safely
el.innerHTML = '<p class="first:mt-0 last:mb-0"><br></p>';

const dt = new DataTransfer();
dt.setData('text/plain', "Your high-value outreach or comment text goes here.");

const evt = new ClipboardEvent('paste', {
    bubbles: true,
    cancelable: true,
    clipboardData: dt
});
el.dispatchEvent(evt);

// Wait 1.0 second for Lexical to register state changes and render
```

### Step C: Triggering the Submit
Once the text is pasted, select and click the slotted submit button directly:

```javascript
const btn = document.querySelector('button[slot="submit-button"]');
if (btn) {
    btn.click();
}
```

---

## 2. Multi-Tab Session Isolation Pattern

Running multiple page navigations sequentially over a single websocket debugger connection can cause keepalive ping timeouts or connection losses when a page unloads or redirects.

To make session automation 100% self-healing and robust, implement the **Multi-Tab Isolation Pattern** via Chrome's HTTP administration endpoints:

1. **Spawn an Isolated Tab:**
   Send a PUT request to `http://127.0.0.1:9222/json/new?https://target-url.com` to open a clean tab pointing directly to the target URL.
2. **Connect to the Tab Debugger:**
   Read the `webSocketDebuggerUrl` and `id` (tab ID) from the HTTP response. Establish a dedicated websocket connection for that tab alone.
3. **Execute the Automation:**
   Interact, focus, paste, and click.
4. **Close and Clean Up:**
   Once the transaction is complete, disconnect the websocket and close the tab using a GET request to `http://127.0.0.1:9222/json/close/{tab_id}`.

This pattern isolates page contexts, prevents memory leaks, and ensures that navigation drops never crash the orchestration runtime.
