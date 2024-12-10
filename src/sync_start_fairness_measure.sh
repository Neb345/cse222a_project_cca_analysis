#!/bin/bash

# Path to your SSH key
SSH_KEY="/home/ec2-user/ec2_key.pem"

# Define the user and server IPs
SERVER1=ec2-user@ec2-35-93-131-79.us-west-2.compute.amazonaws.com # First server
SERVER2=ec2-user@ec2-35-92-46-183.us-west-2.compute.amazonaws.com # Second server

# Define the receiver's IP and ports
RECEIVER_IP=172.31.24.14
PORT1=8001
PORT2=8002

# # Run iperf3 on both servers simultaneously
# ssh -i "$SSH_KEY" $SERVER1 "iperf3 -c $RECEIVER_IP -p $PORT1 -t 20" > fairness_measurement/log/20s_cubic_output.log 2>&1 &
# ssh -i "$SSH_KEY" $SERVER2 "iperf3 -c $RECEIVER_IP -p $PORT2 -t 20" > fairness_measurement/log/20s_bbr_output.log 2>&1 &
# wait  # Wait for both commands to finish

ssh -i "$SSH_KEY" $SERVER1 "iperf3 -c $RECEIVER_IP -p $PORT1 -n 1G" > fairness_measurement/log/1G_lossy_cubic_output.log 2>&1 &
ssh -i "$SSH_KEY" $SERVER2 "iperf3 -c $RECEIVER_IP -p $PORT2 -n 1G" > fairness_measurement/log/1G_lossy_bbr_output.log 2>&1 &
wait  # Wait for both commands to finish
