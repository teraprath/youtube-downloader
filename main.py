from utils import video, playlist, channel
from sys import exit

type = None
format = None

def menue():
    checkType()

def checkType():
    global type
    while True:
        print("\nWhat do you want to download?:")
        print("(1) Video")
        print("(2) Playlist")
        print("(3) Channel")
        option = int(input("\nEnter Number (1/2/3): "))
        options = {
            1: "video",
            2: "playlist",
            3: "channel"
        }
        if option in options:
            type = options[option]
            checkFormat()
        else: print(f"\nFailed! '{option}' is not an option.")
        input("Press [ENTER] to continue...")

def checkFormat():
    global format
    while True:
        print("\nWhich file format do you want?")
        print("(1) Video (.mp4)")
        print("(2) Audio (.mp3)")
        option = int(input("\nEnter Number (1/2): "))
        options = {
            1: "video",
            2: "audio"
        }
        if option in options:
            format = options[option]
            download()
        else: print(f"\nFailed! '{option}' is not an option.")
        input("\nPress [ENTER] to continue...")

def download():
    link = input("\nEnter YouTube-Link: ")
    if type == "video":
        if format == "video": video.downloadVideo(link)
        if format == "audio": video.downloadAudio(link)
    if type == "playlist":
        if format == "video": playlist.downloadVideo(link)
        if format == "audio": playlist.downloadAudio(link)
    if type == "channel":
        if format == "video": channel.downloadVideo(link)
        if format == "audio": channel.downloadAudio(link)


    x = input("\nConvert another Video? (Y/n): ")
    if x.lower() == "y": checkType()
    exit("Thanks.")
    


if __name__ == "__main__":
    menue()