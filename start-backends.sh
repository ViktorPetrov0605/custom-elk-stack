#!/bin/bash
# Start backend containers

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"

echo "=== STARTING BACKEND N1 (10.4.4.21:2332) ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml up -d'" 2>&1

echo ""
echo "=== STARTING BACKEND N2 (10.4.4.90) ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$USER_PASS' | su -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml up -d'" 2>&1

echo ""
echo "=== CHECKING CONTAINERS ==="
echo "Backend N1:"
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S docker ps" 2>&1

echo ""
echo "Backend N2:"
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$USER_PASS' | su -c 'docker ps'" 2>&1
