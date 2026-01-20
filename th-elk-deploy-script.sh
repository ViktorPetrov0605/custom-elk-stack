#!/bin/bash

# --- CONFIGURATION ---
ASCII_LOGO='
                                                                         
                                                                         
██████ ██  ██     ██████ ██     ██ ▄█▀                                   
  ██   ██████ ▄▄▄ ██▄▄   ██     ████                                     
  ██   ██  ██     ██▄▄▄▄ ██████ ██ ▀█▄                                   
                                                                         
                                                                         
                                                                         
████▄  ██████ █████▄ ██     ▄████▄ ██  ██ ██▄  ▄██ ██████ ███  ██ ██████ 
██  ██ ██▄▄   ██▄▄█▀ ██     ██  ██  ▀██▀  ██ ▀▀ ██ ██▄▄   ██ ▀▄██   ██   
████▀  ██▄▄▄▄ ██     ██████ ▀████▀   ██   ██    ██ ██▄▄▄▄ ██   ██   ██   
                                                                         
                                                                         
                                                                         
▄█████ ▄█████ █████▄  ██ █████▄ ██████                                   
▀▀▀▄▄▄ ██     ██▄▄██▄ ██ ██▄▄█▀   ██                                     
█████▀ ▀█████ ██   ██ ██ ██       ██                                     
                                                                         
'

# --- HELPERS ---
print_logo() {
    echo "$ASCII_LOGO"
    echo "Custom TH ELK monitoring stack deployment & setup tool"
    echo "------------------------------------------------"
}

check_connectivity() {
    local target=$1
    echo "Testing connectivity to $target..."
    if ping -c 1 -W 2 "$target" > /dev/null 2>&1; then
        echo "Target $target is reachable."
    else
        read -p "Target $target did not respond to ping. Manual override to continue? (y/n): " override
        if [[ ! $override =~ ^[Yy]$ ]]; then
            echo "Deployment aborted."
            exit 1
        fi
    fi
}

# --- START SCRIPT ---
clear
print_logo

# 0. Sudo / Root Privilege Check
if [[ $EUID -ne 0 ]]; then
   echo "CRITICAL ERROR: This script performs system optimizations and requires root privileges."
   echo "Please run with: sudo $0"
   exit 1
fi

# 1. Deployment Type Selection
echo "Which component are you deploying on this server?"
echo "1) Kibana Frontend (Hub)"
echo "2) Logstash + Elasticsearch (Backend Spoke)"
read -p "Selection (1 or 2): " TYPE

# 2. System Optimization (Quality of Life)
echo "Running system optimizations..."

# Set vm.max_map_count for Elasticsearch performance
echo "Setting vm.max_map_count to 262144..."
sudo sysctl -w vm.max_map_count=262144

# Best Practice: Note that swapping is discouraged for ES stability
read -p "The documentation recommends DISABLING swap for ES stability. Disable swap now? (y/n): " disable_swap
if [[ $disable_swap =~ ^[Yy]$ ]]; then
    sudo swapoff -a
    echo "Swap disabled."
else
    echo "Proceeding without disabling swap (not recommended for production)."
fi

# 3. Information Gathering & Config Generation
if [ "$TYPE" == "1" ]; then
    # --- HUB DEPLOYMENT ---
    read -p "Enter the IP address of the first Spoke (Elasticsearch) server: " SPOKE_IP
    check_connectivity "$SPOKE_IP"
    
    # Update the .env file with the Spoke's IP address
    # This matches the ${SPOKE_IP} variable in the docker-compose file
    if grep -q "SPOKE_IP=" .env; then
        sed -i "s/SPOKE_IP=.*/SPOKE_IP=$SPOKE_IP/" .env
    else
        echo "SPOKE_IP=$SPOKE_IP" >> .env
    fi

    COMPOSE_FILE="docker-compose-frontend.yml"
    echo "Configuration updated. Hub will connect to https://$SPOKE_IP:9200"
        
else
    # BACKEND (SPOKE)
    read -p "Enter the IP address of the central Kibana Hub: " HUB_IP
    read -p "Enter a unique Node Name for this server: " NODE_NAME
    check_connectivity "$HUB_IP"

    # Set mandatory passwords and node names
    export HOSTNAME=$NODE_NAME
    COMPOSE_FILE="docker-compose-backend.yml"
fi

# 4. Final Deployment
echo "Finalizing deployment using $COMPOSE_FILE..."
read -p "Start containers now? (y/n): " start_now
if [[ $start_now =~ ^[Yy]$ ]]; then
    # Run setup first to initialize v9 security settings if necessary
    docker compose -f "$COMPOSE_FILE" up -d
    echo "Deployment complete! Check logs with: docker compose logs -f"
fi
