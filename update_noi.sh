#!/bin/bash
CURRENT_NOI=$(jq '.noi' asset_data.json)
NEW_NOI=$(echo "$CURRENT_NOI * 1.02" | bc | cut -d'.' -f1)
echo "{\"noi\": $NEW_NOI, \"last_updated\": \"$(date +%Y-%m-%d)\"}" > asset_data.json
echo "Portfolio NOI Updated to $NEW_NOI"
