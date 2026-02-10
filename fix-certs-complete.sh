#!/bin/bash
# Fix SSL certificates on backends using sudo

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

echo "=== FIXING BACKEND N1 (10.4.4.21:2332) ==="
# Remove certs dir with sudo, recreate, copy files
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && rm -rf certs && mkdir -p certs/ca certs/wildcard && chown -R telehouse:telehouse certs && ls -la certs/'" 2>&1

# Copy cert files
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/ca/ca.crt $USER@10.4.4.21:/home/telehouse/custom-elk-stack/certs/ca/ 2>/dev/null
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/ca/ca.key $USER@10.4.4.21:/home/telehouse/custom-elk-stack/certs/ca/ 2>/dev/null
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/wildcard/wildcard.crt $USER@10.4.4.21:/home/telehouse/custom-elk-stack/certs/wildcard/ 2>/dev/null
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/wildcard/wildcard.key $USER@10.4.4.21:/home/telehouse/custom-elk-stack/certs/wildcard/ 2>/dev/null

# Verify
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "ls -la /home/telehouse/custom-elk-stack/certs/ca/ && ls -la /home/telehouse/custom-elk-stack/certs/wildcard/" 2>&1

echo ""
echo "=== RESTARTING BACKEND N1 ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml restart" 2>&1

echo ""
echo "=== FIXING BACKEND N2 (10.4.4.90) ==="
# Backend N2 doesn't have sudo, use su with root password
echo "Checking if we can use su..."
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$PASS' | su -c 'whoami'" 2>&1

echo ""
echo "=== ALL DONE - WAITING FOR RESTART ==="
sleep 20

echo ""
echo "=== CHECKING CONTAINERS ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "docker ps" 2>&1
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "docker ps" 2>&1
