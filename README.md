# PyraTunes
A Spotify and YouTube mp3 downloader

## Dependencies
  wxPython |
  spotipy |
  pytube |
  ffmpeg |
  rich |
  sentry_sdk
  
  ## Quick Note
  Credit to the spotify-dl developers for their code which was ONLY used as a backbone for the spotify song detail retrieval (although it could easily have been 90% of this project had I decided to simply make a gui and add minimal functionality). Evidently their project does all mine can and more, but I thought it would be quite fun to use their code which utilizes spotipy and do the video download and conversion to mp3 on my own (plus the gui ofc)

## Directions for usage:
Simply access the /misc/values.py file and replace the filler values of "cid" and "cs" with your Spotify "client id" and "client secret" keys respectively. (This is not necessary if you don't intend on using the Spotify download features and only wish to use the Youtube mp3 downloader)

Open the downloader by simply running the "main.py" file. To download things simply select the type of link you want to use, input the link into the url text field, and press download. There is an optional target folder name field in which you can change the folder that'll be used to save the mp3 files. Leaving this field empty will automatically set the target folder name as "Downloads".

## Disclaimer: I am not responsible for how you decide to use this. Piracy is illegal, but It's the law that will judge you not me.

<img width="417" alt="pyra ss" src="https://user-images.githubusercontent.com/67593209/151176333-37221311-06f5-4cb9-a2e9-c17696997933.png">

<img width="675" alt="pyra ss 2" src="https://user-images.githubusercontent.com/67593209/151176351-1de1ffc1-dacb-4ce6-b5e1-cb48b2d23c24.png">
