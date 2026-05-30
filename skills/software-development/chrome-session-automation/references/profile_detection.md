# Profile Detection & Cookie Audit

To identify which Chrome profile contains active session cookies for target sites:

## Python Script to Check Profiles
```python
import os, sqlite3, glob

chrome_base = os.path.expanduser('~/Library/Application Support/Google/Chrome/')
profiles = []
for entry in os.listdir(chrome_base):
    if os.path.isdir(os.path.join(chrome_base, entry)):
        if entry.startswith('Profile ') or entry == 'Default':
            profiles.append(entry)

print("Found profiles:", profiles)

for profile in profiles:
    cookies_path = os.path.join(chrome_base, profile, 'Cookies')
    if os.path.exists(cookies_path):
        try:
            conn = sqlite3.connect(cookies_path)
            c = conn.cursor()
            # Check for specific site cookies
            c.execute("SELECT COUNT(*) FROM cookies WHERE host_key LIKE '%twitter.com%' OR host_key LIKE '%x.com%'")
            twitter_count = c.fetchone()[0]
            c.execute("SELECT COUNT(*) FROM cookies WHERE host_key LIKE '%reddit.com%'")
            reddit_count = c.fetchone()[0]
            c.execute("SELECT COUNT(*) FROM cookies WHERE host_key LIKE '%linkedin.com%'")
            linkedin_count = c.fetchone()[0]
            conn.close()
            print(f"{profile}: twitter cookies {twitter_count}, reddit cookies {reddit_count}, linkedin cookies {linkedin_count}")
        except Exception as e:
            print(f"{profile}: error {e}")
```

## Gabriel's Configuration
- **Active Profile:** `Profile 2` 
- **Session State:** Contains 143 Twitter/X cookies and 9 Reddit cookies (logged in)
- **Location:** `~/Library/Application Support/Google/Chrome/Profile 2/`

## Usage Notes
1. **Profile names vary:** Default, Profile 1, Profile 2, Profile 3, etc.
2. **Cookies database is locked** when Chrome is running - must quit Chrome before copying
3. **Copy only Cookies file** to temporary directory to bypass Chrome's default directory security block
4. **System keychain access:** macOS uses Google Chrome Keychain item to decrypt cookies - local Chrome instances can access this automatically

## Quick Commands
```bash
# List profiles
ls ~/Library/Application\ Support/Google/Chrome/

# Check specific profile
sqlite3 ~/Library/Application\ Support/Google/Chrome/Profile\ 2/Cookies "SELECT host_key FROM cookies WHERE host_key LIKE '%twitter%' LIMIT 5;"
```