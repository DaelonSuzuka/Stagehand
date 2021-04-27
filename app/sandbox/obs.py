# obs

def GetSceneList(cb=empty_cb):
	def collect_names(message):
		cb([s['name'] for s in message['scenes']])

	send({"request-type": 'GetSceneList'}, collect_names)

def SetCurrentScene(scene):	
	send({"request-type":"SetCurrentScene","scene-name":scene})

def GetCurrentScene(cb=empty_cb):
	send({"request-type": 'GetCurrentScene'}, lambda m: cb(m['name']))