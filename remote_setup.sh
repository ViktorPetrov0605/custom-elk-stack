#!/bin/bash
export MEM_LIMIT="4294967296"
export STACK_VERSION="9.2.4"
export CLUSTER_NAME="netflow-cluster"
export FRONTEND_IP="10.4.4.87"
export BACKEND_IP="10.4.4.21,10.4.4.90"
export ELASTIC_PASSWORD="telehouse"
export KIBANA_PASSWORD="telehouse"
export LICENSE="basic"
export ES_PORT="9200"
export KIBANA_PORT="5601"
export KIBANA_ENCRYPTION_KEY="fixed_kibana_encryption_key_32_c"
export KIBANA_SECURITY_KEY="fixed_kibana_security_key_32_ch"
export KIBANA_REPORTING_KEY="fixed_kibana_reporting_key_32_c"

cd ~/custom-elk-stack
docker compose -f docker-compose-frontend.yml up -d
