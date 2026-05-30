# Gumroad Browser Login — Operational Notes

## ⚠️ Browser Login Status: WORKS (inconsistently)

As of **2026-05-26**, browser-based login to Gumroad is possible via the Hermes browser tool, but with caveats:

- **Login works** with email+password via `browser_type` — no OAuth/Google path (those require manual interaction)
- **Sessions expire unpredictably.** Navigating between pages (e.g. from dashboard to products) can silently log you out, dropping you back on the login form. You'll need to re-authenticate.
- **No 2FA triggered** during this session (email+password was sufficient), but Gumroad may send an auth code for new devices/sessions — have the user ready to provide it.
- **The password form renders differently** from the email form — `browser_type` works on both, but verify the login button is visible before clicking it.
- **No bot detection blanking** was observed during this session — earlier reports of blanking may have been resolved or environment-dependent.

**Login flow (when it works):**
1. Navigate to `https://gumroad.com/login` (or any protected URL that redirects there)
2. `browser_type` email → `browser_type` password → click "Login"
3. You land on the dashboard or the originally-requested page
4. If the login button doesn't respond, try clicking via `browser_console` JS

**When to have the user log in manually:**
- If bot detection keeps blanking the page (environment-dependent race condition)
- If OAuth is the only path available (Google/X/Stripe buttons don't work via automation)
- If 2FA kicks in and you don't have real-time access to the user's email
- After 2-3 failed login attempts — don't keep retrying, ask the user
  
## What Still Works Without Login

- Viewing public storefront pages
- Viewing public product pages (incognito / logged-out view)
- Navigating the store as a visitor
- Checking product descriptions, pricing, and images from the buyer's perspective
