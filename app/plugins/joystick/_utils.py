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

    sources = []

    for i in range(joysticks[name].get_numaxes()):
        sources.append(f'axis {i}')

    for i in range(joysticks[name].get_numbuttons()):
        sources.append(f'button {i}')
    
    return sources
    

def get_joystick_names():
    return [joystick.Joystick(x).get_name() for x in range(joystick.get_count())]