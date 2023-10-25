from pathlib import Path
import os


to_strip = [
    'opengl32sw.dll',
    'Qt6OpenGL.dll',
    'Qt6OpenGLWidgets.dll',
    'QtOpenGL.pyd',
    'Qt6Qml.pyd',
]

sizes = []
for name in to_strip:
    files = Path('dist').rglob(name)
    for f in files:
        sizes.append((f, os.path.getsize(f)))
        os.remove(f)
        # print(f)

print(sizes)
# files = Path('dist').rglob('*.dll')

# [print(f) for f in files]
