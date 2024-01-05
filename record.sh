#!/bin/bash

# This script records a video in H264 encoding for the specified device.
# Version: 1.0
# Author: Daniel Schneider
# Date: 01/03/2024

VIDEO_DEVICE=0

# Check if VIDEO_DEVICE is provided
if [ -n "$1" ]; then
  VIDEO_DEVICE="$1"
fi

# Generate output file name. The name reflects the epoch time whilst creating
OUTPUT_FILE="${EPOCHREALTIME/[^0-9]/}_cam_$VIDEO_DEVICE.mp4"

ffmpeg -f v4l2 -i /dev/video$VIDEO_DEVICE -c:v libx264 -preset ultrafast -use_wallclock_as_timestamps 1 -fflags +genpts -metadata date="${EPOCHREALTIME/[^0-9]/}"  $OUTPUT_FILE 2>/dev/null #-fps_mode passthrough

#ffmpeg -f v4l2 -i /dev/video$VIDEO_DEVICE -c:v libx264 -preset ultrafast -use_wallclock_as_timestamps 1 -fflags +genpts -metadata date="${EPOCHREALTIME/[^0-9]/}" -vf "crop=in_w:in_h-40:0:40" $OUTPUT_FILE 2>/dev/null
