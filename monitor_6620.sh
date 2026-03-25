#!/bin/bash

# Configuration: Monitor 6,620 Resistance
TARGET=6620.00
LOG_FILE="monitor_audit.log"

echo -e "\033[1;34m[DAEMON] Monitoring S&P 500 Resistance @ $TARGET... \033[0m"
echo "Session Started: $(date)" > $LOG_FILE

while true; do
    # Capture the current live-calibrated value from your C++ core
    CURRENT=$(./bloomberg_bin IBM | grep "S&P 500 Index" | awk '{print $4}')
    
    # Logic to handle the decimal comparison
    IS_BREAKOUT=$(echo "$CURRENT >= $TARGET" | bc -l)

    if [ "$IS_BREAKOUT" -eq 1 ]; then
        echo -e "\033[1;37;42m [ALERT] BREAKOUT DETECTED: $CURRENT \033[0m"
        ./edit_market.sh IBM SUMM # Generate the confirmed breakout PNG
        echo "[$(date)] BREAKOUT: $CURRENT" >> $LOG_FILE
        break # Exit loop after capture
    else
        GAP=$(echo "$TARGET - $CURRENT" | bc -l)
        echo -e "\033[1;33m[MONITOR] Current: $CURRENT | Gap: $GAP pts\033[0m"
        sleep 300 # Wait 5 minutes for the next audit cycle
    fi
done
