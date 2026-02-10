#!/bin/bash
# ELK Stack Fix Script
# Fixes .env passwords and manages containers

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log() { echo -e "${GREEN}[$(date +%H:%M:%S)]${NC} $1"; }
warn() { echo -e "${YELLOW}[$(date +%H:%M:%S)]${NC} $1"; }
error() { echo -e "${RED}[$(date +%H:%M:%S)]${NC} $1"; }

# Servers
FRONTEND="telehouse@10.4.4.87"
BACKEND1="telehouse@10.4.4.21:2332"
BACKEND2="telehouse@10.4.4.90"
PASS="T3l3h0us#"

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"

log "Checking containers on all servers..."

# Function to check containers via docker
check_containers() {
    local host="$1"
    local port="$2"
    if [ -n "$port" ]; then
        sshpass -p "$PASS" ssh $SSH_OPTS -p $port "$host" "docker ps -a"
    else
        sshpass -p "$PASS" ssh $SSH_OPTS "$host" "docker ps -a"
    fi
}

echo "=== FRONTEND (10.4.4.87) ==="
check_containers "$FRONTEND" "" || error "Failed to check frontend"

echo ""
echo "=== BACKEND N1 (10.4.4.21:2332) ==="
check_containers "$BACKEND1" "2332" || error "Failed to check backend N1"

echo ""
echo "=== BACKEND N2 (10.4.4.90) ==="
check_containers "$BACKEND2" "" || error "Failed to check backend N2"
