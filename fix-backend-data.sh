#!/bin/bash
# Fix backend cluster UUID issue by wiping ES data

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

echo "=== STOPPING AND WIPING BACKEND N1 ES DATA ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml down -v && docker volume rm custom-elk-stack_data-remote 2>/dev/null; docker volume create custom-elk-stack_data-remote'" 2>&1

echo ""
echo "=== RESTARTING BACKEND N1 ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml up -d" 2>&1

echo ""
echo "=== STOPPING AND WIPING BACKEND N2 ES DATA ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$PASS' | su -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml down -v && docker volume rm custom-elk-stack_data-remote 2>/dev/null; docker volume create custom-elk-stack_data-remote'" 2>&1

echo ""
echo "=== RESTARTING BACKEND N2 ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml up -d" 2>&1

echo ""
echo "=== WAITING 30s FOR BACKENDS TO JOIN ==="
sleep 30

echo ""
echo "=== CHECKING CLUSTER STATUS ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cat/nodes?v" 2>&1

echo ""
echo "=== CLUSTER HEALTH ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cluster/health?pretty" 2>&1
