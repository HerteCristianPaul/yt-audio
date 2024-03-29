import argparse
import json
import os
import subprocess

from pytube import YouTube


def download_video(url: str, location: str = None) -> str:
    """
    Download the audio track of a YouTube video in MP3 format.

    Args:
        url (str): The URL of the YouTube video.
        location (str, optional): The directory path where the audio file will be saved. If not provided, the default location will be used.

    Returns:
        str: The path to the downloaded MP3 audio file.
    """
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if location is None:
        location = get_variable('DEFAULT_PATH')

    audio_file = audio_stream.download(location)
    mp4_filename = audio_file.split(".mp4")[0] + ".mp4"
    mp3_filename = audio_file.split(".mp4")[0] + ".mp3"
    os.rename(mp4_filename, mp3_filename)

    return mp3_filename


def set_default_path(path: str) -> None:
    """
    Set the default path for the converted files.

    Args:
        path (str): The new default path.
    """
    with open('settings.json', 'r') as file:
        data = json.load(file)

    data['DEFAULT_PATH'] = path

    with open('settings.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_variable(var: str) -> str:
    """
    Get a variable from the settings file.

    Args:
        var (str): The name of the variable to retrieve.

    Returns:
        str: The value of the variable.
    """
    with open('settings.json', 'r') as file:
        data = json.load(file)

    return data[var]


def get_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Convert mp4 video files to mp3 audio files or perform additional "
                                                 "action.")
    parser.add_argument("url", help="URL of the video to download and convert")
    parser.add_argument("-p", "--path", help="Default Path To Download")

    return parser.parse_args()


def main() -> None:
    """
    Main function to handle command-line arguments and execute the appropriate actions.
    """
    try:
        args = get_args()

        if args.path is not None:
            set_default_path(args.default_path)
            print('Default Path set successfully')
        download_video(args.url)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
