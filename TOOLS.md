# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Web Browser (undetected-chromedriver)

**Setup:**
- Virtual env: `~/.openclaw/browser-venv`
- Chromium: v144 at `/usr/bin/chromium`
- ChromeDriver: Auto-downloaded by undetected-chromedriver

**Quick Use:**
```bash
cd ~/.openclaw && source browser-venv/bin/activate && python3 SCRIPT.py
```

**Screenshot a webpage:**
```python
import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')
import undetected_chromedriver as uc
options = uc.ChromeOptions()
options.add_argument('--headless=new --no-sandbox --window-size=1920,1080')
driver = uc.Chrome(options=options, version_main=144)
driver.get('https://example.com')
driver.save_screenshot('/home/valentinbot/.openclaw/screenshot.png')
driver.quit()
```

**Skill docs:** `~/.openclaw/skills/webbrowser/SKILL.md`

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
