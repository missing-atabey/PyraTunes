# First things, first. Import the wxPython package.
import wx
from Utilities.media_utils import batchDownload, download, spotifyToSearches, ytFromLink
from spotify_dl import spotify
from spotipy.oauth2 import SpotifyClientCredentials

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
        


frm = MainFrame(None,"PyraTunes",(570,200))
frm.SetIcon(wx.Icon("misc/FrameIcon.png"))

#Set up panel
pan = wx.Panel(frm)

radiolabel = wx.StaticText(pan,id=1, label="Choose a download option:", pos=(132,75))
f1label = wx.StaticText(pan, label="Enter URL:", pos=(21,20))
f12label = wx.StaticText(pan, label="Enter Target Folder Name:", pos=(351,20))



ytl = wx.RadioButton(pan, label="Youtube Link", style=0, pos=(132,95))
spp = wx.RadioButton(pan, label="Spotify Playlist", style=0, pos=(242,95))
spa = wx.RadioButton(pan, label="Spotify Album", style=0, pos=(132,110))
spt = wx.RadioButton(pan, label="Spotify Track", style=0, pos=(242,110))


url_field = wx.TextCtrl(pan, pos=(20,40), size=(320,25), name="Enter URL")
target_field = wx.TextCtrl(pan, pos=(350,40), size=(180,25), name="Enter URL")



dl_button = wx.Button(pan, label="Download", pos=(20,75), size=(102,55))

def onClickDownload(event):
    
    dp = target_field.Value
    
    if url_field.Value == "":
        return
    
    if dp == "":
        dp = "Downloads"
    
    if getOption() == "link":
        download(ytFromLink(url_field.Value), dp)
    else:
        batchDownload(spotifyToSearches(url_field.Value,getOption()),dp)
            
dl_button.Bind(wx.EVT_BUTTON, onClickDownload)



# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()