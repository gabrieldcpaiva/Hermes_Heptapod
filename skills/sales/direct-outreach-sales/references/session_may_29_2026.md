================================================================
SESSION NOTES — May 29, 2026
================================================================

REDDIT IP BLOCK:
- Reddit blocked the exit node IP even with authenticated Profile 2 cookies.
- The headless Chrome instance (port 9222) loaded Profile 2's cookies correctly
  (verified: 143 twitter cookies, 9 reddit cookies in Profile 2's DB).
- But Reddit's network security layer blocked access entirely — "You've been
  blocked by network security" page.
- This is an IP reputation issue, not an auth issue.
- WORKAROUND: Gabriel must post Reddit comments manually from his own machine
  (normal Chrome, not headless) or use a mobile connection with different IP.
- The headless Chrome approach works for Twitter/X (verified: showed home feed).

CHROME SESSION REUSE (Confirmed Working):
- Quit Chrome → kill zombies → create /tmp/chrome_profile_temp/
- Copy only Cookies file from ~/Library/ Application Support/Google/Chrome/Profile 2/
- Remove leftover locks in temp dir
- Launch: /Applications/Google Chrome.app/Contents/MacOS/Google Chrome \
    --remote-debugging-port=9222 \
    --user-data-dir=/tmp/chrome_profile_temp \
    --headless=new --window-size=1280,1024
- Connect via: browse open <url> --auto-connect

MESSAGE FORMAT PREFERENCE (Confirmed):
- 3-4 lines max, plain text, repeatable
- Save as .txt files in Outreach_Execution/
- No credential-framing ("8th Airtable user") in product outreach
- Raw honesty about why selling (son's meds) IS the pitch
- Same message across all prospects — do not customize

PRODUCT REALITY:
- 7 products on Gumroad at gpframes.gumroad.com
- Prices: $7, $9, $29 (Full Arsenal)
- NOT R$ 97/197/347 — those were from a different/older listing
- NOT R$ 297 or R$ 1.200 — those were FABRICATED by Gemini Flash
- The 7 products are ONE core system of deterministic prompts

FAKE DRAFTS CLEANUP:
- 23 fake Apple Mail drafts were:
  1. Exported to /Users/gabrielpaiva/Desktop/Hermes/Saved_Drafts/
  2. Deleted from Mail.app
- All pitched fictional products (R$ 297 "Arsenal Soberano", R$ 1.200 "Airtable Audit")
- Created by Gemini Flash in a prior session

================================================================
