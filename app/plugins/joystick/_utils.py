import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
from pygame import joystick


pygame.init()
joystick.init()


def get_joysticks():
    return {joystick.Joystick(x).get_name(): joystick.Joystick(x) for x in range(joystick.get_count())}


def get_joystick_sources(name):
    joysticks = get_joysticks()

    if name not in joysticks:
        return

    sources = {
        'axes': [],
        'buttons': [],
        'hats': [],
    }

    for i in range(joysticks[name].get_numaxes()):
        sources['axes'].append(i)

    for i in range(joysticks[name].get_numbuttons()):
        sources['buttons'].append(i)

    for i in range(joysticks[name].get_numhats()):
        sources['hats'].append(i)

    return sources


def get_joystick_names():
    return [joystick.Joystick(x).get_name() for x in range(joystick.get_count())]
