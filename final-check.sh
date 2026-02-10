#!/bin/bash
# Final cluster verification

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

echo "=== CONTAINERS STATUS ==="
echo ""
echo "-- Frontend (10.4.4.87) --"
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker ps --format '{{.Names}}: {{.Status}}'" 2>&1

echo ""
echo "-- Backend N1 (10.4.4.21:2332) --"
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "docker ps --format '{{.Names}}: {{.Status}}'" 2>&1

echo ""
echo "-- Backend N2 (10.4.4.90) --"
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.90 "docker ps --format '{{.Names}}: {{.Status}}'" 2>&1

echo ""
echo "=== WAITING FOR FULL STARTUP ==="
sleep 15

echo ""
echo "=== CLUSTER HEALTH ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cluster/health?pretty" 2>&1

echo ""
echo "=== CLUSTER NODES ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cat/nodes?v" 2>&1

echo ""
echo "=== KIBANA STATUS ==="
sshpass -p "$PASS" ssh $SSH_OPTS $USER@10.4.4.87 "docker logs custom-elk-stack-kibana-1 --tail 10" 2>&1
