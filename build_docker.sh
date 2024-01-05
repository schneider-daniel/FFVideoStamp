#/bin/bash

# This script runs the build commant to generate the FFVideoStamp image.
# Version: 1.0
# Author: Daniel Schneider
# Date: 01/03/2024

sudo docker build -f Dockerfile -t ffvideostamp:1.0 .