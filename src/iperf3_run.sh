#!/bin/bash

SERVER_IP=172.31.30.63 
PORT=8001
# DURATION=10
DATA_SIZE=100M
INTERVAL=0.1
LOG_FILE=iperf3_output.log

# ./cca_behavior_measurement/src/ss_watch.sh &
# WATCH_PID=$!
# echo $WATCH_PID

# iperf3 -c $SERVER_IP -p $PORT -i $INTERVAL -t $DURATION --logfile $LOG_FILE
iperf3 -c $SERVER_IP -p $PORT -i $INTERVAL -n $DATA_SIZE --logfile $LOG_FILE

echo "iperf3 output has been redirected to $LOG_FILE"

# kill $WATCH_PID