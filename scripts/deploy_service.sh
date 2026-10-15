#!/bin/bash

echo "=== [BASH] Starting Infrastructure Service Deployment ==="
LOG_FILE="logs/provisioning.log"

# Log deployment step
echo "$(date): Deploying Nginx service configuration..." >> "$LOG_FILE"
echo "[BASH] Service deployed successfully."
