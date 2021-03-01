# obs

def SetCurrentScene(scene):	
	send({"request-type":"SetCurrentScene","scene-name":scene})

def GetSceneList():
    send({"request-type": 'GetSceneList'})

def GetCurrentScene(cb=empty_cb):
    send({"request-type": 'GetCurrentScene'}, lambda m: cb(m['name']))