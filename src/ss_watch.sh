#!/bin/bash

OUTPUT_FILE="ss_output.log"
INTERVAL=0.1
DST=172.31.30.63
START_TIME=$(date +%s)
DURATION=5 # Wait

while true; do
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$(($CURRENT_TIME - $START_TIME))

    while [[ "$ELAPSED_TIME" -lt "$DURATION" ]]; do
        CURRENT_TIME=$(date +%s)
        ELAPSED_TIME=$(($CURRENT_TIME - $START_TIME))
        sleep $INTERVAL
    done

    ACTIVE_CONNECTION=$(ss -tin dst $DST | grep -q 'ESTAB'; echo $?)

    if [ "$ACTIVE_CONNECTION" -ne 0 ]; then
        echo "No active connection to $DST. Exiting loop."
        break
    fi

    # watch -n 0.1 ss -ein dst $DST | awk '
    ss -tin dst $DST | awk '
    /cwnd|rtt/ {
        # Extract RTT, CWND, SSTHRESH, and Peer Info
        match($0, /rtt:([0-9\.]+)\/([0-9\.]+)/, rtt)
        match($0, /cwnd:([0-9]+)/, cwnd)
        match($0, /ssthresh:([0-9]+)/, ssthresh)
        
        # Print extracted values with a timestamp
        printf("%s RTT: %sms RTTVar: %sms CWND: %d SSTHRESH: %d\n", \
            strftime("%Y-%m-%d %H:%M:%S"), rtt[1], rtt[2], cwnd[1], ssthresh[1])
    }' >> $OUTPUT_FILE
    
    sleep $INTERVAL
done