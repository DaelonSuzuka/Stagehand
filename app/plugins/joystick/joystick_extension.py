from stagehand.sandbox import SandboxExtension
# from ._utils import get_joystick_list


class JoystickExtension(SandboxExtension):
    name = ['joystick', 'joy']

    # def __init__(self):
        # for j in get_joystick_list():
        #     print(j.get_name())