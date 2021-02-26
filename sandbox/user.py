# user

'Whiteboard - Thinkpad'
print(locals())


def SaveCurrentScene(location='prev_scene'):
	GetCurrentScene(cb=lambda x: save(location, x))

def RestorePreviousScene(location='prev_scene'):
	SetCurrentScene(load('location'))