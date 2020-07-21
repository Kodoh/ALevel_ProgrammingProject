import pygame
from pygame import mixer
import sys
import time
from Music import TickBoxCheck
from pygame.locals import *
from CurrentS import *
pygame.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.05)
screen = pygame.display.set_mode((current_sizeX(),current_sizeY()), pygame.RESIZABLE)
pygame.display.set_caption("Pause")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
options_font = pygame.font.Font('freesansbold.ttf', 25)
title_font = pygame.font.Font('freesansbold.ttf', 60)


def option_text():
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w 
    Settings_title = title_font.render("PAUSE", True, (255, 0, 0))
    screen.blit(Settings_title, (xSize/3,100))
    Resolution_text = options_font.render("Resolution", True, (255, 255, 255))
    screen.blit(Resolution_text, (xSize/3,180))
    Sound_text = options_font.render("Sound", True, (255, 255, 255))
    screen.blit(Sound_text, (xSize/3,400))
    Menu_text = options_font.render("Menu", True, (255, 255, 255))
    screen.blit(Menu_text, (xSize/3,500))  
    Unpause_text =  options_font.render("Unpause", True, (255, 255, 255))
    screen.blit(Unpause_text, (xSize/3,600))

dropDown = pygame.image.load("DropDown.JPG")

def Resolution(x,y):
    cur = pygame.mouse.get_pos()
    #print(cur)
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 135 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            print("yep")


def ResolutionOptions():
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w    
    cur = pygame.mouse.get_pos()
    #print(cur)
    click = pygame.mouse.get_pressed()
    if (xSize/3 < cur[0] and xSize/3 + 219 > cur[0]) and (210 < cur[1] and 210 + 25 > cur[1]):
        if click[0] == 1:
            screen = pygame.display.set_mode((1024,576))
    elif (xSize/3 < cur[0] and xSize/3 + 219 > cur[0]) and (234 < cur[1] and 234 + 25 > cur[1]):
        if click[0] == 1:
            screen = pygame.display.set_mode((1280,720))
    elif (xSize/3 < cur[0] and xSize/3 + 219 > cur[0]) and (265 < cur[1] and 265 + 25 > cur[1]):
        if click[0] == 1:
            screen = pygame.display.set_mode((1600,900))
    elif (xSize/3 < cur[0] and xSize/3 + 219 > cur[0]) and (295 < cur[1] and 295 + 25 > cur[1]):
        if click[0] == 1:
            screen = pygame.display.set_mode((1920,1080))
    

def Menu(x,y):
    cur = pygame.mouse.get_pos()
    #print(cur)
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 50 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            sys.exit()




running = True

def Unpause(x,y):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 110 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            global running
            running = False
            return running




while running:
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w
    if xSize < 700 or ySize < 800:
        screen = pygame.display.set_mode((700,800), pygame.RESIZABLE)
    ResolutionOptions()
    screen.fill((0,0,0))
    screen.blit(dropDown, (xSize/3,205))
    Resolution(260,180)
    current_sizeX()
    Unpause(xSize/3,600)
    current_sizeY()
    option_text()
    Menu(xSize/3,500)
    TickBoxCheck(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False
    
pygame.display.update()
