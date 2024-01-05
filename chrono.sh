#!/bin/bash

# This script displays the epoch time with maximum update rate. Using <sleep 0.1> ensures defined frequency.
# Version: 1.0
# Author: Daniel Schneider
# Date: 01/03/2024

while true; do
    printf "%s\r" "${EPOCHREALTIME/[^0-9]/}"
done
