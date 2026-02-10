#!/bin/bash
# Fix backend issues

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"

echo "=== FIXING BACKEND N2 - Remove orphaned container ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$USER_PASS' | su -c 'docker rm -f custom-elk-stack-es-remote-1 custom-elk-stack-logstash-1 2>/dev/null; docker compose -f docker-compose-backend.yml up -d'" 2>&1

echo ""
echo "=== FIXING BACKEND N1 - Use docker-compose (hyphen) syntax ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml up -d'" 2>&1

echo ""
echo "=== VERIFYING ALL CONTAINERS ==="
echo "Frontend:"
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$USER_PASS' | su -c 'docker ps --format \"table {{.Names}}\t{{.Status}}\t{{.Ports}}\"'" 2>&1

echo ""
echo "Backend N1:"
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'" 2>&1

echo ""
echo "Backend N2:"
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$USER_PASS' | su -c 'docker ps --format \"table {{.Names}}\t{{.Status}}\t{{.Ports}}\"'" 2>&1
