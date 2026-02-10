#!/bin/bash
# ElastiFlow Deployment Script
# Run this on each server after configs are copied

set -e

echo "========================================"
echo "ElastiFlow Deployment Script"
echo "========================================"

SERVER=$1

if [ -z "$SERVER" ]; then
    echo "Usage: ./deploy.sh [frontend|backend-n1|backend-n2]"
    echo ""
    echo "Examples:"
    echo "  ./deploy.sh frontend    # Deploy on 10.4.4.87"
    echo "  ./deploy.sh backend-n1  # Deploy on 10.4.4.21"
    echo "  ./deploy.sh backend-n2  # Deploy on 10.4.4.90"
    exit 1
fi

case $SERVER in
    frontend)
        COMPOSE_FILE="docker-compose-frontend.yml"
        ;;
    backend-n1)
        COMPOSE_FILE="docker-compose-backend-n1.yml"
        ;;
    backend-n2)
        COMPOSE_FILE="docker-compose-backend-n2.yml"
        ;;
    *)
        echo "Unknown server: $SERVER"
        exit 1
        ;;
esac

if [ ! -f "$COMPOSE_FILE" ]; then
    echo "Error: $COMPOSE_FILE not found!"
    exit 1
fi

echo ""
echo "[1/5] Taking down existing deployment (if any)..."
docker-compose -f $COMPOSE_FILE down -v 2>/dev/null || true

echo ""
echo "[2/5] Pulling latest images..."
docker-compose -f $COMPOSE_FILE pull

echo ""
echo "[3/5] Starting services..."
docker-compose -f $COMPOSE_FILE up -d

echo ""
echo "[4/5] Waiting for services to start..."
sleep 30

echo ""
echo "[5/5] Checking service status..."
docker-compose -f $COMPOSE_FILE ps

echo ""
echo "========================================"
echo "Deployment complete for: $SERVER"
echo "========================================"

# Health check
echo ""
echo "Running health checks..."
if [ "$SERVER" = "frontend" ]; then
    curl -s http://localhost:9200/_cluster/health 2>/dev/null | grep -q '"status"' && echo "✓ Elasticsearch is healthy" || echo "✗ Elasticsearch check failed"
    curl -s http://localhost:5601/api/status 2>/dev/null | grep -q '"state":"green"' && echo "✓ Kibana is ready" || echo "⚠ Kibana still starting..."
else
    curl -s http://localhost:9200/_cluster/health 2>/dev/null | grep -q '"status"' && echo "✓ Elasticsearch data node is healthy" || echo "✗ ES check failed"
    docker ps | grep -q elastiflow-collector && echo "✓ ElastiFlow collector is running" || echo "✗ Collector not running"
fi

echo ""
echo "To view logs: docker-compose -f $COMPOSE_FILE logs -f"
