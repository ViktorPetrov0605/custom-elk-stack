#!/bin/bash
# Remote ElastiFlow Deployment
# This script copies configs and executes deployment on all servers
# Requires SSH access to be configured first

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "========================================"
echo "ElastiFlow Remote Deployment"
echo "========================================"
echo ""
echo "This will deploy ElastiFlow to:"
echo "  - Frontend (10.4.4.87): Kibana + ES Master"
echo "  - Backend N1 (10.4.4.21:2332): NetFlow Collector + ES Data"
echo "  - Backend N2 (10.4.4.90): sFlow Collector + ES Data"
echo ""

# Check for SSH access
check_ssh() {
    local host=$1
    local port=$2
    local user=$3
    echo -n "Checking SSH access to $user@$host:$port... "
    if ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no -p $port $user@$host "echo OK" 2>/dev/null | grep -q "OK"; then
        echo "✓"
        return 0
    else
        echo "✗ (failed)"
        return 1
    fi
}

# Setup directories on remote hosts
setup_remote() {
    local host=$1
    local port=$2
    local user=$3
    echo "Setting up $host..."
    ssh -p $port $user@$host "mkdir -p ~/elastiflow && chmod 755 ~/elastiflow"
}

# Copy and deploy
deploy_to_host() {
    local host=$1
    local port=$2
    local user=$3
    local compose_file=$4
    local server_type=$5
    
    echo ""
    echo "========================================"
    echo "Deploying to: $host ($server_type)"
    echo "========================================"
    
    # Copy files
    echo "  [1/3] Copying configurations..."
    scp -P $port "$SCRIPT_DIR/$compose_file" $user@$host:~/elastiflow/
    scp -P $port "$SCRIPT_DIR/deploy.sh" $user@$host:~/elastiflow/
    
    # Make executable
    ssh -p $port $user@$host "chmod +x ~/elastiflow/deploy.sh"
    
    # Execute deployment
    echo "  [2/3] Executing deployment..."
    ssh -p $port $user@$host "cd ~/elastiflow && ./deploy.sh $server_type"
    
    echo "  [3/3] Done!"
}

# Main deployment flow
echo ""
echo "Phase 1: Setup remote directories..."

FAIL=0
if check_ssh 10.4.4.87 22 telehouse; then
    setup_remote 10.4.4.87 22 telehouse
else
    FAIL=1
fi

if check_ssh 10.4.4.21 2332 telehouse; then
    setup_remote 10.4.4.21 2332 telehouse
else
    FAIL=1
fi

if check_ssh 10.4.4.90 22 telehouse; then
    setup_remote 10.4.4.90 22 telehouse
else
    FAIL=1
fi

if [ $FAIL -eq 1 ]; then
    echo ""
    echo "ERROR: SSH connection failed to some hosts!"
    echo "Please ensure SSH keys are configured or password is provided."
    echo ""
    echo "To manually copy configs:"
    echo "  scp -P 2332 docker-compose-backend-n1.yml telehouse@10.4.4.21:~/elastiflow/"
    echo "  scp docker-compose-backend-n2.yml telehouse@10.4.4.90:~/elastiflow/"
    echo "  scp docker-compose-frontend.yml telehouse@10.4.4.87:~/elastiflow/"
    exit 1
fi

echo ""
echo "Phase 2: Deploy Frontend (Master Node)"
deploy_to_host 10.4.4.87 22 telehouse docker-compose-frontend.yml frontend

echo ""
echo "Phase 3: Deploy Backend N1 (NetFlow)"
deploy_to_host 10.4.4.21 2332 telehouse docker-compose-backend-n1.yml backend-n1

echo ""
echo "Phase 4: Deploy Backend N2 (sFlow)"
deploy_to_host 10.4.4.90 22 telehouse docker-compose-backend-n2.yml backend-n2

echo ""
echo "========================================"
echo "Deployment Complete!"
echo "========================================"
echo ""
echo "URLs:"
echo "  Kibana:      http://10.4.4.87:5601"
echo "  ES API:      http://10.4.4.87:9200"
echo "  NetFlow:     10.4.4.21:2050/udp"
echo "  sFlow:       10.4.4.90:6343/udp"
echo ""
echo "To verify cluster health:"
echo "  curl http://10.4.4.87:9200/_cluster/health?pretty"
echo ""
