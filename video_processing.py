#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: video_processing.py
Author: Daniel Schneider
Date: 01/03/2024
Description: This script extracts the time stamps for all videos in provided directory or slug-folder. It saves a csv-file with epoch time for each frame in the video. If enabeld (settings.toml) also png images are extracted.
"""

import os
import pandas as pd

import src.video_timer as vt
from src import conf
p_ = conf.load_toml()

storage_path = os.getcwd()
slug = "uncovered-bat-25"
path = os.path.join(storage_path, slug)

# Get all video files in provided path
video_files = [f for f in os.listdir(path) if f.endswith(p_.camera.format)]

# Process video file
for video in video_files:
    print('>> Working on: %s'%video)
    
    # Extract all camera information 
    cam_nbr = int(video.split('_')[-1].replace(p_.camera.format, ''))

    # Generate filenames
    _video = os.path.join(path, video)
    _timestamp = _video.replace(p_.camera.format, '_ts.csv')
    _timestamp_augmented = _video.replace(p_.camera.format, '_timestamps.csv')
    _meta = _video.replace(p_.camera.format, '_meta.json')
    _png_dir = os.path.join(path, 'cam_%i_png'%cam_nbr)

    # Generate timestamps
    vt.extract_image_timestamps(_video, _timestamp)

    # Extract all meta data
    vt.extract_meta(_video, _meta)

    # Process timestamps
    start_time = vt.get_start_epoch(_meta) # Extract time stamps from meta data

    # Read the CSV file into a DataFrame
    df = pd.read_csv(_timestamp, header=None, names=['rel', 'img', 'empty'])
    df = df.drop('empty', axis=1)

    df['epoch'] = (df['rel'] * 1_000_000 + start_time).astype(int)
    df = df[['img', 'rel', 'epoch']]
    df.to_csv(_timestamp_augmented, index=False)

    # Generate PNG 
    if p_.settings.extract_png:
        print('>> Extracting images to %s'%video)
        vt.create_directory(_png_dir)
        vt.extract_png(_video, _png_dir)