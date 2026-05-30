# Gumroad Publishing Guide — Browser Workflow

## Session notes from May 25, 2026

### What worked
- Email+password login is the most automatable path
- 2FA codes arrive via email — must be entered immediately (expire quickly)
- Product creation flow: Name → Price → "Next: Customize" → "Save and continue" → Content tab
- Using browser_console with JS to click buttons when refs go stale
- Setting description via JS is more reliable than typing into contenteditable

### What didn't work
- File picker dialogs block the entire browser session
- Browser sessions expire during long tasks (repeated 2FA)
- Gumroad API for product creation returns 404 at known endpoints
- Product creation via browser is slow (2-3 min per product)

### Recommended workflow
1. Get login credentials FIRST
2. Confirm delivery format with user
3. Prepare all files while user logs in
4. Create all products in rapid succession
5. Have user upload ZIP files manually
6. Publish

### 2FA handling
- Gumroad sends numeric code to email
- Code expires within ~60 seconds
- User must check email and provide code immediately
