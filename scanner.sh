#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP_ADDRESS> <NSE_SCRIPT>"
    echo "Example: $0 192.168.1.1 http-title"
    exit 1
fi

TARGET="$1"
SCRIPT="$2"

# Verify nmap exists
if ! command -v nmap &> /dev/null; then
    echo "Error: nmap is not installed."
    exit 1
fi

echo "Target : $TARGET"
echo "Script : $SCRIPT"
echo "Running scan..."
echo

nmap --script="$SCRIPT" "$TARGET"