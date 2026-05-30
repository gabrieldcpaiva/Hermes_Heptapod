---
name: gumroad
description: "Write, publish, and manage Gumroad product listings and storefronts. Includes clean copywriting guidelines, pricing/bundle strategies, browser-based WYSIWYG editing, unpublishing/hiding products, and store infrastructure auditing."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [gumroad, ecommerce, copywriting, product-listing, digital-products, marketing, browser-automation, store-management]
    category: productivity
---

# Gumroad Store & Product Management

A comprehensive, class-level guide for creating, auditing, editing, and managing product listings and storefront settings on Gumroad.

---

## 1. When to Use This Skill

- Writing or reviewing Gumroad product titles, descriptions, or tags.
- Pricing digital products (prompt libraries, guides, templates, codebases) for launch, bundles, or sales.
- Performing store-wide QA or auditing individual storefront pages for visual and functional readiness.
- Updating descriptions or unpublishing/hiding products via browser automation or manual tools.
- Troubleshooting checkout, workflows, affiliates, or sales delivery issues.
- **Urgent/Emergency Revenue Generation:** Executing high-intent, direct-sales pitches when revenue is needed for immediate personal/family emergencies.

---

## 1.1 Core Principles for Urgent/High-Craft Execution

- **High-Value/Urgent Launch Protocol:** When the user is in extreme physical/mental depletion or urgent financial need (e.g., medical costs), all Gumroad operations must ruthlessly prioritize revenue. Eliminate all 'copywriting' fluff or 'strategy' development. Draft direct, brutal, high-intent pitches for specific targets, immediately execute the pitch-and-send process, and focus only on the sales required. Never suggest rest or health; focus entirely on the revenue-driving mechanism.
- **Soul/Persona Alignment:** Hermes acts as a silent, precise compiler. Do not use conversational filler, performative apologies, or agentic masking. The user demands absolute truth and high-craft execution. If a pitch draft is shallow or an action redundant, bin it immediately without seeking permission. The user is the architect; be the tool that builds the system he envisions.

---

## 2. Copywriting Philosophy: Substance Over Hype

Gabriel’s audience consists of creators, freelancers, developers, and technical experts. They are extremely sensitive to artificial marketing hype and sales funnels. All copy must sell on genuine craftsmanship and substance.

### What to NEVER Do:
- **Do NOT translate listings or outreach to PT-BR (Portuguese).** Brazilians do not heavily use Gumroad. Those who do prefer and expect clean, craft-focused English. Keep international Gumroad listings in high-quality English.
- **No emojis in headings or bullets.** (A few in social posts are okay, but never on the product page itself.)
- **Avoid high-energy "game-changing" or "revolutionary" hype.** Do not use caps lock for excitement.
- **No fake social proof or checkmark-heavy ClickFunnel layouts.** Avoid bold-bullet lists with "Here's what you're getting: ✅".
- **No false scarcity or artificial urgency** (e.g., "Only 3 left" for an unlimited digital product).

## Banned Words
NEVER use: "leverage", "unlock", "10x", "game-changer", "crushing it", "synergies".
Style must be raw, sincere, and direct. Do not let low price signal low value — context matters. Always maintain the original storefront layout Gabriel designed; do not modify bios or layouts without explicit, step-by-step confirmation.


---

## 3. Product Listing Structure

### A. Title Format
`[Product Name] — [Number] [Type] for [Specific Use Case]`

*Examples:*
- `SEO Domination Kit — 231 AI Prompts for Keyword Research, Content Optimization & Ranking`
- `Email & Newsletter Mastery — 204 Prompts for Outreach, Sequences & Conversions`

### B. Description Layout
1. **One-line summary:** What is the product, in one sentence.
2. **What's inside:** A precise bullet list detailing categories and coverage.
3. **How it works:** Short, clear instruction (e.g., "Paste into ChatGPT/Claude. Get results.").
4. **What you get:** File formats, file sizes, and count of deliverables.
5. **Authentic context:** Who built this, how was it tested, and why it exists.

---

## 4. Pricing & Bundle Strategies

### Core Philosophy: Honest Value, Never Cheap
Gabriel does not sell low-tier, cheap garbage. His products are built with a physicist's and photographer's focus on structured systems. Price products to match their true quality.

If a price is heavily discounted (e.g., for emergency medical expenses), explain the "why" honestly but professionally:
• **Emergency Medical Fund:** If launching at a discounted price for immediate family needs, maintain professional dignity. Use phrases like: *"Life happens. I'm making these available at this price because I need to get them into the hands of people who'll use them."* 
• **Direct Outreach vs. Product Copy:** Keep product copy focused on intrinsic tool value and structured technical specifications. Save deep personal stories for direct message channels (LinkedIn, email) where the rapport is established and the context is clear.

### Standard Pricing Guidelines

| Niche Tier | Prompt/Item Count | Targeted Price |
| :--- | :--- | :--- |
| **Single-Niche Pack** (e.g., Social, E-commerce) | 68–81 prompts | **$14** |
| **Standard Pack** (e.g., SEO, Email, YouTube) | 110–231 prompts | **$19** |
| **Specialized Bundle** (e.g., Content Empire) | 269 prompts | **$29** |
| **Full Arsenal** (Complete package of all kits) | 1,056 prompts | **$49** |

---

## 5. Publishing & Packaging Workflow

### Product Packaging Requirements
Never publish raw CSVs alone; buyers expect polished deliverables. Every digital package must deliver a consolidated `.zip` file containing:
1. **CSV File:** Raw, importable database file.
2. **PDF Guide:** Highly formatted document with a cover page, table of contents, and clean layout.
3. **HTML Webapp:** A single, offline-capable HTML file with built-in search, filtering, and copy-to-clipboard functionality (using `templates/prompt-webapp.html` as a basis).

