#!/bin/bash
export MEM_LIMIT="2147483648"
export STACK_VERSION="9.2.4"
export CLUSTER_NAME="netflow-cluster"
export FRONTEND_IP="10.4.4.87"
export BACKEND_IP="10.4.4.21,10.4.4.90"
export ELASTIC_PASSWORD="telehouse"
export KIBANA_PASSWORD="telehouse"
export LICENSE="basic"

mkdir -p ~/custom-elk-stack
cd ~/custom-elk-stack
docker compose -f docker-compose-backend.yml up -d
