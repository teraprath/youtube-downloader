from pytube import Playlist
from utils.config import path
import os

def downloadAudio(link: str):
    playlist = Playlist(link)
    print("Converting Playlist...")
    for video in playlist.videos:
        title = video.title
        audio = video.streams.filter(only_audio=True).first()
        output = audio.download(path)
        base, ext = os.path.splitext(output)
        file = base + ".mp3"
        os.rename(output, file)
        print(title + " downloaded.")

def downloadVideo(link: str):
    playlist = Playlist(link)
    print("Converting Playlist...")
    for video in playlist.videos:
        title = video.title
        converted_video = video.streams.get_highest_resolution()
        converted_video.download(path)
        print(title + " downloaded.")