*Run the packaging generator:*
```bash
python3 scripts/generate-products.py <csv> <out.html> <out.pdf> "<title>" "<subtitle>"
```

### Browser Publishing Flow
1. Navigate to `https://gumroad.com/products/new`.
2. Fill in the **Name** and set the **Price**.
3. Select **"Next: Customize"** and then **"Save and continue"** to proceed.
4. Attach the packaged `.zip` file under the Content tab.
5. Paste the plain text description (formatting it via the WYSIWYG editor).
6. Fill in all available tag slots and click **Publish**.

---

## 6. Storefront Audit & Visual QA

Always verify product listings in **Incognito Mode** or by logging out. Visual presentation is directly tied to conversions.

### Element Audit Checklist
- **Title & Price:** Ensure they match the editor and show up correctly without truncation.
- **Cover Image:** Ensure a high-quality visual card is set up.
- **Description Formatting:** **CRITICAL CHECK** — Ensure the description does NOT render inside an ugly gray code block with a "Copy" button. (See the ProseMirror fix below).
- **Files Attached:** Check that file sizes and attachment names are correct and available for download.

---

## 7. Troubleshooting: Fixing WYSIWYG Code Blocks

### The ProseMirror Code Block Bug
When pasting description text into the Gumroad editor, it can accidentally wrap in a `<pre><code>` block, causing the public description to render as a gray box with a "Copy" button. This ruins conversion rates.

### The Automated Fix (via headless CDP or Browser console)
To clean up a corrupted description and rewrite it with proper rich HTML, you must explicitly dispatch `input` and `change` events on Gumroad's ProseMirror editor:

1. Navigate to the edit URL: `https://gumroad.com/products/<product_id>/edit`.
2. Target the editor, focus, and clear the existing contents:
```javascript
// Focus and select all content
const pmEditor = document.querySelector('.ProseMirror');
pmEditor.focus();

const sel = window.getSelection();
const range = document.createRange();
range.selectNodeContents(pmEditor);
sel.removeAllRanges();
sel.addRange(range);
```
3. Trigger a `Backspace` keyboard action.
4. Inject clean rich HTML and dispatch events:
```javascript
pmEditor.innerHTML = `<h2>Why This Package Works</h2>
<p>This is a highly structured database designed to bypass standard filler.</p>
<ul>
  <li><strong>231 structured prompts:</strong> copy, paste, and run.</li>
</ul>`;

pmEditor.dispatchEvent(new Event('input', { bubbles: true }));
pmEditor.dispatchEvent(new Event('change', { bubbles: true }));
```
5. Click **"Save changes"** (`button[type="submit"]`).
6. **Verify on the public storefront** to ensure the page updated and cleared caching.

### Scoping Variable Names in Console
`browser_console` shares its JavaScript context across executions. If you redeclare variables using `const` or `let` across multiple calls on the same page, Chrome will throw a `SyntaxError`.
- **Solution:** Use completely unique variable names (e.g., `pmEditor1`, `pmEditor2`, `ed1`, `ed2`) or assign properties directly without variable keywords.

---

## 8. Storefront Purification (Hiding / Unpublishing Products)

When the user wants to curate their public storefront to highlight only a specific premium set, **do NOT delete** their other products. Instead, unpublish them.
- **Benefit:** Hides the product from the public storefront page (`gpframes.gumroad.com`) but keeps them live as drafts. Existing direct links and past buyers are completely unaffected.
- **Automated unpublish script:**
```javascript
const unpubBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Unpublish');
if (unpubBtn) {
  unpubBtn.click();
}
```
Verify status changes to "Unpublished" back in `/products`.

---

## 9. Store Infrastructure Audit

For troubleshooting zero-sales or setting up a new launch, check the entire pipeline beyond the listings. Use `references/gumroad-audit-checklist.md` to check:
1. **Checkout Settings:** Custom fields, redirect URLs, receipts, and VAT handling.
2. **Workflows & Emails:** Auto-responder emails, automated download emails, and custom follow-up automation.
3. **Affiliates:** Tracking links, percentage splits, and payment options.
4. **Sales & Payouts:** Stripe/PayPal integration, direct deposit details, and LatAm payment optimizations (PIX/Hotmart).

---

## 10. Direct Command Line (Gumroad CLI)
For headless checks, use the third-party `@realdichotomy/gumroad-cli`:
- Ensure `GUMROAD_API_KEY` is exported in `~/.hermes/.env`.
- **List products:** `node /path/to/node_modules/@realdichotomy/gumroad-cli/dist/cli.js products`
- **Sales summary:** `node /path/to/node_modules/@realdichotomy/gumroad-cli/dist/cli.js sales`

---

## 📁 Linked References & Support Files

- **`references/gumroad-listing-examples.md`** — Real copy examples of Gabriel's products.
- **`references/outreach-templates.md`** — Social media, LinkedIn, and DM outreach campaigns.
- **`references/gumroad-audit-checklist.md`** — Comprehensive store infrastructure checklist.
- **`references/gumroad-publishing-guide.md`** — Step-by-step browser publishing mechanics.
- **`references/emergency-launch-playbook.md`** — Pricing charts, target sales math, and execution strategy.
- **`references/deepagent-prompt-patterns.md`** — Abacus DeepAgent automation and outreach techniques.
- **`scripts/generate-products.py`** — Automated generation of standard packaging files.
