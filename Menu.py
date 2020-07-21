import pygame
import sys
from Music import *
from pygame.locals import *
from CurrentS import *
pygame.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.05)
tick = True
screen = pygame.display.set_mode((current_sizeX(),current_sizeY()), pygame.RESIZABLE)
Sword1 = pygame.image.load("Sword.JPG")
Sword2 = pygame.image.load("SwordDown.JPG")
pygame.display.set_caption("Main Menu")
options_font = pygame.font.Font('freesansbold.ttf', 25)
title_font = pygame.font.Font('freesansbold.ttf', 60)
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

def option_text():
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w 
    Menu_title = title_font.render("MENU", True, (255, 0, 0))
    screen.blit(Menu_title, (xSize/2.3,100))
    Start_text = options_font.render("Start", True, (255, 255, 255))
    screen.blit(Start_text, (xSize/2.3,300))
    Settings_text = options_font.render("Settings", True, (255, 255, 255))
    screen.blit(Settings_text, (xSize/2.3,400))
    HowToPlay_text = options_font.render("How To Play", True, (255, 255, 255))
    screen.blit(HowToPlay_text, (xSize/2.3,500))    
    Exit_text = options_font.render("Exit", True, (255, 255, 255))
    screen.blit(Exit_text, (xSize/2.3,600))

running = True

def Exit(x,y):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 50 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            sys.exit()

def Settings(x,y):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 80 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            import Settings
            sys.exit()

def HowToPlay(x,y):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 150 > cur[0]) and (y < cur[1] and y + 25 > cur[1]):
        if click[0] == 1:
            import HowToPlay
            sys.exit()


while running:
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w
    screen.fill((0,0,0))
    if xSize < 700 or ySize < 800:
        screen = pygame.display.set_mode((700,800), pygame.RESIZABLE)
    option_text()
    current_sizeX()
    current_sizeY()
    Exit(xSize/2.3,600)
    musicCheck(tick)
    HowToPlay(xSize/2.3,500)
    Settings(xSize/2.3,400)
    current_sizeX()
    current_sizeY()
    screen.blit(Sword1, (0,0))
    screen.blit(Sword2, ((xSize - 180),0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False
pygame.display.update()

