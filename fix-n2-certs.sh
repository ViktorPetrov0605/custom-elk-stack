#!/bin/bash
# Fix Backend N2 SSL certs using su with root password

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

echo "=== COPYING CERTS TO BACKEND N2 WITH ROOT ==="
# Copy via scp first to /tmp
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/ca/ca.crt $USER@10.4.4.90:/tmp/ca.crt
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/ca/ca.key $USER@10.4.4.90:/tmp/ca.key
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/wildcard/wildcard.crt $USER@10.4.4.90:/tmp/wildcard.crt
sshpass -p "$PASS" scp $SSH_OPTS /tmp/certs_sync/wildcard/wildcard.key $USER@10.4.4.90:/tmp/wildcard.key

# Use su to recreate cert directories properly
echo "Recreating cert directories with root..."
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$PASS' | su -c 'rm -rf /home/telehouse/custom-elk-stack/certs && mkdir -p /home/telehouse/custom-elk-stack/certs/ca /home/telehouse/custom-elk-stack/certs/wildcard && cp /tmp/ca.crt /tmp/ca.key /home/telehouse/custom-elk-stack/certs/ca/ && cp /tmp/wildcard.crt /tmp/wildcard.key /home/telehouse/custom-elk-stack/certs/wildcard/ && chown -R telehouse:telehouse /home/telehouse/custom-elk-stack/certs && ls -la /home/telehouse/custom-elk-stack/certs/ca/'" 2>&1

echo ""
echo "=== RESTARTING BACKEND N2 ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml restart" 2>&1

echo ""
echo "=== WAITING 20s FOR RESTART ==="
sleep 20

echo ""
echo "=== CHECKING BACKEND N2 STATUS ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "docker ps" 2>&1

echo ""
echo "=== CHECKING CLUSTER NODES ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cat/nodes?v" 2>&1
