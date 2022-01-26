# PyraTunes
A Spotify and YouTube mp3 downloader

## Dependencies
  wxPython 4.1.1 |
  potipy==2.16.1 |
  pytube 11.0.2 |
  moviepy 1.0.3 |
  rich 11.0.0 |
  sentry_sdk==1.5.3
  
  ## Quick Note
  Credit to the spotify-dl developers for their code which was ONLY used as a backbone for the spotify song detail retrieval (although it could easily have been 90% of this project had I decided to simply make a gui and add minimal functionality). Evidently their project does all mine can and more, but I thought it would be quite fun to use their code which utilizes spotipy and do the video download and conversion to mp3 on my own (plus the gui ofc)

## Directions for usage:
Simply access the /misc/values.py file and replace the filler values of "cid" and "cs" with your Spotify "client id" and "client secret" keys respectively. (This is not necessary if you don't intend on using the Spotify download features and only wish to use the Youtube mp3 downloader)

Open the downloader by simply running the "main.py" file. To download things simply select the type of link you want to use, input the link into the url text field, and press download. There is an optional target folder name field in which you can change the folder that'll be used to save the mp3 files. Leaving this field empty will automatically set the target folder name as "Downloads".

## Disclaimer: I am not responsible for how you decide to use this. Piracy is illegal, however I am not judging.

