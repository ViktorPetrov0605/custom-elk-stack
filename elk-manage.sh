#!/bin/bash
# Manage ELK Stack - with sudo where available

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
PASS="T3l3h0us#"

echo "=== Backend N1 (10.4.4.21:2332) - Has sudo ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 telehouse@10.4.4.21 "cd /home/telehouse/custom-elk-stack && sudo docker compose -f docker-compose-backend.yml down 2>&1"

echo ""
echo "=== Backend N2 (10.4.4.90) - No docker perms ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.90 "cd /home/telehouse/custom-elk-stack && docker compose ps 2>&1"

echo ""
echo "=== Frontend (10.4.4.87) - Try docker ps anyway ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.87 "cd /home/telehouse/custom-elk-stack && docker ps 2>&1"
