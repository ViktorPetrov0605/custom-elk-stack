#!/bin/bash
# Copy certificates to backends and restart

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

echo "=== COPYING CERTS TO BACKEND N1... ==="
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/ca/ca.crt $USER@10.4.4.21:/tmp/ca.crt
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/ca/ca.key $USER@10.4.4.21:/tmp/ca.key
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/wildcard/wildcard.crt $USER@10.4.4.21:/tmp/wildcard.crt
sshpass -p "$PASS" scp $SSH_OPTS -P 2332 /tmp/certs_sync/wildcard/wildcard.key $USER@10.4.4.21:/tmp/wildcard.key

sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && rm -rf certs && mkdir -p certs/ca certs/wildcard && cp /tmp/ca.crt /tmp/ca.key certs/ca/ && cp /tmp/wildcard.crt /tmp/wildcard.key certs/wildcard/ && ls -la certs/ca/ && ls -la certs/wildcard/" 2>&1

echo ""
echo "=== COPYING CERTS TO BACKEND N2... ==="
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/ca/ca.crt $USER@10.4.4.90:/tmp/ca.crt
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/ca/ca.key $USER@10.4.4.90:/tmp/ca.key
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/wildcard/wildcard.crt $USER@10.4.4.90:/tmp/wildcard.crt
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/wildcard/wildcard.key $USER@10.4.4.90:/tmp/wildcard.key

sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && rm -rf certs && mkdir -p certs/ca certs/wildcard && cp /tmp/ca.crt /tmp/ca.key certs/ca/ && cp /tmp/wildcard.crt /tmp/wildcard.key certs/wildcard/ && ls -la certs/ca/ && ls -la certs/wildcard/" 2>&1

echo ""
echo "=== RESTARTING BACKEND CONTAINERS ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml restart" 2>&1
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml restart" 2>&1

echo ""
echo "=== WAITING 20s FOR RESTART ==="
sleep 20

echo ""
echo "=== CHECKING CONTAINER STATUS ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "docker ps" 2>&1
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "docker ps" 2>&1
