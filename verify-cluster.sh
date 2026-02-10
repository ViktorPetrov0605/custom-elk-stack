#!/bin/bash
# Verify cluster status

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"

echo "================================"
echo "  CLUSTER VERIFICATION"
echo "================================"

echo ""
echo "=== ALL CONTAINERS ==="
echo ""
echo "-- Frontend (10.4.4.87) --"
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$USER_PASS' | su -c 'docker ps --format \"{{.Names}}: {{.Status}}\"'" 2>&1

echo ""
echo "-- Backend N1 (10.4.4.21:2332) --"
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S docker ps --format '{{.Names}}: {{.Status}}'" 2>&1

echo ""
echo "-- Backend N2 (10.4.4.90) --"
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$USER_PASS' | su -c 'docker ps --format \"{{.Names}}: {{.Status}}\"'" 2>&1

echo ""
echo "=== WAITING 30s FOR CLUSTER TO FORM ==="
sleep 30

echo ""
echo "=== CLUSTER HEALTH ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$USER_PASS' | su -c 'docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cluster/health?pretty'" 2>&1

echo ""
echo "=== CLUSTER NODES ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$USER_PASS' | su -c 'docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cat/nodes?v'" 2>&1

echo ""
echo "=== KIBANA CHECK ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$USER_PASS' | su -c 'docker logs custom-elk-stack-kibana-1 --tail 20'" 2>&1
