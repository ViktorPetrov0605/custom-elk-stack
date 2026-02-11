# TTS Integration for OpenClaw

This setup adds voice messaging capability to Valentin-bot using the free Edge-TTS service.

## Quick Start

```bash
cd ~/.openclaw/workspace
bash setup-edge-tts.sh
```

This will:
1. Download and start the Edge-TTS Docker container
2. Expose TTS API on port 5050
3. Test the connection

## Usage

### From Python

```python
from tts_client import generate_speech, is_server_running

# Check server
if is_server_running():
    # Generate English voice
    audio_path = generate_speech("Hello! This is a voice message.", language="en")
    
    # Generate Bulgarian voice
    audio_path = generate_speech("Здравей! Това е гласово съобщение.", language="bg")
```

### Available Languages

| Language | Code | Voice |
|----------|------|-------|
| English | `en` | en-US-AvaNeural |
| Bulgarian | `bg` | bg-BG-KalinaNeural |
| German | `de` | de-DE-KatjaNeural |
| Spanish | `es` | es-ES-ElviraNeural |
| French | `fr` | fr-FR-DeniseNeural |
| Italian | `it` | it-IT-ElsaNeural |
| Russian | `ru` | ru-RU-SvetlanaNeural |

See all voices at: https://tts.travisvn.com/

## API Endpoints

- `POST /v1/audio/speech` - Generate speech from text
- `GET /v1/voices/all` - List all available voices
- `GET /v1/models` - List available TTS models

### Example Request

```bash
curl -X POST http://localhost:5050/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input": "Hello!", "voice": "alloy", "response_format": "mp3"}' \
  --output voice.mp3
```

## Docker Management

```bash
# Check if running
docker ps | grep edge-tts

# View logs
docker logs edge-tts-server --tail 50

# Restart
docker restart edge-tts-server

# Stop
docker stop edge-tts-server
```

## Integration with Telegram

To send voice messages via Telegram, use the `message` tool with:
```python
message(action="send", media="path/to/audio.mp3", asVoice=True)
```

## Notes

- Uses Microsoft Edge's free TTS service
- No API key required (set `REQUIRE_API_KEY=False`)
- Supports 100+ languages
- MP3 output format
- Adjustable speed (0.25x to 4.0x)