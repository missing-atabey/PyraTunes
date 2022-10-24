import imp
from pytube import *
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import sys
import subprocess
import misc
from spotify_dl import spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

keys = []
for lines in open("spotify_keys.txt"):
    keys.append(lines)
keys.pop(0)

#mp4 to mp3
def convert_to_mp3(video_file, output_ext="mp3"):

    filename = video_file[:-4]
    syatem_call = "ffmpeg -y -i \"" + filename + ".mp4\" \"" + filename + ".mp3\""
    os.system(syatem_call)


#yt video downloader
def download(yt, folder_name):
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    stream = yt.streams.filter(file_extension="mp4").first()
    stream.download(folder_name)
    convert_to_mp3(stream.get_file_path(output_path=folder_name))
    os.remove(stream.get_file_path(output_path=folder_name))
    
    o1 = yt.title
    o2 = stream.get_file_path(output_path=folder_name)
    o3 = yt.length
    
    return o1,o2,o3
    

    
#Get first result of search as yt object
def ytFromSearch(term):
    return Search(term).results[0]

def ytFromLink(link):
    return YouTube(link)

def spotifyToSearches(spotLink, s_type):
    if s_type == "track":
        song = spotify.fetch_tracks(spotify_auth(),"track", spotLink)[0]
        return [song["artist"] + " " + song["name"] + " audio"]
    elif s_type == "album":
        songs = spotify.fetch_tracks(spotify_auth(),"album", spotLink)
        terms = []
        for i in songs:
            terms = terms + [i["artist"] + " " + i["name"] + " audio"]
        return terms
    elif s_type == "playlist":
        songs = spotify.fetch_tracks(spotify_auth(),"playlist", spotLink)
        terms = []
        for i in songs:
            terms = terms + [i["artist"] + " " + i["name"] + " audio"]
            
        return terms
    
            
def spotify_auth():
    client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=keys[0],
                                                                   client_secret=keys[1]))
    return client

def batchDownload(searches, folder_name):
    for i in searches:
        download(ytFromSearch(i), folder_name)