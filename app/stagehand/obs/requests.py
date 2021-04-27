def SetScene(scene_name):
    return({"request-type":"SetCurrentScene","scene-name":scene_name})

def GetSceneList():
    return {"request-type": 'GetSceneList'}

def GetSourcesList():
    return {"request-type": 'GetSourcesList'}

def ListOutputs():
    return {"request-type": 'ListOutputs'}
    
def GetVersion():
    return {"request-type": 'GetVersion'}

def GetAuthRequired():
    return {"request-type": "GetAuthRequired"}