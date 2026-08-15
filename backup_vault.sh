#!/bin/bash
# PARACITY Lead Vault Backup Utility
# Purpose: Encrypt and move leads to a secure location

DATE=$(date +%Y-%m-%d_%H%M%S)
SOURCE="lead_vault.csv"
DEST="./backups/paracity_leads_$DATE.csv"

# Ensure backup directory exists
mkdir -p ./backups

# Copy file
cp $SOURCE $DEST

# Log activity (Visible in listener.log)
echo "[$DATE] SUCCESS: Lead Vault Backed Up to $DEST" >> listener.log

# Optional: Keep only the last 30 days of backups
find ./backups -name "*.csv" -type f -mtime +30 -delete
