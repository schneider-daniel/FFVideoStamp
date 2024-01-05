#/bin/bash

# This script starts the FFVideoStamp docker image. The working directory as well as /dev is mounted as privileged volume.
# Version: 1.0
# Author: Daniel Schneider
# Date: 01/03/2024

docker run -it --privileged -v /home/usr/daniel/FFVideoStamp:/FFVideoStamp/ -v /dev:/dev ffvideostamp:1.0
