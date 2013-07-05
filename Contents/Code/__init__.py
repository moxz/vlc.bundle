####################################################################################################
NAME = 'VLC Player'
ART = 'art-default.jpg'
ICON = 'icon-default.png'
PLUGIN_PREFIX = '/video/vlc'
url_vlc = 'http://%s:%s' % (Prefs['vlc_host'], Prefs['vlc_port'])
TEXT_TITLE = 'VLC Plugin'

####################################################################################################

def Start():
	Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, NAME, ICON, ART)

	ObjectContainer.art = R(ART)	
	objectContainer.title1 = NAME

	TrackObject.thumb = R(ICON)

####################################################################################################

@handler('/video/vlc', TEXT_TITLE, thumb=ICON, art=ART)
def MainMenu():

		oc = ObjectContainer(title1="VLC Player")
        
        	mo = MediaObject(parts=[PartObject(key=HTTPLiveStreamURL("%s" % (url_vlc)))])
		vco = VideoClipObject(title="Play VLC Stream", url='%s' % (url_vlc))
        	vco.add(mo)
        	oc.add(vco)
        
		oc.add(PrefsObject(title = L('Preferences')))

		return oc
