#!/bin/bash
PASSWORD="T3l3h0us#"
SSH_OPTS="-o StrictHostKeyChecking=no -o ConnectTimeout=10"

ssh_pw() {
    SSH_ASKPASS=./ssh_askpass.sh setsid -w ssh $SSH_OPTS "$@"
}

log() { echo -e "\033[1;34m[VALENTIN]\033[0m $1"; }

log "Starting ELK Deployment process..."

# 1. Prepare frontend (10.4.4.87)
log "Deploying Frontend on 10.4.4.87..."
# (In a real scenario, I'd rsync the workspace or git clone)
# For now, let's assume the repo is already there or we need to push it
# My MEMORY says I manually deployed this on 2026-02-18, so I should check status first.

log "Checking health of existing stack..."
# Check ES on .87
ssh_pw telehouse@10.4.4.87 "curl -u elastic:telehouse -k -s https://localhost:9200/_cluster/health"
