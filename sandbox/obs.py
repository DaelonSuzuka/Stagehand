# obs

def SetCurrentScene(scene):
	send({"request-type":"SetCurrentScene","scene-name":scene}, print)

def GetSceneList():
    send({"request-type": 'GetSceneList'}, print)

def GetCurrentScene(cb=empty_cb):
    send({"request-type": 'GetCurrentScene'}, lambda m: cb(m['name']))