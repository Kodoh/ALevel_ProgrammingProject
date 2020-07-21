import pygame
from pygame.locals import *

def current_sizeX():
    xSize = pygame.display.Info().current_w
    return xSize

def current_sizeY():
    ySize = pygame.display.Info().current_h 
    return ySize