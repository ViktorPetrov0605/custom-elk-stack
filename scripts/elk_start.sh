#!/bin/bash
# ELK Distributed Startup Script
# Created by Valentin-bot

PASSWORD="T3l3h0us#"
FRONTEND="10.4.4.87"
BACKEND1="10.4.4.21"
BACKEND2="10.4.4.90"

echo "🚀 Starting Distributed ELK Stack..."

# 1. Start Frontend
echo "Checking Frontend ($FRONTEND)..."
sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no telehouse@$FRONTEND "cd ~/custom-elk-stack && docker compose -f docker-compose-frontend.yml up -d 2>/dev/null"

# 2. Start Backends using remote_setup.sh (which handles env vars)
echo "Checking Backend N1 ($BACKEND1)..."
sshpass -p "$PASSWORD" ssh -p 2332 -o StrictHostKeyChecking=no telehouse@$BACKEND1 "bash ~/remote_setup.sh 2>/dev/null"

echo "Checking Backend N2 ($BACKEND2)..."
sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no telehouse@$BACKEND2 "bash ~/remote_setup.sh 2>/dev/null"

echo "✅ Startup commands sent to all nodes."
echo "⏳ Waiting 30s for services to initialize..."
sleep 30

echo "📊 Status Check:"
sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no telehouse@$FRONTEND "docker ps --format '{{.Names}}: {{.Status}}'"
