# First things, first. Import the wxPython package.
from concurrent.futures import thread
from tracemalloc import start
from turtle import pos
from numpy import size, true_divide
import wx
from wx.adv import *
from Utilities.media_utils import batchDownload, download, spotifyToSearches, ytFromLink
import misc
from spotify_dl import spotify
from spotipy.oauth2 import SpotifyClientCredentials
import threading
from multiprocessing import Process
import ctypes
import time

#Account for high DPI screens on windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


# Next, create an application object.
app = wx.App()

class MainFrame(wx.Frame):
    def __init__(self, parent, mytitle, mysize):
        wx.Frame.__init__(self, parent, wx.ID_ANY, mytitle, size=mysize,
            style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX)
        

def getOption():
    if ytl.Value:
        return "link"
    elif spp.Value:
        return "playlist"
    elif spa.Value:
        return "album"
    elif spt.Value:
        return "track"
    else:
        return -1
        


frm = MainFrame(None,"PyraTunes",(680,230))
frm.SetIcon(wx.Icon("misc/FrameIcon.png"))

#Set up panel
pan = wx.Panel(frm)

radiolabel = wx.StaticText(pan,id=1, label="Choose a download option:", pos=(132,75))
f1label = wx.StaticText(pan, label="Enter URL:", pos=(21,15))
f12label = wx.StaticText(pan, label="Enter Target Folder Name:", pos=(351,15))


ytl = wx.RadioButton(pan, label="Youtube Link", style=0, pos=(132,100))
spp = wx.RadioButton(pan, label="Spotify Playlist", style=0, pos=(285,100))
spa = wx.RadioButton(pan, label="Spotify Album", style=0, pos=(132,125))
spt = wx.RadioButton(pan, label="Spotify Track", style=0, pos=(285,125))


url_field = wx.TextCtrl(pan, pos=(20,40), size=(320,30), name="Enter URL")
target_field = wx.TextCtrl(pan, pos=(390,40), size=(250,30), name="Enter directory")
target_field.SetHint("Downloads")

dl_button = wx.Button(pan, label="Download", pos=(20,80), size=(102,55))

folder_img = wx.Image("misc/folder.png")
folder_img = folder_img.Scale(26,26, wx.IMAGE_QUALITY_HIGH)
dir_button = wx.BitmapButton(pan, bitmap=folder_img.ConvertToBitmap(), pos=(350,40))

loading_anim = wx.ActivityIndicator(parent=pan, size=(50 , 50), pos=(550 , 90))
loading_anim.Hide()

#DL Button Background Function
def dlfunc():
    dp = target_field.Value
    
    if url_field.Value == "":
        loading_anim.Stop()
        loading_anim.Hide()
        return
    
    if dp == "":
        dp = "Downloads"
    
    if getOption() == "link":
        download(ytFromLink(url_field.Value), dp)
    else:
        batchDownload(spotifyToSearches(url_field.Value, getOption()),dp)
    
    loading_anim.Stop()
    loading_anim.Hide()

#Define directory button functionality
def onClickDirectory(event):
    dlg = wx.DirDialog(None, "Select folder to download in", "Downloads", wx.DD_DEFAULT_STYLE)
    if dlg.ShowModal() == wx.ID_OK:
        target_field.SetValue(dlg.GetPath())
    dlg.Destroy()

#Define Download Button functionality
def onClickDownload(event):
    loading_anim.Show()
    loading_anim.Start()
    thread_downloader = threading.Thread(target=dlfunc)
    thread_downloader.start()     
            
dl_button.Bind(wx.EVT_BUTTON, onClickDownload)
dir_button.Bind(wx.EVT_BUTTON, onClickDirectory)

# Show frame.
frm.Show()

#Gui Thread Start
app.MainLoop()