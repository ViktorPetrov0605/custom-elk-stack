#!/usr/bin/env python3
"""
TTS Client for OpenClaw
Uses local Edge-TTS server to generate voice messages
"""

import requests
import tempfile
import os
from pathlib import Path

# Default TTS server URL
TTS_SERVER = "http://localhost:5050"
# User preferences - can be saved/loaded from config file
USER_VOICES = {
    "en": "en-US-AvaNeural",       # Viktor prefers Ava (female) for English
    "bg": "bg-BG-BorislavNeural",  # Bulgarian male voice
}

DEFAULT_VOICE = USER_VOICES.get("en", "en-US-AvaNeural")

# Voice mappings for different languages
VOICE_MAP = {
    "en": USER_VOICES.get("en", "en-US-AvaNeural"),      # English - user preference: Ava
    "bg": "bg-BG-BorislavNeural",   # Bulgarian - male voice
    "de": "de-DE-KatjaNeural",      # German
    "es": "es-ES-ElviraNeural",     # Spanish
    "fr": "fr-FR-DeniseNeural",     # French
    "it": "it-IT-ElsaNeural",       # Italian
    "ru": "ru-RU-SvetlanaNeural",   # Russian
}

def generate_speech(text: str, language: str = "en", voice: str = None, speed: float = 1.0) -> str:
    """
    Generate speech from text using Edge-TTS
    
    Args:
        text: Text to convert to speech
        language: Language code (en, bg, de, etc.)
        voice: Specific voice (overrides language)
        speed: Playback speed (0.25 to 4.0)
    
    Returns:
        Path to generated audio file
    """
    
    # Get voice for language
    if voice is None:
        voice = VOICE_MAP.get(language, DEFAULT_VOICE)
    
    # Prepare request
    payload = {
        "input": text,
        "voice": voice,
        "response_format": "mp3",
        "speed": speed,
        "model": "tts-1"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer openclaw-tts-key"
    }
    
    # Make request to TTS server
    try:
        response = requests.post(
            f"{TTS_SERVER}/v1/audio/speech",
            json=payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code != 200:
            print(f"TTS Error: {response.status_code} - {response.text}")
            return None
        
        # Save to temp file
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            f.write(response.content)
            return f.name
            
    except Exception as e:
        print(f"TTS Request failed: {e}")
        return None

def get_available_voices(language: str = None) -> list:
    """Get list of available voices"""
    try:
        response = requests.get(
            f"{TTS_SERVER}/v1/voices/all",
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        return []
    except:
        return []

def is_server_running() -> bool:
    """Check if TTS server is running"""
    try:
        response = requests.get(f"{TTS_SERVER}/v1/models", timeout=2)
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    # Test the TTS
    if not is_server_running():
        print("❌ TTS server is not running. Start it with:")
        print("   bash setup-edge-tts.sh")
        exit(1)
    
    # Generate test messages
    test_text = "Hello! I can now send voice messages in different languages."
    
    print("🎤 Testing TTS...")
    audio_file = generate_speech(test_text, language="en")
    
    if audio_file:
        print(f"✅ Audio generated: {audio_file}")
        print(f"   Size: {os.path.getsize(audio_file)} bytes")
    else:
        print("❌ Failed to generate audio")
