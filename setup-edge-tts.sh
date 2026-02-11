#!/bin/bash
# Setup script for OpenAI-Compatible Edge-TTS
# Uses Microsoft Edge's free TTS service

set -e

INSTALL_DIR="$HOME/.openclaw/edge-tts"
PORT=5050

echo "🔧 Setting up Edge-TTS Server..."

# Create directory
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"

# Clone the repository if not exists
if [ ! -d "openai-edge-tts" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/travisvn/openai-edge-tts.git
fi

cd openai-edge-tts

# Create .env file
cat > .env <<EOF
API_KEY=openclaw-tts-key
PORT=5050
DEFAULT_VOICE=en-US-AvaNeural
DEFAULT_RESPONSE_FORMAT=mp3
DEFAULT_SPEED=1.0
DEFAULT_LANGUAGE=en-US
REQUIRE_API_KEY=False
REMOVE_FILTER=False
EXPAND_API=True
DETAILED_ERROR_LOGGING=True
EOF

echo "✅ Configuration created"

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "🐳 Starting with Docker..."
    docker run -d \
        --name edge-tts-server \
        -p 5050:5050 \
        -e API_KEY=openclaw-tts-key \
        -e PORT=5050 \
        -e REQUIRE_API_KEY=False \
        -e DEFAULT_VOICE=en-US-AvaNeural \
        -e DEFAULT_LANGUAGE=en-US \
        travisvn/openai-edge-tts:latest
    
    echo "✅ Edge-TTS server started on port 5050"
    echo "📡 API endpoint: http://localhost:5050/v1/audio/speech"
    
else
    echo "⚠️ Docker not available. Please install Docker first."
    exit 1
fi

# Wait for server to start
echo "⏳ Waiting for server to start..."
sleep 5

# Test the API
echo "🧪 Testing TTS API..."
curl -s -X POST http://localhost:5050/v1/audio/speech \
    -H "Content-Type: application/json" \
    -d '{"input": "Hello! I am ready to talk.", "voice": "alloy"}' \
    -o "$INSTALL_DIR/test.mp3" 2>/dev/null

if [ -f "$INSTALL_DIR/test.mp3" ] && [ -s "$INSTALL_DIR/test.mp3" ]; then
    echo "✅ TTS API is working! Test audio saved to $INSTALL_DIR/test.mp3"
else
    echo "⚠️ API test may have failed. Checking status..."
    docker logs edge-tts-server --tail 20
fi

echo ""
echo "🎤 Available voices can be seen at: https://tts.travisvn.com/"
echo "📖 API docs: https://github.com/travisvn/openai-edge-tts"
