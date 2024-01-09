#!/bin/bash

# This script records a video in H264 encoding for the specified device.
# Version: 1.0
# Author: Daniel Schneider
# Date: 01/03/2024


ffmpeg -f v4l2 -i /dev/video0 -c:v libx264 -preset ultrafast -use_wallclock_as_timestamps 1 -fflags +genpts -metadata date="${EPOCHREALTIME/[^0-9]/}"  "${EPOCHREALTIME/[^0-9]/}_cam_0.mp4" 2>/dev/null &
ffmpeg -f v4l2 -i /dev/video4 -c:v libx264 -preset ultrafast -use_wallclock_as_timestamps 1 -fflags +genpts -metadata date="${EPOCHREALTIME/[^0-9]/}"  "${EPOCHREALTIME/[^0-9]/}_cam_4.mp4" 2>/dev/null &

wait