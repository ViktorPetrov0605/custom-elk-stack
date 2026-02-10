#!/bin/bash
# Start ELK services in correct order per Viktor's instructions

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"
ROOT_PASS="T3l3h0us#"
FRONTEND_IP="10.4.4.87"

# Helper to extract password from .env
get_env_pass() {
    local host="$1"
    local port="${2:-22}"
    if [ "$port" = "22" ]; then
        sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@$host "grep ELASTIC_PASSWORD /home/telehouse/custom-elk-stack/.env | cut -d= -f2"
    else
        sshpass -p "$USER_PASS" ssh $SSH_OPTS -p $port $USER@$host "grep ELASTIC_PASSWORD /home/telehouse/custom-elk-stack/.env | cut -d= -f2"
    fi
}

echo "============================================"
echo "  STARTING ELK STACK SERVICES"
echo "  Order: Frontend first, then Backends"
echo "============================================"

# Check env password
echo ""
echo "Checking .env passwords..."
F_PASS=$(sshpass -p "$USER_PASS" ssh $SSH_OPTS telehouse@10.4.4.87 "grep ELASTIC_PASSWORD /home/telehouse/custom-elk-stack/.env | cut -d= -f2")
B1_PASS=$(sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 telehouse@10.4.4.21 "grep ELASTIC_PASSWORD /home/telehouse/custom-elk-stack/.env | cut -d= -f2")
B2_PASS=$(sshpass -p "$USER_PASS" ssh $SSH_OPTS telehouse@10.4.4.90 "grep ELASTIC_PASSWORD /home/telehouse/custom-elk-stack/.env | cut -d= -f2")
echo "  Frontend: $F_PASS"
echo "  Backend N1: $B1_PASS"
echo "  Backend N2: $B2_PASS"

# START FRONTEND
echo ""
echo "=== STEP 1: STARTING FRONTEND (10.4.4.87) ==="
echo "Starting with root (docker permission)..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@$FRONTEND_IP "echo '$ROOT_PASS' | su -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-frontend.yml up -d --build'" 2>&1

echo ""
echo "Waiting 30s for frontend ES to start..."
sleep 30

# Check frontend status
echo "Checking frontend containers..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@$FRONTEND_IP "echo '$ROOT_PASS' | su -c 'docker ps && docker logs custom-elk-stack-setup-1 --tail 20 2>/dev/null || echo Setup container may have exited'" 2>&1

# START BACKEND N1
echo ""
echo "=== STEP 2: STARTING BACKEND N1 (10.4.4.21:2332) ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml up -d --build'" 2>&1

# START BACKEND N2
echo ""
echo "=== STEP 3: STARTING BACKEND N2 (10.4.4.90) ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$ROOT_PASS' | su -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml up -d --build'" 2>&1

echo ""
echo "Waiting 60s for all services to start and cluster to form..."
sleep 60

echo ""
echo "=== STEP 4: VERIFYING CLUSTER ==="
echo "Checking cluster health on frontend..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@$FRONTEND_IP "echo '$ROOT_PASS' | su -c 'docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cluster/health'" 2>&1

echo ""
echo "Checking nodes..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@$FRONTEND_IP "echo '$ROOT_PASS' | su -c 'docker exec custom-elk-stack-es-frontend-1 curl -s -k -u elastic:telehouse https://localhost:9200/_cat/nodes?v'" 2>&1

echo ""
echo "============================================"
echo "  STARTUP COMPLETE - CHECK LOGS ABOVE"
echo "============================================"
