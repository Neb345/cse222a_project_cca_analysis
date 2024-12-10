#!/bin/bash

VIDEOFIlE="/home/ec2-user/sample.mp4"
LOGFILE=cubic.log
DST="172.31.30.63:8001"

# Run the FFmpeg command and redirect both stdout and stderr to the log file
ffmpeg -re -i "$VIDEOFILE" -f mpegts tcp://$DST > "$LOGFILE" 2>&1
 
echo "FFmpeg output has been redirected to $LOGFILE"
