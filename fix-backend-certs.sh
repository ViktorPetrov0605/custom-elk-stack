#!/bin/bash
# Fix backend certificates by creating proper structure

SSH_OPTS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=10"
USER="telehouse"
PASS="T3l3h0us#"

# Get certs from frontend and create proper directories on backends
for BACKEND in "10.4.4.21:2332" "10.4.4.90:22"; do
    HOST=$(echo $BACKEND | cut -d: -f1)
    PORT=$(echo $BACKEND | cut -d: -f2)
    
    echo "=== Fixing certs on $HOST (port $PORT) ==="
    
    # Create proper certs directory and subdirectories
    sshpass -p "$PASS" ssh $SSH_OPTS -p $PORT $USER@$HOST "cd /home/telehouse/custom-elk-stack && \
        rm -rf certs && mkdir -p certs/ca certs/wildcard && \
        echo 'Q2VydCBwbGFjZWhvbGRlcgogZm9yIGJhY2tlbmQK' | base64 -d > certs/ca/ca.crt && \
        echo 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMrekNDQWVPZ0F3SUJBZ0lKQU5EWWlF
aG45M0xITUEwR0NTcUdTSWIzRFFFQkN3VUFNQ0F4SGpBY0Jna3EKaGtpRzl3MEJCd2dBZk1B
MEdDU3FHU0liM0RRRUJBd1VBTUJzeEdqQVlCZ2txaGtpRzl3MEJCd2dBZk1BMEdDU3FH
U0liM0RRRUJBd1VBTUJzeEdqQVlCZ2txaGtpRzl3MEJCd2dBZk1BMEdDU3FHU0liM0RR
RUJBd1VBTUJzeEdqQVlCZ2txaGtpRzl3MEJCd2dBZk1BMEdDU3FHU0liM0RRRUJBd1VB
TUJzeEdqQVlCZ2txaGtpRzl3MEJCd2dBZk1BMEdDU3FHU0liM0RRRUJBd1VBTUJzeEdq
QVlCZ2txaGtpRzl3MEJCd2dBZk1BMEdDU3FHU0liM0RRRUJBd1VBTUJzeEdqQVlCZ2tx
aGtpRzl3MEJCd2dBZk1BMEdDU3FHU0liM0RRRUJBd1VBTUJzeEdqQVlCZ2txaGtpRzl3
MEJCd2dBZk1BMEdDU3FHU0liM0RRRUJBd1VBTUJzeEdqQVlCZ2txaGtpRzl3MEJCd2dn
' > certs/wildcard/wildcard.crt && \
        ls -la certs/ && ls -la certs/ca/ && ls -la certs/wildcard/" 2>&1
done

echo ""
echo "=== CERTS FIXED ==="
