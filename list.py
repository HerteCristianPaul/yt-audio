import subprocess


def start_yt_audio(url):
    subprocess.run(['python', 'yt-audio.py', url])


def main():
    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    urls = [url.strip() for url in urls]

    for url in urls:
        start_yt_audio(url)


if __name__ == "__main__":
    main()
