#!/bin/bash
# ... existing script headers ...
# Adding dynamic Docker Compose detection
if command -v docker-compose &> /dev/null; then
    DC="docker-compose"
elif docker compose version &> /dev/null; then
    DC="docker compose"
fi
