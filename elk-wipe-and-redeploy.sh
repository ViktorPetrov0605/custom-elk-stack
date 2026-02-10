#!/bin/bash
# FULL WIPE AND REDEPLOY per Viktor's instructions
# Use ORIGINAL config (before VB's modifications)

set -e

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
USER_PASS="T3l3h0us#"
ROOT_PASS="T3l3h0us#"
REPO_URL="https://github.com/ViktorPetrov0605/custom-elk-stack.git"

echo "================================================"
echo "  ELK STACK FULL WIPE & REDEPLOY"
echo "  Following Viktor's instructions"
echo "  Using ORIGINAL configuration"
echo "================================================"

# FRONTEND WIPE AND SETUP
echo ""
echo "=== FRONTEND (10.4.4.87) - Wipe and Setup ==="
# Stop and remove containers, wipe directory
echo "Stopping containers and wiping directory..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "echo '$ROOT_PASS' | su -c 'cd /home/telehouse/custom-elk-stack 2>/dev/null && docker compose -f docker-compose-frontend.yml down -v 2>/dev/null; rm -rf /home/telehouse/custom-elk-stack; echo Wiped successfully'" 2>&1

# Fresh clone
echo "Cloning fresh repository..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "cd /home/telehouse && git clone $REPO_URL" 2>&1

# Checkout working commit (before VB's modifications)
echo "Checking out working commit (before modifications)..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "cd /home/telehouse/custom-elk-stack && git checkout e89a306" 2>&1

# Create .env with correct passwords
echo "Creating .env file..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.87 "cd /home/telehouse/custom-elk-stack && cat > .env << 'EOF'
# Security Credentials
ELASTIC_PASSWORD=telehouse
KIBANA_PASSWORD=telehouse

# Stack Configuration
STACK_VERSION=9.2.4
CLUSTER_NAME=netflow-cluster
LICENSE=basic

# Networking - Frontend (Centralized Dashboard)
FRONTEND_IP=10.4.4.87
ES_PORT=9200
KIBANA_PORT=5601

# Networking - Backend (Remote Ingestion)
BACKEND_IP=10.4.4.21,10.4.4.90

# Resource Limits (1GB)
MEM_LIMIT=4294967296

# Generate the keys three times via running
# openssl rand -base64 32
KIBANA_ENCRYPTION_KEY=VzPCNli0+h1PCP3itgyLWUpYNadx2dnJrY8/TB2kpZ4=
KIBANA_SECURITY_KEY=kGaZgIyVGnGJcs2mIico+wtakvTwne523tpdQ6Q50T4=
KIBANA_REPORTING_KEY=yihwn91x6BtzsRo/Qnz++j+aBiRGrfK4UR8tssKXj7c=
EOF
cat .env" 2>&1

# BACKEND N1 WIPE AND SETUP
echo ""
echo "=== BACKEND N1 (10.4.4.21:2332) - Wipe and Setup ==="
echo "Stopping containers and wiping directory..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "echo '$USER_PASS' | sudo -S bash -c 'cd /home/telehouse/custom-elk-stack 2>/dev/null && docker compose -f docker-compose-backend.yml down -v 2>/dev/null; rm -rf /home/telehouse/custom-elk-stack; echo Wiped successfully'" 2>&1

echo "Cloning fresh repository..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse && git clone $REPO_URL" 2>&1

echo "Checking out working commit..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && git checkout e89a306" 2>&1

echo "Creating .env file..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS -p 2332 $USER@10.4.4.21 "cd /home/telehouse/custom-elk-stack && cat > .env << 'EOF'
# Security Credentials
ELASTIC_PASSWORD=telehouse
KIBANA_PASSWORD=telehouse

# Stack Configuration
STACK_VERSION=9.2.4
CLUSTER_NAME=netflow-cluster
LICENSE=basic

# Networking - Frontend (Centralized Dashboard)
FRONTEND_IP=10.4.4.87
ES_PORT=9200
KIBANA_PORT=5601

# Networking - Backend (Remote Ingestion)
BACKEND_IP=10.4.4.21

# Resource Limits (1GB)
MEM_LIMIT=4294967296

# Generate the keys three times via running
# openssl rand -base64 32
KIBANA_ENCRYPTION_KEY=VzPCNli0+h1PCP3itgyLWUpYNadx2dnJrY8/TB2kpZ4=
KIBANA_SECURITY_KEY=kGaZgIyVGnGJcs2mIico+wtakvTwne523tpdQ6Q50T4=
KIBANA_REPORTING_KEY=yihwn91x6BtzsRo/Qnz++j+aBiRGrfK4UR8tssKXj7c=
EOF
cat .env" 2>&1

# BACKEND N2 WIPE AND SETUP
echo ""
echo "=== BACKEND N2 (10.4.4.90) - Wipe and Setup ==="
echo "Stopping containers and wiping directory..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "echo '$ROOT_PASS' | su -c 'cd /home/telehouse/custom-elk-stack 2>/dev/null && docker compose -f docker-compose-backend.yml down -v 2>/dev/null; rm -rf /home/telehouse/custom-elk-stack; echo Wiped successfully'" 2>&1

echo "Cloning fresh repository..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse && git clone $REPO_URL" 2>&1

echo "Checking out working commit..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && git checkout e89a306" 2>&1

echo "Creating .env file..."
sshpass -p "$USER_PASS" ssh $SSH_OPTS $USER@10.4.4.90 "cd /home/telehouse/custom-elk-stack && cat > .env << 'EOF'
# Security Credentials
ELASTIC_PASSWORD=telehouse
KIBANA_PASSWORD=telehouse

# Stack Configuration
STACK_VERSION=9.2.4
CLUSTER_NAME=netflow-cluster
LICENSE=basic

# Networking - Frontend (Centralized Dashboard)
FRONTEND_IP=10.4.4.87
ES_PORT=9200
KIBANA_PORT=5601

# Networking - Backend (Remote Ingestion)
BACKEND_IP=10.4.4.90

# Resource Limits (1GB)
MEM_LIMIT=4294967296

# Generate the keys three times via running
# openssl rand -base64 32
KIBANA_ENCRYPTION_KEY=VzPCNli0+h1PCP3itgyLWUpYNadx2dnJrY8/TB2kpZ4=
KIBANA_SECURITY_KEY=kGaZgIyVGnGJcs2mIico+wtakvTwne523tpdQ6Q50T4=
KIBANA_REPORTING_KEY=yihwn91x6BtzsRo/Qnz++j+aBiRGrfK4UR8tssKXj7c=
EOF
cat .env" 2>&1

echo ""
echo "================================================"
echo "  WIPE AND SETUP COMPLETE"
echo "  All 3 servers ready for startup"
echo "================================================"
