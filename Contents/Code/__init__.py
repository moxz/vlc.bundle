####################################################################################################
NAME = 'VLC Player'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/vlc'

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON, ART)

	ObjectContainer.art = R(ART)	
	objectContainer.title1 = NAME

	TrackObject.thumb = R(ICON)

####################################################################################################

def MainMenu():
        oc = ObjectContainer(title1="VLC Player")
        
        mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("http://127.0.0.1:1234"))])
        
        vco = VideoClipObject(title="Play local VLC stream", url='http://127.0.0.1:1234')
        vco.add(mo)
        oc.add(vco)
        
        return oc
