import os
import sys
import getopt
from pathlib import Path
from pytube import YouTube


def main():
    download_path = str(Path.home() / "Downloads")

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "u:", ["url="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for opt, val in opts:
        if opt == '-u':
            url = val
        elif opt == '--url':
            url = val
        else:
            print("No URL provided")
            sys.exit(2)

        video = YouTube(url)
        video.streams.get_highest_resolution().download(download_path)
        print(f"Video downloaded to {download_path}")
        os.startfile(download_path)


if __name__ == '__main__':
    main()
