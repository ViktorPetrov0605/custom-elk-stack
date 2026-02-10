#!/bin/bash
# Fix SSL certificates - copy from frontend to backends

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"
ROOT_PASS="T3l3h0us#"

echo "=== CHECKING CERTS ON FRONTEND ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'ls -la /home/telehouse/custom-elk-stack/certs/'" 2>&1

echo ""
echo "=== CHECKING IF SETUP CONTAINER GENERATED CERTS ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'ls -la /home/telehouse/custom-elk-stack/certs/ca/ 2>/dev/null; ls -la /home/telehouse/custom-elk-stack/certs/wildcard/ 2>/dev/null; docker logs custom-elk-stack-setup-1'" 2>&1 | head -40

echo ""
echo "=== CHECKING BACKEND N1 CERTS ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "ls -la /home/telehouse/custom-elk-stack/certs/" 2>&1

echo ""
echo "=== CHECKING BACKEND N2 CERTS ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "ls -la /home/telehouse/custom-elk-stack/certs/" 2>&1
