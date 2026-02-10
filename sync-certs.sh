#!/bin/bash
# Sync certificates from frontend to backends

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"
ROOT_PASS="T3l3h0us#"

echo "=== STORING CERTS TO TEMPORARY LOCATION ==="
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'cat /home/telehouse/custom-elk-stack/certs/ca/ca.crt'" > /tmp/ca.crt 2>/dev/null
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'cat /home/telehouse/custom-elk-stack/certs/ca/ca.key'" > /tmp/ca.key 2>/dev/null
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'cat /home/telehouse/custom-elk-stack/certs/wildcard/wildcard.crt'" > /tmp/wildcard.crt 2>/dev/null
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'cat /home/telehouse/custom-elk-stack/certs/wildcard/wildcard.key'" > /tmp/wildcard.key 2>/dev/null

echo "Certs saved to /tmp/"
ls -la /tmp/*.crt /tmp/*.key

echo ""
echo "=== COPYING TO BACKEND N1 ==="
sshpass -p "$USER_PASS" scp $SSH_OPTS -P 2332 /tmp/ca.crt telehouse@10.4.4.21:/tmp/ca.crt 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS -P 2332 /tmp/ca.key telehouse@10.4.4.21:/tmp/ca.key 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS -P 2332 /tmp/wildcard.crt telehouse@10.4.4.21:/tmp/wildcard.crt 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS -P 2332 /tmp/wildcard.key telehouse@10.4.4.21:/tmp/wildcard.key 2>/dev/null

sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'mkdir -p /home/telehouse/custom-elk-stack/certs/ca /home/telehouse/custom-elk-stack/certs/wildcard && cp /tmp/ca.crt /tmp/ca.key /home/telehouse/custom-elk-stack/certs/ca/ && cp /tmp/wildcard.crt /tmp/wildcard.key /home/telehouse/custom-elk-stack/certs/wildcard/ && chown -R telehouse:telehouse /home/telehouse/custom-elk-stack/certs && ls -la /home/telehouse/custom-elk-stack/certs/ca/ && ls -la /home/telehouse/custom-elk-stack/certs/wildcard/'" 2>&1

echo ""
echo "=== COPYING TO BACKEND N2 ==="
sshpass -p "$USER_PASS" scp $SSH_OPTS /tmp/ca.crt telehouse@10.4.4.90:/tmp/ca.crt 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS /tmp/ca.key telehouse@10.4.4.90:/tmp/ca.key 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS /tmp/wildcard.crt telehouse@10.4.4.90:/tmp/wildcard.crt 2>/dev/null
sshpass -p "$USER_PASS" scp $SSH_OPTS /tmp/wildcard.key telehouse@10.4.4.90:/tmp/wildcard.key 2>/dev/null

sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$ROOT_PASS' | su -c 'mkdir -p /home/telehouse/custom-elk-stack/certs/ca /home/telehouse/custom-elk-stack/certs/wildcard && cp /tmp/ca.crt /tmp/ca.key /home/telehouse/custom-elk-stack/certs/ca/ && cp /tmp/wildcard.crt /tmp/wildcard.key /home/telehouse/custom-elk-stack/certs/wildcard/ && chown -R telehouse:telehouse /home/telehouse/custom-elk-stack/certs && ls -la /home/telehouse/custom-elk-stack/certs/ca/ && ls -la /home/telehouse/custom-elk-stack/certs/wildcard/'" 2>&1

echo ""
echo "=== RESTARTING BACKEND CONTAINERS ==="
echo "Restarting Backend N1..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack && docker-compose -f docker-compose-backend.yml restart'" 2>&1

echo ""
echo "Restarting Backend N2..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$ROOT_PASS' | su -c 'cd /home/telehouse/custom-elk-stack && docker compose -f docker-compose-backend.yml restart'" 2>&1

echo ""
echo "=== DONE - Waiting for ES to start ==="
echo "Check cluster health in 30 seconds..."
