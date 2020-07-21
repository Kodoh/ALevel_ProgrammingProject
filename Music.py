import pygame
from pygame import mixer
import time
tick = True
def TickBoxCheck(screen):
    global tick
    time.sleep(0.1)
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w     
    if pygame.mixer.music.get_busy() == 1: 
        TickedboxImg = pygame.image.load("SoundTick.JPG")
        screen.blit(TickedboxImg, ((xSize/3 + 100),385))
        tick = True 
    else:
        UntickedboxImg = pygame.image.load("SoundUnticked.JPG")
        screen.blit(UntickedboxImg, ((xSize/3 + 100),385))
        tick = False
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if ((xSize/3 + 100) < cur[0] and (xSize/3 + 100) + 50 > cur[0]) and (385 < cur[1] and 385 + 50 > cur[1]):
        if click[0] == 1:
            if tick == True:
                pygame.mixer.music.stop()
            elif tick == False:
                pygame.mixer.music.play()
    return tick


def musicCheck(TickBoxCheck):
    if tick == False:
        pygame.mixer.music.stop()