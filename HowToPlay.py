import pygame
import sys
from pygame import mixer
from Music import *
from pygame.locals import *
from CurrentS import *
pygame.init()
mixer.music.load("BackgroundMusic.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.05)
screen = pygame.display.set_mode((current_sizeX(),current_sizeY()), pygame.RESIZABLE)
pygame.display.set_caption("How To Play")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
options_font = pygame.font.Font('freesansbold.ttf', 25)
title_font = pygame.font.Font('freesansbold.ttf', 60)
#You now own the region. Now you cannot move or attack you
def option_text():
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w 
    HowToPlay_title = title_font.render("How To Play", True, (255, 0, 0))
    screen.blit(HowToPlay_title, (xSize/2.56,0))
    Menu_text = options_font.render("Back To Menu", True, (255, 0, 0))
    screen.blit(Menu_text, (20,20))    
    instruction_text1 = options_font.render("Players will start with two troops, by right clicking on an area (region) not owned by them, this will be", True, (255,255,255))
    screen.blit(instruction_text1, (xSize/64,ySize/4.8))
    instruction_text2 = options_font.render("in white. You can move the troops by typing into the console the amount you want to move", True, (255,255,255))
    screen.blit(instruction_text2, (xSize/64,ySize/4))
    instruction_text3 = options_font.render("(this will be one for the time being as you must keep at least one troop in each of your owned regions).", True, (255,255,255))
    screen.blit(instruction_text3, (xSize/64,ySize/3.43))
    instruction_text4 = options_font.render("You now own the region. Now you cannot move or attack with troops (due to insufficient troops) you", True, (255,255,255))
    screen.blit(instruction_text4, (xSize/64,ySize/3))
    instruction_text5 = options_font.render("can now left click Next Turn. This will add two more troops to your starting region and will have the", True, (255,255,255))
    screen.blit(instruction_text5, (xSize/64,ySize/2.66))
    instruction_text6 = options_font.render("the oponents play out their turn. Once back to your turn you can move troops by right clicking on the", True, (255,255,255))
    screen.blit(instruction_text6, (xSize/64,ySize/2.4))
    instruction_text7 = options_font.render("region of the troops you want to move and then the owned region (indicated by the colour you have been", True, (255,255,255))
    screen.blit(instruction_text7, (xSize/64,ySize/2.2))
    instruction_text8 = options_font.render("assigned) you want to move them to then typing into the programming console the amount you want to", True, (255,255,255))
    screen.blit(instruction_text8, (xSize/64,ySize/2))
    instruction_text9 = options_font.render("send. If the troops are next to a region owned by an opponent (will be a different colour to yours and ", True, (255,255,255))
    screen.blit(instruction_text9, (xSize/64,ySize/1.85))
    instruction_text10 = options_font.render("not white) you can begin an attack where you try and move these troops into their region. Based on how", True, (255,255,255))
    screen.blit(instruction_text10, (xSize/64,ySize/1.7))
    instruction_text11 = options_font.render("many troops they have in their region and how many in your region (the one you are attacking from)", True, (255,255,255))
    screen.blit(instruction_text11, (xSize/64,ySize/1.6))
    instruction_text12 = options_font.render("you will both be given a number (random but the more troops the more likely to be higher) and if the", True, (255,255,255))
    screen.blit(instruction_text12, (xSize/64,ySize/1.5))
    instruction_text13 = options_font.render("attacker is higher they will now own the opponents region and gain two troops or if the player", True, (255,255,255))
    screen.blit(instruction_text13, (xSize/64,ySize/1.4))
    instruction_text14 = options_font.render("fortifying (defending) wins they will keep their region and the attacker loses two troops. Once there", True, (255,255,255))
    screen.blit(instruction_text14, (xSize/64,ySize/1.333))
    instruction_text15 = options_font.render("is no more to do the player can end the turn. This will continue until you either have no troops(loss)", True, (255,255,255))
    screen.blit(instruction_text15, (xSize/64,ySize/1.26))
    instruction_text16 = options_font.render("or own all regions (win)", True, (255,255,255))
    screen.blit(instruction_text16, (xSize/64,ySize/1.2))




def Exit(x,y):
    cur = pygame.mouse.get_pos()
    #print(cur)
    click = pygame.mouse.get_pressed()
    if (x < cur[0] and x + 170 > cur[0]) and (y < cur[1] and y + 22 > cur[1]):
        if click[0] == 1:
            import Menu
            sys.exit()

running = True 
while running:
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w
    if xSize < 1280 or ySize < 720:
        screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
    screen.fill((0,0,0))
    option_text()
    Exit(20,20)
    musicCheck(tick)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False
pygame.display.update()