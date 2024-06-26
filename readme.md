# YouTube Audio Downloader

The **Video Downloader and 'to Audio' Converter** is a Python script that converts MP4 video files to MP3 audio files. 
Python script that enables users to download the audio track of YouTube videos in MP3 format. It provides a simple 
command-line interface for specifying the URL of the YouTube video and an optional default path to save the downloaded 
audio file.

## Features

- Download the audio track of a YouTube video in MP3 format.
- Download multiple urls at once
- Set a default path to save the downloaded audio file.

## Requirements

- Python 3.x
- pytube library (pip install pytube)

## Installation

1. Install Python 3.x if you haven't already.

2. Install the required dependencies using pip:

    ```
    pip install pytube
    ```

3. Clone the repository or copy the script to your local machine.

4. Run the script:

    ```
    python yt-audio.py
    ```

## Usage

### Download single file
The yt-audio.py can be executed from the command line with the following options:

- **URL**: Specify the URL of the YouTube video as a positional argument.

- `-p, --path`: (Optional) Set a default path to save the downloaded audio file.

Example usage:
    ```
   python yt-audio.py https://www.youtube.com/video1 -p /path/to/save/audio
    ```

### Download multiple files
Seed **urls.txt** file with the desired urls. Running list.py script will download all videos 
and convert them to mp3

Example usage:
    ```
   python list.py
    ```


