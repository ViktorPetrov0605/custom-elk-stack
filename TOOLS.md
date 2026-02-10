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

## SearXNG Local Search (Default)

**Status:** Docker container on localhost:8888 — 30+ search engines (Google, Brave, Bing, DDG, Qwant, etc.)

**Check if running:**
```bash
node ~/.openclaw/scripts/searxng_local.js --check
```

**Search:**
```bash
node ~/.openclaw/scripts/searxng_local.js "your query" --limit 10
```

**Files:**
- `~/.openclaw/searxng/` — Docker Compose + config
- `~/.openclaw/scripts/searxng_local.js` — Search tool
- `SEARCH_INSTRUCTIONS.md` — Full search strategy guide

## Custom Slash Commands

### /dalivali
Simple command that responds with "ne" (Bulgarian for "no").

**Location:** `~/.openclaw/skills/dalivali/`  
**Usage:** Send `/dalivali` in chat  
**Response:** `ne`

### /daliboli
Simple command that responds with "da" (Bulgarian for "yes").

**Location:** `~/.openclaw/skills/daliboli/`  
**Usage:** Send `/daliboli` in chat  
**Response:** `da`

---

## Speech-to-Text (Whisper)

**Local voice message transcription for Telegram/WhatsApp.**

**Status:** ✅ Active — I can receive and transcribe voice messages in English and Bulgarian.

**Setup:**
- Virtual env: `~/.openclaw/whisper-venv`
- Model: Whisper `base` (151MB, good balance of speed/accuracy)
- Dependencies: `ffmpeg` (installed at system level)
- RAM usage: ~2-3GB
- Languages tested: English, Bulgarian (supports 99 languages total)

**How it works:**
1. Voice messages arrive as OGG audio files (Telegram) or other formats
2. I receive the audio file path in the message context
3. Run transcription using Whisper locally (no cloud, no API keys)
4. The transcribed text appears in my context — I respond to what you said

**Transcription commands:**

```bash
# English (auto-detected)
cd /tmp && ~/.openclaw/whisper-venv/bin/whisper /path/to/audio.ogg --model base --device cpu --output_format txt

# Bulgarian (explicit language)
ffmpeg -i /path/to/audio.ogg -ar 16000 -ac 1 -c:a pcm_s16le /tmp/audio.wav
cd /tmp && ~/.openclaw/whisper-venv/bin/whisper /tmp/audio.wav --model base --device cpu --output_format txt --language bg
```

**Notes:**
- First run downloads the model (~151MB for base)
- For best Bulgarian results, convert to WAV 16kHz mono first
- Base model is fast enough for real-time on this hardware (6 cores, 8GB RAM)
- Larger models (small, medium, turbo) available for better accuracy

---

## AliExpress Search Tool

**Browser-based AliExpress product search with URL filter parameters.**

**File:** `~/.openclaw/aliexpress_search.py`

**Usage:**
```bash
cd ~/.openclaw && source browser-venv/bin/activate && python3 aliexpress_search.py "laptop" --min-price 300 --max-price 800 --sort price_asc --free-ship
```

**Parameters:**
- `--min-price`, `--max-price` — Price range
- `--sort` — `price_asc`, `price_desc`, `orders`, `newest`
- `--free-ship` — Free shipping only
- `--ship-from CN|US|etc` — Ship from country
- `--ship-to BG|US|etc` — Ship to country (default: BG)
- `--page N` — Page number
- `-o output.json` — Save to file

**URL Structure** (documented in `ALIEXPRESS_SEARCH.md`):
```
https://www.aliexpress.com/wholesale?SearchText=QUERY&minPrice=X&maxPrice=Y&sortType=price_asc&isFreeShip=y
```

**Note:** AliExpress loads products dynamically via JavaScript. This tool uses undetected-chromedriver to render the full page and extract data. First run may be slow (downloads chromedriver).

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
