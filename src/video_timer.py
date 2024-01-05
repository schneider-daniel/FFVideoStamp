#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: video_timer.py
Author: Daniel Schneider
Date: 01/03/2024
Description: This file provides function set to extract time infomration from recorded images using ffmpeg.
"""

import os
import json

def extract_meta(video_file, meta_file): 
    """
    Extract metadata from a video file using ffprobe and save it to a JSON file.

    Args:
        video_file (str): Path to the input video file from which metadata will be extracted.
        meta_file (str): Path to the output JSON file where the extracted metadata will be saved.

    Returns:
        None

    Notes:
        This function uses the ffprobe utility to retrieve metadata information from the
        provided video_file and saves it in JSON format to the specified meta_file. The
        generated JSON file will contain details about the video's format and streams,
        making it easier to analyze or process metadata.

    Example:
        extract_meta("input.mp4", "metadata.json")
    """
    prompt = f"ffprobe -v quiet -print_format json -show_format -show_streams {video_file} > {meta_file}"
    os.system(prompt)

def extract_image_timestamps(video_file, ts_file):
    """
    Extract image timestamps from a video file using ffprobe and save them to a text file.

    Args:
        video_file (str): Path to the input video file from which image timestamps will be extracted.
        ts_file (str): Path to the output text file where the extracted timestamps will be saved.

    Returns:
        None

    Notes:
        This function uses the ffprobe utility to retrieve timestamps for each frame in the
        provided video_file. The timestamps include coded_picture_number and pkt_dts_time,
        and they are saved in a text file specified by ts_file. Each line in the output file
        represents a timestamp for a frame, making it useful for frame-by-frame analysis.

    Example:
        extract_image_timestamps("input.mp4", "timestamps.txt")
    """
    prompt = f"ffprobe {video_file} -select_streams v -show_entries frame=coded_picture_number,pkt_dts_time -of csv=p=0:nk=1 -v 0 > {ts_file}" #pts_time or pkt_dts_time
    os.system(prompt)

def get_start_epoch(meta_file):
    """
    Get the start epoch time from metadata stored in a JSON file.

    Args:
        meta_file (str): Path to the JSON file containing metadata information.

    Returns:
        int: The start epoch time extracted from the metadata.

    Notes:
        This function reads the specified JSON file to retrieve the start epoch time
        from the metadata. The start epoch time is typically stored under the 'date'
        key in the 'tags' section of the 'format' section within the JSON data.

    Example:
        start_epoch = get_start_epoch("metadata.json")
    """
    with open(meta_file, 'r') as file:
        data = json.load(file)
    file.close()
    return int(data['format']['tags']['date'])

def extract_png(video_file, storage_path):
    """
    Extract PNG frames from a video file using ffmpeg and save them to a specified directory.

    Args:
        video_file (str): Path to the input video file from which PNG frames will be extracted.
        storage_path (str): Path to the directory where the extracted PNG frames will be saved.

    Returns:
        None

    Notes:
        This function uses ffmpeg to extract PNG frames from the provided video_file. The
        extracted frames are saved as numbered PNG files in the specified storage_path
        directory. The '-q:v 2' option controls the quality of the extracted frames.

    Example:
        extract_png("input.mp4", "frames_directory")
    """
    prompt = f"ffmpeg -i {video_file} -q:v 2 {storage_path}/%06d.png 2>/dev/null"
    os.system(prompt)

def create_directory(directory_path):
    """
    Create a directory if it does not exist, or print a message if it already exists.

    Args:
        directory_path (str): Path to the directory to be created.

    Returns:
        None

    Notes:
        This function checks if the specified directory already exists. If it does not exist,
        it creates the directory and prints a message indicating that it has been created.
        If the directory already exists, it prints a message indicating that it is already present.

    Example:
        create_directory("/output_frames")
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")