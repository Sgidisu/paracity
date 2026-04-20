#!/bin/bash
# Paracity Lead Vault Backup Script
BACKUP_DIR=~/paracity_project/backups
mkdir -p $BACKUP_DIR

TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
SOURCE_FILE=~/paracity_project/lead_vault.csv

if [ -f "$SOURCE_FILE" ]; then
    cp "$SOURCE_FILE" "$BACKUP_DIR/lead_vault_backup_$TIMESTAMP.csv"
    echo "✅ Backup successfully archived in $BACKUP_DIR"
else
    echo "❌ Error: lead_vault.csv not found. No backup created."
fi
