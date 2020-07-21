import pygame
import sys
from pygame import mixer
from Music import *
from pygame.locals import *
from CurrentS import *
from Troops import *
import random
import time 



pygame.init()
pygame.display.set_caption("Map")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1400,900))
Player1Troop2 = PlayerTroop1("Player1TroopIdle.JPG.png") 
Player1Troop1 = PlayerTroop1("Player1TroopIdle.JPG.png")
Player2Troop1 = PlayerTroop1("Player2TroopIdle.JPG.png")
Player2Troop2 = PlayerTroop1("Player2TroopIdle.JPG.png")
Player3Troop1 = PlayerTroop1("Player3TroopIdle.JPG.png")
Player3Troop2 = PlayerTroop1("Player3TroopIdle.JPG.png")
Player3Troop3 = PlayerTroop1("Player3TroopIdle.JPG.png")
xSize = pygame.display.Info().current_w
ySize = pygame.display.Info().current_h

options_font = pygame.font.Font('freesansbold.ttf', 25)
title_font = pygame.font.Font('freesansbold.ttf', 60)

def option_text():
    xSize = pygame.display.Info().current_w
    ySize = pygame.display.Info().current_h
    Menu_title = title_font.render("Next Turn", True, (255, 0, 0))
    screen.blit(Menu_title, (xSize - 300,ySize - 50))

NextTurnList = [1,2,3]
def NextTurn(NextTurnList):
    R1MinMax = (xSize - 350,xSize - 160,ySize - 450,ySize - 336)
    R2MinMax = (xSize - 425,xSize - 200,ySize - 700,ySize - 560)
    R3MinMax = (xSize - 427,xSize - 198,ySize - 735,ySize - 708)
    R4MinMax = (xSize - 450,xSize - 150,ySize - 560,ySize - 450)
    R5MinMax = (xSize - 463,xSize - 426,ySize - 390,ySize - 295)
    R6MinMax = (xSize - 310,xSize - 238,ySize - 233,ySize - 138)
    R7MinMax = (xSize - 235,xSize - 179,ySize - 234,ySize - 140)
    R8MinMax = (xSize - 384,xSize - 310,ySize - 240,ySize - 128)
    R9MinMax = (xSize - 765,xSize - 639,ySize - 560,ySize - 326)
    R10MinMax = (xSize - 709,xSize - 560,ySize - 751,ySize - 676)
    R11MinMax = (xSize - 973,xSize - 893,ySize - 773,ySize - 666)
    R12MinMax = (xSize - 974,xSize - 918,ySize - 663,ySize - 613)
    R13MinMax = (xSize - 1146,xSize - 993,ySize - 662,ySize - 488)
    R14MinMax = (xSize - 1155,xSize - 975, ySize - 780, ySize - 665)
    R15MinMax = (xSize - 1056,xSize - 900,ySize - 428,ySize - 323)
    R16MinMax = (xSize - 1061,xSize - 904,ySize - 332,ySize - 221)
    R17MinMax = (xSize - 1080,xSize - 932,ySize - 210,ySize - 161)
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (xSize - 300 < cur[0] and xSize > cur[0]) and (ySize - 50 < cur[1] and ySize > cur[1]):
        if click[0] == 1:
            global RegionOption 
            if len(NextTurnList) == 3:
                if len(Troop2) > 0:
                    Player2Move()
                    Player2Troop3 = PlayerTroop1("Player2TroopIdle.JPG.png")
                    Troop2.append(Player2Troop3)
                    Troop2_14.append(Player2Troop3)
                    AllTroops.append(Player2Troop3)
                    all_sprites_list.add(Player2Troop3)
                    Player2Troop3.rect.x = 400
                    Player2Troop3.rect.y = 200
                    NextTurnList.remove(1)
                if len(Troop3) > 0:
                    Player3Move()
                    Player3Troop3 = PlayerTroop1("Player3TroopIdle.JPG.png")
                    Troop3_16.append(Player3Troop3)
                    Troop3.append(Player3Troop3)
                    AllTroops.append(Player3Troop3)
                    all_sprites_list.add(Player3Troop3)
                    Player3Troop3.rect.x = 350
                    Player3Troop3.rect.y = 700
                if len(Troop1) > 0:
                    Player1Troop3 = PlayerTroop1("Player1TroopIdle.JPG.png")
                    Troop1.append(Player1Troop3)
                    Troop1_4.append(Player1Troop3)
                    AllTroops.append(Player1Troop3)
                    all_sprites_list.add(Player1Troop3)
                    Player1Troop3.rect.x = 1050
                    Player1Troop3.rect.y = 400
            elif len(NextTurnList) == 2:
                if len(Troop2) > 0:
                    Player2Move()
                    Player2Troop4 = PlayerTroop1("Player2TroopIdle.JPG.png")
                    Troop2.append(Player2Troop4)
                    Troop2_14.append(Player2Troop4)
                    AllTroops.append(Player2Troop4)
                    all_sprites_list.add(Player2Troop4)
                    Player2Troop4.rect.x = 450
                    Player2Troop4.rect.y = 200
                if len(Troop3) > 0:
                    Player3Move()
                    Player3Troop4 = PlayerTroop1("Player3TroopIdle.JPG.png")
                    Troop3_16.append(Player3Troop4)
                    Troop3.append(Player3Troop4)
                    AllTroops.append(Player3Troop4)
                    all_sprites_list.add(Player3Troop4)
                    Player3Troop4.rect.x = 400
                    Player3Troop4.rect.y = 700
                if len(Troop1) > 0:
                    Player1Troop4 = PlayerTroop1("Player1TroopIdle.JPG.png")
                    Troop1.append(Player1Troop4)
                    Troop1_4.append(Player1Troop4)
                    AllTroops.append(Player1Troop4)
                    all_sprites_list.add(Player1Troop4)
                    Player1Troop4.rect.x = 1150
                    Player1Troop4.rect.y = 400
                    NextTurnList.remove(2) 
            elif len(NextTurnList) == 1:
                if len(Troop2) > 0:
                    Player2Move()
                    Player2Troop5 = PlayerTroop1("Player2TroopIdle.JPG.png")
                    Troop2.append(Player2Troop5)
                    Troop2_14.append(Player2Troop5)
                    AllTroops.append(Player2Troop5)
                    all_sprites_list.add(Player2Troop5)
                    Player2Troop5.rect.x = 400
                    Player2Troop5.rect.y = 200
                if len(Troop3) > 0:
                    Player3Move()
                    Player3Troop5 = PlayerTroop1("Player3TroopIdle.JPG.png")
                    Troop3_16.append(Player3Troop5)
                    Troop3.append(Player3Troop5)
                    AllTroops.append(Player3Troop5)
                    all_sprites_list.add(Player3Troop5)
                    Player3Troop5.rect.x = 450
                    Player3Troop5.rect.y = 700
                if len(Troop1) > 0:
                    Player1Troop5 = PlayerTroop1("Player1TroopIdle.JPG.png")
                    Troop1.append(Player1Troop5)
                    Troop1_4.append(Player1Troop5)
                    AllTroops.append(Player1Troop5)
                    all_sprites_list.add(Player1Troop5)
                    Player1Troop5.rect.x = 1160
                    Player1Troop5.rect.y = 400
            RegionOption = int(input("What region would you like to select: "))                



running = True
AllTroops = []
Troop1 = []

Troop1_1 = []
Troop1_2 = []
Troop1_3 = []
Troop1_4 = []
Troop1_5 = []
Troop1_6 = []
Troop1_7 = []
Troop1_8 = []
Troop1_9 = []
Troop1_10 = []
Troop1_11 = []
Troop1_12 = []
Troop1_13 = []
Troop1_14 = []
Troop1_15 = []
Troop1_16 = []
Troop1_17 = []

Troop2_1 = []
Troop2_2 = []
Troop2_3 = []
Troop2_4 = []
Troop2_5 = []
Troop2_6 = []
Troop2_7 = []
Troop2_8 = []
Troop2_9 = []
Troop2_10 = []
Troop2_11 = []
Troop2_12 = []
Troop2_13 = []
Troop2_14 = []
Troop2_15 = []
Troop2_16 = []
Troop2_17 = []

Troop3_1 = []
Troop3_2 = []
Troop3_3 = []
Troop3_4 = []
Troop3_5 = []
Troop3_6 = []
Troop3_7 = []
Troop3_8 = []
Troop3_9 = []
Troop3_10 = []
Troop3_11 = []
Troop3_12 = []
Troop3_13 = []
Troop3_14 = []
Troop3_15 = []
Troop3_16 = []
Troop3_17 = []


Troop2 = []
Troop2B = []
Troop2C = []
Troop2D = []
Troop3 = []
Troop3B = []
Troop3C = []
AllTroop1 = []
AllTroop2 = []
AllTroop3 = []






Troop1.append(Player1Troop1)
Troop1.append(Player1Troop2)
Troop2.append(Player2Troop1)
Troop2.append(Player2Troop2)
Troop3.append(Player3Troop1)
Troop3.append(Player3Troop2)
Troop3.append(Player3Troop3)

AllTroops.append(Player1Troop1)
AllTroops.append(Player1Troop2)
AllTroops.append(Player2Troop1)
AllTroops.append(Player2Troop2)
AllTroops.append(Player3Troop1)
AllTroops.append(Player3Troop2)
AllTroops.append(Player3Troop3)

Troop1_4.append(Player1Troop1)
Troop1_4.append(Player1Troop2)
#Troop1_4.append(Player1Troop3)
Troop2_14.append(Player2Troop1)
Troop2_14.append(Player2Troop2)
Troop3_16.append(Player3Troop1)
Troop3_16.append(Player3Troop2)
Troop3_1.append(Player3Troop3)

AllTroop1.append(Player1Troop1)
AllTroop1.append(Player1Troop2)
AllTroop2.append(Player2Troop1)
AllTroop2.append(Player2Troop2)
AllTroop3.append(Player3Troop1)
AllTroop3.append(Player3Troop2)
AllTroop3.append(Player3Troop3)


R1MinMax = (xSize - 350,xSize - 160,ySize - 450,ySize - 336)
R2MinMax = (xSize - 425,xSize - 200,ySize - 700,ySize - 560)
R3MinMax = (xSize - 427,xSize - 198,ySize - 735,ySize - 708)
R4MinMax = (xSize - 450,xSize - 150,ySize - 560,ySize - 450)
R5MinMax = (xSize - 463,xSize - 426,ySize - 390,ySize - 295)
R6MinMax = (xSize - 310,xSize - 238,ySize - 233,ySize - 138)
R7MinMax = (xSize - 235,xSize - 179,ySize - 234,ySize - 140)
R8MinMax = (xSize - 384,xSize - 310,ySize - 240,ySize - 128)
R9MinMax = (xSize - 765,xSize - 639,ySize - 560,ySize - 326)
R10MinMax = (xSize - 709,xSize - 560,ySize - 751,ySize - 676)
R11MinMax = (xSize - 973,xSize - 893,ySize - 773,ySize - 666)
R12MinMax = (xSize - 974,xSize - 918,ySize - 663,ySize - 613)
R13MinMax = (xSize - 1146,xSize - 993,ySize - 662,ySize - 488)
R14MinMax = (xSize - 1155,xSize - 975, ySize - 780, ySize - 665)
R15MinMax = (xSize - 1056,xSize - 900,ySize - 428,ySize - 323)
R16MinMax = (xSize - 1061,xSize - 904,ySize - 332,ySize - 221)
R17MinMax = (xSize - 1080,xSize - 932,ySize - 210,ySize - 161)

all_sprites_list = pygame.sprite.Group() 
ySize = pygame.display.Info().current_h 
xSize = pygame.display.Info().current_w
all_sprites_list.add(Player1Troop2)
all_sprites_list.add(Player1Troop1)
Player2Troop1.rect.x = (R14MinMax[0] + R14MinMax[1]) / 2 + 20
Player2Troop1.rect.y = (R14MinMax[2] + R14MinMax[3]) / 2 
Player2Troop2.rect.x = ((R14MinMax[0] + R14MinMax[1]) / 2) - 20
Player2Troop2.rect.y = ((R14MinMax[2] + R14MinMax[3]) / 2) 
Player3Troop1.rect.x = ((R16MinMax[0] + R16MinMax[1]) / 2)
Player3Troop1.rect.y = ((R16MinMax[2] + R16MinMax[3]) / 2)
Player3Troop2.rect.x = ((R16MinMax[0] + R16MinMax[1]) / 2) 
Player3Troop2.rect.y = ((R16MinMax[2] + R16MinMax[3]) / 2) - 40
Player1Troop1.rect.x = ((R4MinMax[0] + R4MinMax[1]) / 2)
Player1Troop1.rect.y = ((R4MinMax[2] + R4MinMax[3]) / 2)
Player1Troop2.rect.x = ((R4MinMax[0] + R4MinMax[1]) / 2) + 50
Player1Troop2.rect.y = ((R4MinMax[2] + R4MinMax[3]) / 2) 
Player3Troop3.rect.x = 1150
Player3Troop3.rect.y = 500



all_sprites_list.add(Player3Troop1)
all_sprites_list.add(Player3Troop2)
all_sprites_list.add(Player2Troop1)
all_sprites_list.add(Player2Troop2)
all_sprites_list.add(Player3Troop3)

Background = "Map.png"


cur = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()
#constants 



def Player2Move():
    R1MinMax = (1050, 1240,450,564)
    R2MinMax = (975, 1200, 200, 340)
    R3MinMax = (973, 1202, 166, 192)
    R4MinMax = (950, 1250, 340, 450)
    R5MinMax = (937, 974, 510, 605)
    R6MinMax = (1090, 1162, 647, 762)
    R7MinMax = (1165, 1221, 646, 760)
    R8MinMax = (1016, 1090, 660, 772)
    R9MinMax = (635, 761, 337, 374)
    R10MinMax = (691, 840, 149, 224)
    R11MinMax = (427, 507, 127, 234)
    R12MinMax = (426, 482, 237, 287)
    R13MinMax = (254, 407, 238, 412)
    R14MinMax = (245, 425, 121, 236)
    R15MinMax = (344, 500, 472, 577)
    R16MinMax = (339, 496, 568, 679)
    R17MinMax = (320, 468, 690, 739)
    #1
        #1
    if len(Troop2_1) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_4) >= 1:
                Botattack(Troop2_1,Troop1_4,Troop2_4,R4MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_4) >= 1:
                Botattack(Troop2_1,Troop3_4,Troop2_4,R4MinMax,R16MinMax,R14MinMax)
            if len(Troop2_4) >= 1:
                count = 1
                for i in Troop2_1:
                    if count >= len(Troop2_1):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_1.remove(i)
                        Troop2_4.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_1.remove(i)
                        Troop2_4.append(i)
                    count += 1
            if len(Troop2_4) == 0:
                if len(Troop1_4) == 0:
                    if len(Troop3_4) == 0:
                            count = 1
                            for i in Troop2_1:
                                if count >= len(Troop2_1):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_1.remove(i)
                                    Troop2_4.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_1.remove(i)
                                    Troop2_4.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_5) >= 1:
                Botattack(Troop2_1,Troop3_5,Troop2_5,R5MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_5) >= 1:
                Botattack(Troop2_1,Troop1_5,Troop2_5,R5MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_5) >= 1:
                count = 1 
                for i in Troop2_1:
                    if count >= len(Troop2_1):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_1.remove(i)
                        Troop2_5.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_1.remove(i)
                        Troop2_5.append(i)
                    count += 1  
            if len(Troop2_5) == 0:
                if len(Troop1_5) == 0:
                    if len(Troop3_5) == 0:
                            count = 1
                            for i in Troop2_1:
                                if count >= len(Troop2_1):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_1.remove(i)
                                    Troop2_5.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_1.remove(i)
                                    Troop2_5.append(i)
                                count += 1
        else:
            if len(Troop3_6) >= 1:
                Botattack(Troop2_1,Troop3_6,Troop2_6,R6MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_6) >= 1:
                Botattack(Troop2_1,Troop1_6,Troop2_6,R6MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_6) >= 1:
                count = 1 
                for i in Troop2_1:
                    if count >= len(Troop2_1):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_1.remove(i)
                        Troop2_6.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_1.remove(i)
                        Troop2_6.append(i)
                    count += 1  
            if len(Troop2_6) == 0:
                if len(Troop1_6) == 0:
                    if len(Troop3_6) == 0:
                            count = 1
                            for i in Troop2_1:
                                if count >= len(Troop2_1):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_1.remove(i)
                                    Troop2_6.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_1.remove(i)
                                    Troop2_6.append(i)
                                count += 1
            
        #1
    if len(Troop2_2) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_3) >= 1:
                Botattack(Troop2_2,Troop1_3,Troop2_3,R3MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_3) >= 1:
                Botattack(Troop2_2,Troop3_3,Troop2_3,R3MinMax,R16MinMax,R14MinMax)
            if len(Troop2_3) >= 1:
                count = 1
                for i in Troop2_2:
                    if count >= len(Troop2_2):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_2.remove(i)
                        Troop2_3.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_2.remove(i)
                        Troop2_3.append(i)
                    count += 1
            if len(Troop2_3) == 0:
                if len(Troop1_3) == 0:
                    if len(Troop3_3) == 0:
                            count = 1
                            for i in Troop2_2:
                                if count >= len(Troop2_2):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_2.remove(i)
                                    Troop2_3.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_2.remove(i)
                                    Troop2_3.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_4) >= 1:
                Botattack(Troop2_2,Troop3_4,Troop2_4,R4MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_4) >= 1:
                Botattack(Troop2_2,Troop1_4,Troop2_4,R4MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_4) >= 1:
                count = 1 
                for i in Troop2_2:
                    if count >= len(Troop2_2):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_2.remove(i)
                        Troop2_4.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_2.remove(i)
                        Troop2_4.append(i)
                    count += 1  
            if len(Troop2_4) == 0:
                if len(Troop1_4) == 0:
                    if len(Troop3_4) == 0:
                            count = 1
                            for i in Troop2_2:
                                if count >= len(Troop2_2):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_2.remove(i)
                                    Troop2_4.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_2.remove(i)
                                    Troop2_4.append(i)
                                count += 1
        #1
    if len(Troop2_3) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_10) >= 1:
                Botattack(Troop2_3,Troop1_10,Troop2_10,R10MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_10) >= 1:
                Botattack(Troop2_3,Troop3_10,Troop2_10,R10MinMax,R16MinMax,R14MinMax)
            if len(Troop2_10) >= 1:
                count = 1
                for i in Troop2_3:
                    if count >= len(Troop2_3):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_3.remove(i)
                        Troop2_10.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_3.remove(i)
                        Troop2_10.append(i)
                    count += 1
            if len(Troop2_10) == 0:
                if len(Troop1_10) == 0:
                    if len(Troop3_10) == 0:
                            count = 1
                            for i in Troop2_3:
                                if count >= len(Troop2_3):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_3.remove(i)
                                    Troop2_10.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_3.remove(i)
                                    Troop2_10.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_2) >=  1:
                Botattack(Troop2_3,Troop3_2,Troop2_2,R2MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_2) >= 1:
                Botattack(Troop2_3,Troop1_2,Troop2_2,R2MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_2) >= 1:
                count = 1 
                for i in Troop2_3:
                    if count >= len(Troop2_3):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_3.remove(i)
                        Troop2_2.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_3.remove(i)
                        Troop2_2.append(i)
                    count += 1  
            if len(Troop2_2) == 0:
                if len(Troop1_2) == 0:
                    if len(Troop3_2) == 0:
                            count = 1
                            for i in Troop2_3:
                                if count >= len(Troop2_3):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_3.remove(i)
                                    Troop2_2.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_3.remove(i)
                                    Troop2_2.append(i)
                                count += 1
        #1
    if len(Troop2_4) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_2) >= 1:
                Botattack(Troop2_4,Troop1_2,Troop2_2,R4MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_2) >= 1:
                Botattack(Troop2_4,Troop3_2,Troop2_2,R4MinMax,R16MinMax,R14MinMax)
            if len(Troop2_2) >= 1:
                count = 1
                for i in Troop2_4:
                    if count >= len(Troop2_4):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_4.remove(i)
                        Troop2_2.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_4.remove(i)
                        Troop2_2.append(i)
                    count += 1
            if len(Troop2_2) == 0:
                if len(Troop1_2) == 0:
                    if len(Troop3_2) == 0:
                            count = 1
                            for i in Troop2_4:
                                if count >= len(Troop2_4):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_4.remove(i)
                                    Troop2_2.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_4.remove(i)
                                    Troop2_2.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_1) >= 1:
                Botattack(Troop2_4,Troop3_1,Troop2_1,R1MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_1) >= 1:
                Botattack(Troop2_4,Troop1_1,Troop2_1,R1MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_1) >= 1:
                count = 1 
                for i in Troop2_4:
                    if count >= len(Troop2_4):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_4.remove(i)
                        Troop2_1.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_4.remove(i)
                        Troop2_1.append(i)
                    count += 1  
            if len(Troop2_1) == 0:
                if len(Troop1_1) == 0:
                    if len(Troop3_1) == 0:
                            count = 1
                            for i in Troop2_4:
                                if count >= len(Troop2_4):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_4.remove(i)
                                    Troop2_1.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_4.remove(i)
                                    Troop2_1.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_9) >= 1:
                Botattack(Troop2_1,Troop3_9,Troop2_9,R9MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_9) >= 1:
                Botattack(Troop2_1,Troop1_9,Troop2_9,R9MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_9) >= 1:
                count = 1 
                for i in Troop2_4:
                    if count >= len(Troop2_4):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_4.remove(i)
                        Troop2_9.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_4.remove(i)
                        Troop2_9.append(i)
                    count += 1  
            if len(Troop2_9) == 0:
                if len(Troop1_9) == 0:
                    if len(Troop3_9) == 0:
                            count = 1
                            for i in Troop2_4:
                                if count >= len(Troop2_4):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_4.remove(i)
                                    Troop2_9.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_4.remove(i)
                                    Troop2_9.append(i)
                                count += 1
        #1
    if len(Troop2_5) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_1) >= 1:
                Botattack(Troop2_5,Troop1_1,Troop2_1,R1MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_1) >= 1:
                Botattack(Troop2_5,Troop3_1,Troop2_1,R1MinMax,R16MinMax,R14MinMax)
            if len(Troop2_1) >= 1:
                count = 1
                for i in Troop2_5:
                    if count >= len(Troop2_5):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_5.remove(i)
                        Troop2_1.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_5.remove(i)
                        Troop2_1.append(i)
                    count += 1
            if len(Troop2_1) == 0:
                if len(Troop1_1) == 0:
                    if len(Troop3_1) == 0:
                            count = 1
                            for i in Troop2_5:
                                if count >= len(Troop2_5):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_5.remove(i)
                                    Troop2_1.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_5.remove(i)
                                    Troop2_1.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_6) >= 1:
                Botattack(Troop2_5,Troop3_6,Troop2_6,R6MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_6) >= 1:
                Botattack(Troop2_5,Troop1_6,Troop2_6,R6MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_6) >= 1:
                count = 1 
                for i in Troop2_5:
                    if count >= len(Troop2_5):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_5.remove(i)
                        Troop2_6.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_5.remove(i)
                        Troop2_6.append(i)
                    count += 1  
            if len(Troop2_6) == 0:
                if len(Troop1_6) == 0:
                    if len(Troop3_6) == 0:
                            count = 1
                            for i in Troop2_5:
                                if count >= len(Troop2_5):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_5.remove(i)
                                    Troop2_6.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_5.remove(i)
                                    Troop2_6.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_16) >= 1:
                Botattack(Troop2_5,Troop3_16,Troop2_16,R16MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_16) >= 1:
                Botattack(Troop2_5,Troop1_16,Troop2_16,R16MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_16) >= 1:
                count = 1 
                for i in Troop2_5:
                    if count >= len(Troop2_5):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_5.remove(i)
                        Troop2_16.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_5.remove(i)
                        Troop2_16.append(i)
                    count += 1  
            if len(Troop2_16) == 0:
                if len(Troop1_16) == 0:
                    if len(Troop3_16) == 0:
                            count = 1
                            for i in Troop2_5:
                                if count >= len(Troop2_5):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_5.remove(i)
                                    Troop2_16.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_5.remove(i)
                                    Troop2_16.append(i)
                                count += 1
        #1
    if len(Troop2_6) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_7) >= 1:
                Botattack(Troop2_6,Troop1_7,Troop2_7,R7MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_7) >= 1:
                Botattack(Troop2_6,Troop3_7,Troop2_7,R7MinMax,R16MinMax,R14MinMax)
            if len(Troop2_7) >= 1:
                count = 1
                for i in Troop2_6:
                    if count >= len(Troop2_6):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_6.remove(i)
                        Troop2_7.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_6.remove(i)
                        Troop2_7.append(i)
                    count += 1
            if len(Troop2_7) == 0:
                if len(Troop1_7) == 0:
                    if len(Troop3_7) == 0:
                            count = 1
                            for i in Troop2_6:
                                if count >= len(Troop2_6):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_6.remove(i)
                                    Troop2_7.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_6.remove(i)
                                    Troop2_7.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_8) >= 1:
                Botattack(Troop2_6,Troop3_8,Troop2_8,R8MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_8) >= 1:
                Botattack(Troop2_6,Troop1_8,Troop2_8,R8MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_8) >= 1:
                count = 1 
                for i in Troop2_6:
                    if count >= len(Troop2_6):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_6.remove(i)
                        Troop2_8.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_6.remove(i)
                        Troop2_8.append(i)
                    count += 1  
            if len(Troop2_8) == 0:
                if len(Troop1_8) == 0:
                    if len(Troop3_8) == 0:
                            count = 1
                            for i in Troop2_6:
                                if count >= len(Troop2_6):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_6.remove(i)
                                    Troop2_8.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_6.remove(i)
                                    Troop2_8.append(i)
                                count += 1
        #1
    if len(Troop2_7) > 1:
        RanChoice = random.randint(1,1)
        if RanChoice == 1:
            if len(Troop1_6) >= 1:
                Botattack(Troop2_7,Troop1_6,Troop2_6,R6MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_6) >= 1:
                Botattack(Troop2_7,Troop3_6,Troop2_6,R6MinMax,R16MinMax,R14MinMax)
            if len(Troop2_6) >= 1:
                count = 1
                for i in Troop2_7:
                    if count >= len(Troop2_7):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_7.remove(i)
                        Troop2_6.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_7.remove(i)
                        Troop2_6.append(i)
                    count += 1
            if len(Troop2_6) == 0:
                if len(Troop1_6) == 0:
                    if len(Troop3_6) == 0:
                            count = 1
                            for i in Troop2_7:
                                if count >= len(Troop2_7):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_7.remove(i)
                                    Troop2_6.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_7.remove(i)
                                    Troop2_6.append(i)
                                count += 1
        #1
    if len(Troop2_8) > 1:
        RanChoice = random.randint(1,1)
        if RanChoice == 1:
            if len(Troop1_6) >= 1:
                Botattack(Troop2_8,Troop1_6,Troop2_6,R6MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_6) >= 1:
                Botattack(Troop2_8,Troop3_6,Troop2_6,R6MinMax,R16MinMax,R14MinMax)
            if len(Troop2_6) >= 1:
                count = 1
                for i in Troop2_8:
                    if count >= len(Troop2_8):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_8.remove(i)
                        Troop2_6.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_8.remove(i)
                        Troop2_6.append(i)
                    count += 1
            if len(Troop2_6) == 0:
                if len(Troop1_6) == 0:
                    if len(Troop3_6) == 0:
                            count = 1
                            for i in Troop2_8:
                                if count >= len(Troop2_8):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_8.remove(i)
                                    Troop2_6.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_8.remove(i)
                                    Troop2_6.append(i)
                                count += 1
        #1
    if len(Troop2_9) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_4) >= 1:
                Botattack(Troop2_9,Troop1_4,Troop2_4,R4MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_4) >= 1:
                Botattack(Troop2_9,Troop3_4,Troop2_4,R4MinMax,R16MinMax,R14MinMax)
            if len(Troop2_4) >= 1:
                count = 1
                for i in Troop2_9:
                    if count >= len(Troop2_9):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_9.remove(i)
                        Troop2_4.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_9.remove(i)
                        Troop2_4.append(i)
                    count += 1
            if len(Troop2_4) == 0:
                if len(Troop1_4) == 0:
                    if len(Troop3_4) == 0:
                            count = 1
                            for i in Troop2_9:
                                if count >= len(Troop2_9):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_9.remove(i)
                                    Troop2_4.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_9.remove(i)
                                    Troop2_4.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_12) >= 1:
                Botattack(Troop2_9,Troop3_12,Troop2_12,R12MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_12) >= 1:
                Botattack(Troop2_9,Troop1_12,Troop2_12,R12MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_12) >= 1:
                count = 1 
                for i in Troop2_9:
                    if count >= len(Troop2_9):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_9.remove(i)
                        Troop2_12.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_9.remove(i)
                        Troop2_12.append(i)
                    count += 1  
            if len(Troop2_12) == 0:
                if len(Troop1_12) == 0:
                    if len(Troop3_12) == 0:
                            count = 1
                            for i in Troop2_9:
                                if count >= len(Troop2_9):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_9.remove(i)
                                    Troop2_12.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_9.remove(i)
                                    Troop2_12.append(i)
                                count += 1
        #1
    if len(Troop2_10) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_3) >= 1:
                Botattack(Troop2_10,Troop1_3,Troop2_3,R3MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_3) >= 1:
                Botattack(Troop2_10,Troop3_3,Troop2_3,R3MinMax,R16MinMax,R14MinMax)
            if len(Troop2_3) >= 1:
                count = 1
                for i in Troop2_10:
                    if count >= len(Troop2_10):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_10.remove(i)
                        Troop2_3.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_10.remove(i)
                        Troop2_3.append(i)
                    count += 1
            if len(Troop2_3) == 0:
                if len(Troop1_3) == 0:
                    if len(Troop3_3) == 0:
                            count = 1
                            for i in Troop2_10:
                                if count >= len(Troop2_10):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_10.remove(i)
                                    Troop2_3.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_10.remove(i)
                                    Troop2_3.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_11) >= 1:
                Botattack(Troop2_10,Troop3_11,Troop2_11,R11MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_11) >= 1:
                Botattack(Troop2_10,Troop1_11,Troop2_11,R11MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_11) >= 1:
                count = 1 
                for i in Troop2_10:
                    if count >= len(Troop2_10):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_10.remove(i)
                        Troop2_11.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_10.remove(i)
                        Troop2_11.append(i)
                    count += 1  
            if len(Troop2_11) == 0:
                if len(Troop1_11) == 0:
                    if len(Troop3_11) == 0:
                            count = 1
                            for i in Troop2_10:
                                if count >= len(Troop2_10):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_10.remove(i)
                                    Troop2_11.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_10.remove(i)
                                    Troop2_11.append(i)
                                count += 1
        #1
    if len(Troop2_11) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_12) >= 1:
                Botattack(Troop2_11,Troop1_12,Troop2_12,R12MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_12) >= 1:
                Botattack(Troop2_11,Troop3_12,Troop2_12,R12MinMax,R16MinMax,R14MinMax)
            if len(Troop2_12) >= 1:
                count = 1
                for i in Troop2_11:
                    if count >= len(Troop2_11):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_11.remove(i)
                        Troop2_12.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_11.remove(i)
                        Troop2_12.append(i)
                    count += 1
            if len(Troop2_12) == 0:
                if len(Troop1_12) == 0:
                    if len(Troop3_12) == 0:
                            count = 1
                            for i in Troop2_11:
                                if count >= len(Troop2_11):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_11.remove(i)
                                    Troop2_12.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_11.remove(i)
                                    Troop2_12.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_14) >= 1:
                Botattack(Troop2_11,Troop3_14,Troop2_14,R14MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_14) >= 1:
                Botattack(Troop2_11,Troop1_14,Troop2_14,R14MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_14) >= 1:
                count = 1 
                for i in Troop2_11:
                    if count >= len(Troop2_11):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_11.remove(i)
                        Troop2_14.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_11.remove(i)
                        Troop2_14.append(i)
                    count += 1  
            if len(Troop2_14) == 0:
                if len(Troop1_14) == 0:
                    if len(Troop3_14) == 0:
                            count = 1
                            for i in Troop2_11:
                                if count >= len(Troop2_11):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_11.remove(i)
                                    Troop2_14.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_11.remove(i)
                                    Troop2_14.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_10) >= 1:
                Botattack(Troop2_11,Troop3_10,Troop2_10,R10MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_10) >= 1:
                Botattack(Troop2_11,Troop1_10,Troop2_10,R10MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_10) >= 1:
                count = 1 
                for i in Troop2_11:
                    if count >= len(Troop2_11):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_11.remove(i)
                        Troop2_10.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_11.remove(i)
                        Troop2_10.append(i)
                    count += 1  
            if len(Troop2_10) == 0:
                if len(Troop1_10) == 0:
                    if len(Troop3_10) == 0:
                            count = 1
                            for i in Troop2_11:
                                if count >= len(Troop2_11):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_11.remove(i)
                                    Troop2_10.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_11.remove(i)
                                    Troop2_10.append(i)
                                count += 1

        #1
    if len(Troop2_12) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_11) >= 1:
                Botattack(Troop2_12,Troop1_11,Troop2_11,R11MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_11) >= 1:
                Botattack(Troop2_12,Troop3_11,Troop2_11,R11MinMax,R16MinMax,R14MinMax)
            if len(Troop2_11) >= 1:
                count = 1
                for i in Troop2_12:
                    if count >= len(Troop2_12):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_12.remove(i)
                        Troop2_11.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_12.remove(i)
                        Troop2_11.append(i)
                    count += 1
            if len(Troop2_11) == 0:
                if len(Troop1_11) == 0:
                    if len(Troop3_11) == 0:
                            count = 1
                            for i in Troop2_12:
                                if count >= len(Troop2_12):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_12.remove(i)
                                    Troop2_11.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_12.remove(i)
                                    Troop2_11.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_13) >= 1:
                Botattack(Troop2_12,Troop3_13,Troop2_13,R13MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_13) >= 1:
                Botattack(Troop2_12,Troop1_13,Troop2_13,R13MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_13) >= 1:
                count = 1 
                for i in Troop2_12:
                    if count >= len(Troop2_12):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_12.remove(i)
                        Troop2_13.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_12.remove(i)
                        Troop2_13.append(i)
                    count += 1  
            if len(Troop2_13) == 0:
                if len(Troop1_13) == 0:
                    if len(Troop3_13) == 0:
                            count = 1
                            for i in Troop2_12:
                                if count >= len(Troop2_12):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_12.remove(i)
                                    Troop2_13.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_12.remove(i)
                                    Troop2_13.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_9) >= 1:
                Botattack(Troop2_12,Troop3_9,Troop2_9,R9MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_9) >= 1:
                Botattack(Troop2_12,Troop1_9,Troop2_9,R9MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_9) >= 1:
                count = 1 
                for i in Troop2_12:
                    if count >= len(Troop2_12):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_12.remove(i)
                        Troop2_9.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_12.remove(i)
                        Troop2_9.append(i)
                    count += 1  
            if len(Troop2_9) == 0:
                if len(Troop1_9) == 0:
                    if len(Troop3_9) == 0:
                            count = 1
                            for i in Troop2_12:
                                if count >= len(Troop2_12):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_12.remove(i)
                                    Troop2_9.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_12.remove(i)
                                    Troop2_9.append(i)
                                count += 1
        #1
    
    if len(Troop2_13) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_14) >= 1:
                Botattack(Troop2_13,Troop1_14,Troop2_14,R14MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_14) >= 1:
                Botattack(Troop2_13,Troop3_14,Troop2_14,R14MinMax,R16MinMax,R14MinMax)
            if len(Troop2_14) >= 1:
                count = 1
                for i in Troop2_13:
                    if count >= len(Troop2_13):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_13.remove(i)
                        Troop2_14.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_13.remove(i)
                        Troop2_14.append(i)
                    count += 1
            if len(Troop2_14) == 0:
                if len(Troop1_14) == 0:
                    if len(Troop3_14) == 0:
                            count = 1
                            for i in Troop2_13:
                                if count >= len(Troop2_13):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_13.remove(i)
                                    Troop2_14.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_13.remove(i)
                                    Troop2_14.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_15) >= 1:
                Botattack(Troop2_13,Troop3_15,Troop2_15,R15MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_15) >= 1:
                Botattack(Troop2_13,Troop1_15,Troop2_15,R15MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_15) >= 1:
                count = 1 
                for i in Troop2_13:
                    if count >= len(Troop2_13):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_13.remove(i)
                        Troop2_15.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_13.remove(i)
                        Troop2_15.append(i)
                    count += 1  
            if len(Troop2_15) == 0:
                if len(Troop1_15) == 0:
                    if len(Troop3_15) == 0:
                            count = 1
                            for i in Troop2_13:
                                if count >= len(Troop2_13):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_13.remove(i)
                                    Troop2_15.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_13.remove(i)
                                    Troop2_15.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_12) >= 1:
                Botattack(Troop2_13,Troop3_12,Troop2_12,R12MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_12) >= 1:
                Botattack(Troop2_13,Troop1_12,Troop2_12,R12MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_12) >= 1:
                count = 1 
                for i in Troop2_13:
                    if count >= len(Troop2_13):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_13.remove(i)
                        Troop2_12.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_13.remove(i)
                        Troop2_12.append(i)
                    count += 1  
            if len(Troop2_12) == 0:
                if len(Troop1_12) == 0:
                    if len(Troop3_12) == 0:
                            count = 1
                            for i in Troop2_13:
                                if count >= len(Troop2_13):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_13.remove(i)
                                    Troop2_12.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_13.remove(i)
                                    Troop2_12.append(i)
                                count += 1
        #1
    if len(Troop2_14) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_11) >= 1:
                Botattack(Troop2_14,Troop1_11,Troop2_11,R11MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_11) >= 1:
                Botattack(Troop2_14,Troop3_11,Troop2_11,R11MinMax,R16MinMax,R14MinMax)
            if len(Troop2_11) >= 1:
                count = 1
                for i in Troop2_14:
                    if count >= len(Troop2_14):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_14.remove(i)
                        Troop2_11.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_14.remove(i)
                        Troop2_11.append(i)
                    count += 1
            if len(Troop2_11) == 0:
                if len(Troop1_11) == 0:
                    if len(Troop3_11) == 0:
                            count = 1
                            for i in Troop2_14:
                                if count >= len(Troop2_14):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_14.remove(i)
                                    Troop2_11.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_14.remove(i)
                                    Troop2_11.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_13) >= 1:
                Botattack(Troop2_14,Troop3_13,Troop2_13,R13MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_13) >= 1:
                Botattack(Troop2_14,Troop1_13,Troop2_13,R13MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_13) >= 1:
                count = 1 
                for i in Troop2_14:
                    if count >= len(Troop2_14):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_14.remove(i)
                        Troop2_13.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_14.remove(i)
                        Troop2_13.append(i)
                    count += 1  
            if len(Troop2_13) == 0:
                if len(Troop1_13) == 0:
                    if len(Troop3_13) == 0:
                            count = 1
                            for i in Troop2_14:
                                if count >= len(Troop2_14):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_14.remove(i)
                                    Troop2_13.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_14.remove(i)
                                    Troop2_13.append(i)
                                count += 1
    
    if len(Troop2_15) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_13) >= 1:
                Botattack(Troop2_15,Troop1_13,Troop2_13,R13MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_13) >= 1:
                Botattack(Troop2_15,Troop3_13,Troop2_13,R13MinMax,R16MinMax,R14MinMax)
            if len(Troop2_13) >= 1:
                count = 1
                for i in Troop2_15:
                    if count >= len(Troop2_15):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_15.remove(i)
                        Troop2_13.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_15.remove(i)
                        Troop2_13.append(i)
                    count += 1
            if len(Troop2_13) == 0:
                if len(Troop1_13) == 0:
                    if len(Troop3_13) == 0:
                            count = 1
                            for i in Troop2_15:
                                if count >= len(Troop2_15):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_15.remove(i)
                                    Troop2_13.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_15.remove(i)
                                    Troop2_13.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_16) >= 1:
                Botattack(Troop2_15,Troop3_16,Troop2_16,R16MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_16) >= 1:
                Botattack(Troop2_15,Troop1_1,Troop2_16,R16MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_16) >= 1:
                count = 1 
                for i in Troop2_15:
                    if count >= len(Troop2_15):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_15.remove(i)
                        Troop2_16.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_15.remove(i)
                        Troop2_16.append(i)
                    count += 1  
            if len(Troop2_16) == 0:
                if len(Troop1_16) == 0:
                    if len(Troop3_16) == 0:
                            count = 1
                            for i in Troop2_15:
                                if count >= len(Troop2_15):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_15.remove(i)
                                    Troop2_16.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_15.remove(i)
                                    Troop2_16.append(i)
                                count += 1
    
    if len(Troop2_16) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_15) >= 1:
                Botattack(Troop2_16,Troop1_15,Troop2_15,R15MinMax,R4MinMax,R14MinMax)                    
            if len(Troop3_15) >= 1:
                Botattack(Troop2_16,Troop3_15,Troop2_15,R15MinMax,R16MinMax,R14MinMax)
            if len(Troop2_15) >= 1:
                count = 1
                for i in Troop2_16:
                    if count >= len(Troop2_16):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_16.remove(i)
                        Troop2_15.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_16.remove(i)
                        Troop2_15.append(i)
                    count += 1
            if len(Troop2_15) == 0:
                if len(Troop1_15) == 0:
                    if len(Troop3_15) == 0:
                            count = 1
                            for i in Troop2_16:
                                if count >= len(Troop2_16):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_16.remove(i)
                                    Troop2_15.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_16.remove(i)
                                    Troop2_15.append(i)
                                count += 1
        if RanChoice == 2:
            if len(Troop3_17) >= 1:
                Botattack(Troop2_16,Troop3_17,Troop2_17,R17MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_17) >= 1:
                Botattack(Troop2_16,Troop1_17,Troop2_17,R17MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_17) >= 1:
                count = 1 
                for i in Troop2_16:
                    if count >= len(Troop2_16):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_16.remove(i)
                        Troop2_17.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_16.remove(i)
                        Troop2_17.append(i)
                    count += 1  
            if len(Troop2_17) == 0:
                if len(Troop1_17) == 0:
                    if len(Troop3_17) == 0:
                            count = 1
                            for i in Troop2_16:
                                if count >= len(Troop2_16):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_16.remove(i)
                                    Troop2_17.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_16.remove(i)
                                    Troop2_17.append(i)
                                count += 1
        if RanChoice == 3:
            if len(Troop3_5) >= 1:
                Botattack(Troop2_16,Troop3_5,Troop2_5,R5MinMax,R16MinMax,R14MinMax)
            elif len(Troop1_5) >= 1:
                Botattack(Troop2_16,Troop1_5,Troop2_5,R5MinMax,R4MinMax,R14MinMax)  
            elif len(Troop2_5) >= 1:
                count = 1 
                for i in Troop2_16:
                    if count >= len(Troop2_16):
                        break
                    elif count == 1:
                        i.rect.x = 300
                        i.rect.y = 300  
                        Troop2_16.remove(i)
                        Troop2_5.append(i)
                    else:
                        i.rect.x = 350
                        i.rect.y = 300
                        Troop2_16.remove(i)
                        Troop2_5.append(i)
                    count += 1  
            if len(Troop2_5) == 0:
                if len(Troop1_5) == 0:
                    if len(Troop3_5) == 0:
                            count = 1
                            for i in Troop2_16:
                                if count >= len(Troop2_16):
                                    break
                                elif count == 1:
                                    i.rect.x = 300
                                    i.rect.y = 300
                                    Troop2_16.remove(i)
                                    Troop2_5.append(i)
                                else:
                                    i.rect.x = 350
                                    i.rect.y = 300
                                    Troop2_16.remove(i)
                                    Troop2_5.append(i)
                                count += 1

    if len(Troop2_17) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_16) >= 1:
                Botattack(Troop2_17,Troop1_16,Troop2_16,R16MinMax,R4MinMax)                    
            if len(Troop3_16) >= 1:
                Botattack(Troop2_17,Troop3_16,Troop2_16,R16MinMax,R16MinMax)
            if len(Troop2_16) >= 1:
                count = 1
                for i in Troop2_17:
                    if count >= len(Troop2_17):
                        break
                    elif count == 1:
                        i.rect.x = 450
                        i.rect.y = 150  
                        Troop2_17.remove(i)
                        Troop2_16.append(i)
                    else:
                        i.rect.x = 475
                        i.rect.y = 150
                        Troop2_17.remove(i)
                        Troop2_16.append(i)
                    count += 1
            if len(Troop2_16) == 0:
                if len(Troop1_16) == 0:
                    if len(Troop3_16) == 0:
                            count = 1
                            for i in Troop2_17:
                                if count >= len(Troop2_17):
                                    break
                                elif count == 1:
                                    i.rect.x = 450
                                    i.rect.y = 150
                                    Troop2_17.remove(i)
                                    Troop2_16.append(i)
                                else:
                                    i.rect.x = 475
                                    i.rect.y = 150
                                    Troop2_17.remove(i)
                                    Troop2_16.append(i)
                                count += 1


def Player3Move():
    R1MinMax = (xSize - 350,xSize - 160,ySize - 450,ySize - 336)
    R2MinMax = (xSize - 425,xSize - 200,ySize - 700,ySize - 560)
    R3MinMax = (xSize - 427,xSize - 198,ySize - 735,ySize - 708)
    R4MinMax = (xSize - 450,xSize - 150,ySize - 560,ySize - 450)
    R5MinMax = (xSize - 463,xSize - 426,ySize - 390,ySize - 295)
    R6MinMax = (xSize - 310,xSize - 238,ySize - 233,ySize - 138)
    R7MinMax = (xSize - 235,xSize - 179,ySize - 234,ySize - 140)
    R8MinMax = (xSize - 384,xSize - 310,ySize - 240,ySize - 128)
    R9MinMax = (xSize - 765,xSize - 639,ySize - 560,ySize - 326)
    R10MinMax = (xSize - 709,xSize - 560,ySize - 751,ySize - 676)
    R11MinMax = (xSize - 973,xSize - 893,ySize - 773,ySize - 666)
    R12MinMax = (xSize - 974,xSize - 918,ySize - 663,ySize - 613)
    R13MinMax = (xSize - 1146,xSize - 993,ySize - 662,ySize - 488)
    R14MinMax = (xSize - 1155,xSize - 975, ySize - 780, ySize - 665)
    R15MinMax = (xSize - 1056,xSize - 900,ySize - 428,ySize - 323)
    R16MinMax = (xSize - 1061,xSize - 904,ySize - 332,ySize - 221)
    R17MinMax = (xSize - 1080,xSize - 932,ySize - 210,ySize - 161)
    if len(Troop3_1) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_4) >= 1:
                Botattack(Troop3_1,Troop1_4,Troop3_4,R4MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_4) >= 1:
                Botattack(Troop3_1,Troop2_4,Troop3_4,R4MinMax,R14MinMax,R16MinMax)
            if len(Troop3_4) >= 1:
                count = 1
                for i in Troop3_1:
                    if count >= len(Troop3_1):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_1.remove(i)
                        Troop3_4.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_1.remove(i)
                        Troop3_4.append(i)
                    count += 1
            if len(Troop3_4) == 0:
                if len(Troop2_4) == 0:
                    if len(Troop1_4) == 0:
                        count = 1
                        for i in Troop3_1:
                            if count >= len(Troop3_1):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_1.remove(i)
                                Troop3_4.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_1.remove(i)
                                Troop3_4.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_5) >= 1:
                Botattack(Troop3_1,Troop2_5,Troop3_5,R5MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_5) >= 1:
                Botattack(Troop3_1,Troop1_5,Troop3_5,R5MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_5) >= 1:
                count = 1 
                for i in Troop3_1:
                    if count >= len(Troop3_1):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_1.remove(i)
                        Troop3_5.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_1.remove(i)
                        Troop3_5.append(i)
                    count += 1  
            if len(Troop2_5) == 0:
                if len(Troop1_5) == 0:
                    if len(Troop3_5) == 0:
                        count = 1
                        for i in Troop3_1:
                            if count >= len(Troop3_1):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_1.remove(i)
                                Troop3_5.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_1.remove(i)
                                Troop3_5.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_6) >= 1:
                Botattack(Troop3_1,Troop2_6,Troop3_6,R6MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_6) >= 1:
                Botattack(Troop3_1,Troop1_6,Troop3_6,R6MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_6) >= 1:
                count = 1 
                for i in Troop3_1:
                    if count >= len(Troop3_1):
                        break
                    elif count == 1:
                        i.rect.x = 946
                        i.rect.y = 630  
                        Troop3_1.remove(i)
                        Troop3_6.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 630
                        Troop3_1.remove(i)
                        Troop3_6.append(i)
                    count += 1  
            if len(Troop2_6) == 0:
                if len(Troop1_6) == 0:
                    if len(Troop3_6) == 0:
                        count = 1
                        for i in Troop3_1:
                            if count >= len(Troop3_1):
                                break
                            elif count == 1:
                                i.rect.x = 946
                                i.rect.y = 630
                                Troop3_1.remove(i)
                                Troop3_6.append(i)
                            else:
                                i.rect.x = 946
                                i.rect.y = 630
                                Troop3_1.remove(i)
                                Troop3_6.append(i)
                            count += 1

    if len(Troop3_2) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_3) >= 1:
                Botattack(Troop3_2,Troop1_2,Troop3_2,R3MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_3) >= 1:
                Botattack(Troop3_2,Troop2_3,Troop3_2,R3MinMax,R14MinMax,R16MinMax)
            if len(Troop3_3) >= 1:
                count = 1
                for i in Troop3_2:
                    if count >= len(Troop3_2):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_2.remove(i)
                        Troop3_3.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_2.remove(i)
                        Troop3_3.append(i)
                    count += 1
            if len(Troop3_3) == 0:
                if len(Troop2_3) == 0:
                    if len(Troop1_3) == 0:
                        count = 1
                        for i in Troop3_2:
                            if count >= len(Troop3_2):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_2.remove(i)
                                Troop3_3.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_2.remove(i)
                                Troop3_3.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_4) >= 1:
                Botattack(Troop3_2,Troop2_3,Troop3_4,R4MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_4) >= 1:
                Botattack(Troop3_2,Troop1_4,Troop3_4,R4MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_4) >= 1:
                count = 1 
                for i in Troop3_2:
                    if count >= len(Troop3_2):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_2.remove(i)
                        Troop3_4.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_2.remove(i)
                        Troop3_4.append(i)
                    count += 1  
            if len(Troop2_4) == 0:
                if len(Troop1_4) == 0:
                    if len(Troop3_4) == 0:
                        count = 1
                        for i in Troop3_2:
                            if count >= len(Troop3_2):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_2.remove(i)
                                Troop3_4.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_2.remove(i)
                                Troop3_4.append(i)
                            count += 1

    if len(Troop3_3) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_10) >= 1:
                Botattack(Troop3_3,Troop1_10,Troop3_10,R10MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_10) >= 1:
                Botattack(Troop3_3,Troop2_10,Troop3_10,R10MinMax,R14MinMax,R16MinMax)
            if len(Troop3_10) >= 1:
                count = 1
                for i in Troop3_3:
                    if count >= len(Troop3_3):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_3.remove(i)
                        Troop3_10.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_3.remove(i)
                        Troop3_10.append(i)
                    count += 1
            if len(Troop3_10) == 0:
                if len(Troop2_10) == 0:
                    if len(Troop1_10) == 0:
                        count = 1
                        for i in Troop3_3:
                            if count >= len(Troop3_3):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_3.remove(i)
                                Troop3_10.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_3.remove(i)
                                Troop3_10.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_2) >= 1:
                Botattack(Troop3_3,Troop2_2,Troop3_2,R2MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_2) >= 1:
                Botattack(Troop3_3,Troop1_2,Troop3_2,R2MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_2) >= 1:
                count = 1 
                for i in Troop3_3:
                    if count >= len(Troop3_3):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_3.remove(i)
                        Troop3_2.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_3.remove(i)
                        Troop3_2.append(i)
                    count += 1  
            if len(Troop2_2) == 0:
                if len(Troop1_2) == 0:
                    if len(Troop3_2) == 0:
                        count = 1
                        for i in Troop3_3:
                            if count >= len(Troop3_3):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_3.remove(i)
                                Troop3_2.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_3.remove(i)
                                Troop3_2.append(i)
                            count += 1


    if len(Troop3_4) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_2) >= 1:
                Botattack(Troop3_4,Troop1_2,Troop3_2,R2MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_2) >= 1:
                Botattack(Troop3_4,Troop2_2,Troop3_2,R2MinMax,R14MinMax,R16MinMax)
            if len(Troop3_2) >= 1:
                count = 1
                for i in Troop3_4:
                    if count >= len(Troop3_4):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_4.remove(i)
                        Troop3_2.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_4.remove(i)
                        Troop3_2.append(i)
                    count += 1
            if len(Troop3_2) == 0:
                if len(Troop2_2) == 0:
                    if len(Troop1_2) == 0:
                        count = 1
                        for i in Troop3_4:
                            if count >= len(Troop3_4):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_4.remove(i)
                                Troop3_2.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_4.remove(i)
                                Troop3_2.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_1) >= 1:
                Botattack(Troop3_4,Troop2_1,Troop3_1,R1MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_1) >= 1:
                Botattack(Troop3_4,Troop1_1,Troop3_1,R1MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_1) >= 1:
                count = 1 
                for i in Troop3_4:
                    if count >= len(Troop3_4):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_4.remove(i)
                        Troop3_1.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_4.remove(i)
                        Troop3_1.append(i)
                    count += 1  
            if len(Troop2_1) == 0:
                if len(Troop1_1) == 0:
                    if len(Troop3_1) == 0:
                        count = 1
                        for i in Troop3_4:
                            if count >= len(Troop3_4):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_4.remove(i)
                                Troop3_1.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_4.remove(i)
                                Troop3_1.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_9) >= 1:
                Botattack(Troop3_4,Troop2_9,Troop3_9,R9MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_9) >= 1:
                Botattack(Troop3_4,Troop1_9,Troop3_9,R9MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_9) >= 1:
                count = 1 
                for i in Troop3_4:
                    if count >= len(Troop3_4):
                        break
                    elif count == 1:
                        i.rect.x = 949
                        i.rect.y = 930  
                        Troop3_4.remove(i)
                        Troop3_9.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 930
                        Troop3_4.remove(i)
                        Troop3_9.append(i)
                    count += 1  
            if len(Troop2_9) == 0:
                if len(Troop1_9) == 0:
                    if len(Troop3_9) == 0:
                        count = 1
                        for i in Troop3_4:
                            if count >= len(Troop3_4):
                                break
                            elif count == 1:
                                i.rect.x = 949
                                i.rect.y = 930
                                Troop3_4.remove(i)
                                Troop3_9.append(i)
                            else:
                                i.rect.x = 949
                                i.rect.y = 930
                                Troop3_4.remove(i)
                                Troop3_9.append(i)
                            count += 1

    if len(Troop3_5) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_1) >= 1:
                Botattack(Troop3_5,Troop1_1,Troop3_1,R1MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_1) >= 1:
                Botattack(Troop3_5,Troop2_1,Troop3_1,R1MinMax,R14MinMax,R16MinMax)
            if len(Troop3_1) >= 1:
                count = 1
                for i in Troop3_5:
                    if count >= len(Troop3_5):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_5.remove(i)
                        Troop3_1.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_5.remove(i)
                        Troop3_1.append(i)
                    count += 1
            if len(Troop3_1) == 0:
                if len(Troop2_1) == 0:
                    if len(Troop1_1) == 0:
                        count = 1
                        for i in Troop3_5:
                            if count >= len(Troop3_5):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_5.remove(i)
                                Troop3_1.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_5.remove(i)
                                Troop3_1.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_16) >= 1:
                Botattack(Troop3_5,Troop2_16,Troop3_16,R16MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_16) >= 1:
                Botattack(Troop3_5,Troop1_16,Troop3_16,R16MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_16) >= 1:
                count = 1 
                for i in Troop3_5:
                    if count >= len(Troop3_5):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_5.remove(i)
                        Troop3_16.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_5.remove(i)
                        Troop3_16.append(i)
                    count += 1  
            if len(Troop2_16) == 0:
                if len(Troop1_16) == 0:
                    if len(Troop3_16) == 0:
                        count = 1
                        for i in Troop3_5:
                            if count >= len(Troop3_5):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_5.remove(i)
                                Troop3_16.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_5.remove(i)
                                Troop3_16.append(i)
                            count += 1

    if len(Troop3_6) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_7) >= 1:
                Botattack(Troop3_6,Troop1_7,Troop3_7,R7MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_7) >= 1:
                Botattack(Troop3_6,Troop2_7,Troop3_7,R7MinMax,R14MinMax,R16MinMax)
            if len(Troop3_7) >= 1:
                count = 1
                for i in Troop3_6:
                    if count >= len(Troop3_6):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_6.remove(i)
                        Troop3_7.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_6.remove(i)
                        Troop3_7.append(i)
                    count += 1
            if len(Troop3_7) == 0:
                if len(Troop2_7) == 0:
                    if len(Troop1_7) == 0:
                        count = 1
                        for i in Troop3_6:
                            if count >= len(Troop3_6):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_6.remove(i)
                                Troop3_7.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_6.remove(i)
                                Troop3_7.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_8) >= 1:
                Botattack(Troop3_6,Troop2_8,Troop3_8,R8MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_8) >= 1:
                Botattack(Troop3_6,Troop1_8,Troop3_8,R8MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_8) >= 1:
                count = 1 
                for i in Troop3_6:
                    if count >= len(Troop3_6):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_6.remove(i)
                        Troop3_8.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_6.remove(i)
                        Troop3_8.append(i)
                    count += 1  
            if len(Troop2_8) == 0:
                if len(Troop1_8) == 0:
                    if len(Troop3_8) == 0:
                        count = 1
                        for i in Troop3_6:
                            if count >= len(Troop3_6):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_6.remove(i)
                                Troop3_8.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_6.remove(i)
                                Troop3_8.append(i)
                            count += 1


    if len(Troop3_7) > 1:
        RanChoice = random.randint(1,1)
        if RanChoice == 1:
            if len(Troop1_6) >= 1:
                Botattack(Troop3_7,Troop1_6,Troop3_6,R6MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_6) >= 1:
                Botattack(Troop3_7,Troop2_6,Troop3_6,R6MinMax,R14MinMax,R16MinMax)
            if len(Troop3_6) >= 1:
                count = 1
                for i in Troop3_7:
                    if count >= len(Troop3_7):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_7.remove(i)
                        Troop3_6.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_7.remove(i)
                        Troop3_6.append(i)
                    count += 1
            if len(Troop3_6) == 0:
                if len(Troop2_6) == 0:
                    if len(Troop1_6) == 0:
                        count = 1
                        for i in Troop3_7:
                            if count >= len(Troop3_7):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_7.remove(i)
                                Troop3_6.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_7.remove(i)
                                Troop3_6.append(i)
                            count += 1

    if len(Troop3_8) > 1:
        RanChoice = random.randint(1,1)
        if RanChoice == 1:
            if len(Troop1_6) >= 1:
                Botattack(Troop3_8,Troop1_6,Troop3_6,R6MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_6) >= 1:
                Botattack(Troop3_8,Troop2_6,Troop3_6,R6MinMax,R14MinMax,R16MinMax)
            if len(Troop3_6) >= 1:
                count = 1
                for i in Troop3_8:
                    if count >= len(Troop3_8):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_8.remove(i)
                        Troop3_6.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_8.remove(i)
                        Troop3_6.append(i)
                    count += 1
            if len(Troop3_6) == 0:
                if len(Troop2_6) == 0:
                    if len(Troop1_6) == 0:
                        count = 1
                        for i in Troop3_8:
                            if count >= len(Troop3_8):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_8.remove(i)
                                Troop3_6.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_8.remove(i)
                                Troop3_6.append(i)
                            count += 1

    if len(Troop3_9) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_4) >= 1:
                Botattack(Troop3_9,Troop1_4,Troop3_4,R4MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_4) >= 1:
                Botattack(Troop3_9,Troop2_4,Troop3_4,R4MinMax,R14MinMax,R16MinMax)
            if len(Troop3_4) >= 1:
                count = 1
                for i in Troop3_9:
                    if count >= len(Troop3_9):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_9.remove(i)
                        Troop3_4.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_9.remove(i)
                        Troop3_4.append(i)
                    count += 1
            if len(Troop3_4) == 0:
                if len(Troop2_4) == 0:
                    if len(Troop1_4) == 0:
                        count = 1
                        for i in Troop3_9:
                            if count >= len(Troop3_9):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_9.remove(i)
                                Troop3_4.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_9.remove(i)
                                Troop3_4.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_12) >= 1:
                Botattack(Troop3_10,Troop2_12,Troop3_12,R12MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_12) >= 1:
                Botattack(Troop3_11,Troop1_12,Troop3_12,R12MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_12) >= 1:
                count = 1 
                for i in Troop3_9:
                    if count >= len(Troop3_9):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_9.remove(i)
                        Troop3_12.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_9.remove(i)
                        Troop3_12.append(i)
                    count += 1  
            if len(Troop2_12) == 0:
                if len(Troop1_12) == 0:
                    if len(Troop3_12) == 0:
                        count = 1
                        for i in Troop3_9:
                            if count >= len(Troop3_9):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_9.remove(i)
                                Troop3_12.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_9.remove(i)
                                Troop3_12.append(i)
                            count += 1

    if len(Troop3_10) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_3) >= 1:
                Botattack(Troop3_10,Troop1_3,Troop3_3,R3MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_3) >= 1:
                Botattack(Troop3_10,Troop2_3,Troop3_3,R3MinMax,R14MinMax,R16MinMax)
            if len(Troop3_3) >= 1:
                count = 1
                for i in Troop3_10:
                    if count >= len(Troop3_10):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_10.remove(i)
                        Troop3_3.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_10.remove(i)
                        Troop3_3.append(i)
                    count += 1
            if len(Troop3_3) == 0:
                if len(Troop2_3) == 0:
                    if len(Troop1_3) == 0:
                        count = 1
                        for i in Troop3_10:
                            if count >= len(Troop3_10):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_10.remove(i)
                                Troop3_3.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_10.remove(i)
                                Troop3_3.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_11) >= 1:
                Botattack(Troop3_10,Troop2_11,Troop3_11,R11MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_11) >= 1:
                Botattack(Troop3_10,Troop1_11,Troop3_11,R11MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_11) >= 1:
                count = 1 
                for i in Troop3_10:
                    if count >= len(Troop3_10):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_10.remove(i)
                        Troop3_11.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_10.remove(i)
                        Troop3_11.append(i)
                    count += 1  
            if len(Troop2_11) == 0:
                if len(Troop1_11) == 0:
                    if len(Troop3_11) == 0:
                        count = 1
                        for i in Troop3_10:
                            if count >= len(Troop3_10):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_10.remove(i)
                                Troop3_11.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_10.remove(i)
                                Troop3_11.append(i)
                            count += 1

    if len(Troop3_11) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_10) >= 1:
                Botattack(Troop3_11,Troop1_10,Troop3_10,R10MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_10) >= 1:
                Botattack(Troop3_11,Troop2_10,Troop3_10,R11MinMax,R14MinMax,R16MinMax)
            if len(Troop3_10) >= 1:
                count = 1
                for i in Troop3_11:
                    if count >= len(Troop3_11):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_11.remove(i)
                        Troop3_10.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_11.remove(i)
                        Troop3_10.append(i)
                    count += 1
            if len(Troop3_10) == 0:
                if len(Troop2_10) == 0:
                    if len(Troop1_10) == 0:
                        count = 1
                        for i in Troop3_11:
                            if count >= len(Troop3_11):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_11.remove(i)
                                Troop3_10.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_11.remove(i)
                                Troop3_10.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_12) >= 1:
                Botattack(Troop3_11,Troop2_12,Troop3_12,R12MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_12) >= 1:
                Botattack(Troop3_11,Troop1_12,Troop3_12,R12MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_12) >= 1:
                count = 1 
                for i in Troop3_11:
                    if count >= len(Troop3_11):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_11.remove(i)
                        Troop3_12.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_11.remove(i)
                        Troop3_12.append(i)
                    count += 1  
            if len(Troop2_12) == 0:
                if len(Troop1_12) == 0:
                    if len(Troop3_12) == 0:
                        count = 1
                        for i in Troop3_11:
                            if count >= len(Troop3_11):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_11.remove(i)
                                Troop3_12.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_11.remove(i)
                                Troop3_12.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_14) >= 1:
                Botattack(Troop3_11,Troop2_14,Troop3_14,R14MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_14) >= 1:
                Botattack(Troop3_11,Troop1_14,Troop3_14,R14MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_14) >= 1:
                count = 1 
                for i in Troop3_11:
                    if count >= len(Troop3_11):
                        break
                    elif count == 1:
                        i.rect.x = 9414
                        i.rect.y = 1430  
                        Troop3_11.remove(i)
                        Troop3_14.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 1430
                        Troop3_11.remove(i)
                        Troop3_14.append(i)
                    count += 1  
            if len(Troop2_14) == 0:
                if len(Troop1_14) == 0:
                    if len(Troop3_14) == 0:
                        count = 1
                        for i in Troop3_11:
                            if count >= len(Troop3_11):
                                break
                            elif count == 1:
                                i.rect.x = 9414
                                i.rect.y = 1430
                                Troop3_11.remove(i)
                                Troop3_14.append(i)
                            else:
                                i.rect.x = 9414
                                i.rect.y = 1430
                                Troop3_11.remove(i)
                                Troop3_14.append(i)
                            count += 1

    if len(Troop3_12) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_9) >= 1:
                Botattack(Troop3_12,Troop1_9,Troop3_9,R9MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_9) >= 1:
                Botattack(Troop3_12,Troop2_9,Troop3_9,R9MinMax,R14MinMax,R16MinMax)
            if len(Troop3_9) >= 1:
                count = 1
                for i in Troop3_12:
                    if count >= len(Troop3_12):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_12.remove(i)
                        Troop3_9.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_12.remove(i)
                        Troop3_9.append(i)
                    count += 1
            if len(Troop3_9) == 0:
                if len(Troop2_9) == 0:
                    if len(Troop1_9) == 0:
                        count = 1
                        for i in Troop3_12:
                            if count >= len(Troop3_12):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_12.remove(i)
                                Troop3_9.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_12.remove(i)
                                Troop3_9.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_11) >= 1:
                Botattack(Troop3_12,Troop2_11,Troop3_11,R11MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_11) >= 1:
                Botattack(Troop3_12,Troop1_11,Troop3_11,R11MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_11) >= 1:
                count = 1 
                for i in Troop3_12:
                    if count >= len(Troop3_12):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_12.remove(i)
                        Troop3_11.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_12.remove(i)
                        Troop3_11.append(i)
                    count += 1  
            if len(Troop2_11) == 0:
                if len(Troop1_11) == 0:
                    if len(Troop3_11) == 0:
                        count = 1
                        for i in Troop3_12:
                            if count >= len(Troop3_12):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_12.remove(i)
                                Troop3_11.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_12.remove(i)
                                Troop3_11.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_13) >= 1:
                Botattack(Troop3_12,Troop2_13,Troop3_13,R13MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_13) >= 1:
                Botattack(Troop3_12,Troop1_13,Troop3_13,R13MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_13) >= 1:
                count = 1 
                for i in Troop3_12:
                    if count >= len(Troop3_12):
                        break
                    elif count == 1:
                        i.rect.x = 9413
                        i.rect.y = 1330  
                        Troop3_12.remove(i)
                        Troop3_13.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 1330
                        Troop3_12.remove(i)
                        Troop3_13.append(i)
                    count += 1  
            if len(Troop2_13) == 0:
                if len(Troop1_13) == 0:
                    if len(Troop3_13) == 0:
                        count = 1
                        for i in Troop3_12:
                            if count >= len(Troop3_12):
                                break
                            elif count == 1:
                                i.rect.x = 945
                                i.rect.y = 530
                                Troop3_12.remove(i)
                                Troop3_13.append(i)
                            else:
                                i.rect.x = 945
                                i.rect.y = 530
                                Troop3_12.remove(i)
                                Troop3_13.append(i)
                            count += 1

    if len(Troop3_13) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_12) >= 1:
                Botattack(Troop3_13,Troop1_12,Troop3_12,R12MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_12) >= 1:
                Botattack(Troop3_13,Troop2_12,Troop3_12,R12MinMax,R14MinMax,R16MinMax)
            if len(Troop3_12) >= 1:
                count = 1
                for i in Troop3_13:
                    if count >= len(Troop3_13):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_13.remove(i)
                        Troop3_12.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_13.remove(i)
                        Troop3_12.append(i)
                    count += 1
            if len(Troop3_12) == 0:
                if len(Troop2_12) == 0:
                    if len(Troop1_12) == 0:
                        count = 1
                        for i in Troop3_13:
                            if count >= len(Troop3_13):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_13.remove(i)
                                Troop3_12.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_13.remove(i)
                                Troop3_12.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_14) >= 1:
                Botattack(Troop3_13,Troop2_14,Troop3_14,R14MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_14) >= 1:
                Botattack(Troop3_13,Troop1_14,Troop3_14,R14MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_14) >= 1:
                count = 1 
                for i in Troop3_13:
                    if count >= len(Troop3_13):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_13.remove(i)
                        Troop3_14.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_13.remove(i)
                        Troop3_14.append(i)
                    count += 1  
            if len(Troop2_14) == 0:
                if len(Troop1_14) == 0:
                    if len(Troop3_14) == 0:
                        count = 1
                        for i in Troop3_13:
                            if count >= len(Troop3_13):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_13.remove(i)
                                Troop3_14.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_13.remove(i)
                                Troop3_14.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_15) >= 1:
                Botattack(Troop3_13,Troop2_15,Troop3_15,R15MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_15) >= 1:
                Botattack(Troop3_13,Troop1_15,Troop3_15,R15MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_15) >= 1:
                count = 1 
                for i in Troop3_13:
                    if count >= len(Troop3_13):
                        break
                    elif count == 1:
                        i.rect.x = 9415
                        i.rect.y = 1530  
                        Troop3_13.remove(i)
                        Troop3_15.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 1530
                        Troop3_13.remove(i)
                        Troop3_15.append(i)
                    count += 1  
            if len(Troop2_15) == 0:
                if len(Troop1_15) == 0:
                    if len(Troop3_15) == 0:
                        count = 1
                        for i in Troop3_13:
                            if count >= len(Troop3_13):
                                break
                            elif count == 1:
                                i.rect.x = 9415
                                i.rect.y = 1530
                                Troop3_13.remove(i)
                                Troop3_15.append(i)
                            else:
                                i.rect.x = 9415
                                i.rect.y = 1530
                                Troop3_13.remove(i)
                                Troop3_15.append(i)
                            count += 1
    if len(Troop3_14) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_11) >= 1:
                Botattack(Troop3_14,Troop1_11,Troop3_11,R11MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_11) >= 1:
                Botattack(Troop3_14,Troop2_11,Troop3_11,R11MinMax,R14MinMax,R16MinMax)
            if len(Troop3_11) >= 1:
                count = 1
                for i in Troop3_14:
                    if count >= len(Troop3_14):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_14.remove(i)
                        Troop3_11.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_14.remove(i)
                        Troop3_11.append(i)
                    count += 1
            if len(Troop3_11) == 0:
                if len(Troop2_11) == 0:
                    if len(Troop1_11) == 0:
                        count = 1
                        for i in Troop3_14:
                            if count >= len(Troop3_14):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_14.remove(i)
                                Troop3_11.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_14.remove(i)
                                Troop3_11.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_13) >= 1:
                Botattack(Troop3_14,Troop2_13,Troop3_13,R13MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_13) >= 1:
                Botattack(Troop3_14,Troop1_13,Troop3_13,R13MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_13) >= 1:
                count = 1 
                for i in Troop3_14:
                    if count >= len(Troop3_14):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_14.remove(i)
                        Troop3_13.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_14.remove(i)
                        Troop3_13.append(i)
                    count += 1  
            if len(Troop2_13) == 0:
                if len(Troop1_13) == 0:
                    if len(Troop3_13) == 0:
                        count = 1
                        for i in Troop3_14:
                            if count >= len(Troop3_14):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_14.remove(i)
                                Troop3_13.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_14.remove(i)
                                Troop3_13.append(i)
                            count += 1

    if len(Troop3_15) > 1:
        RanChoice = random.randint(1,2)
        if RanChoice == 1:
            if len(Troop1_13) >= 1:
                Botattack(Troop3_13,Troop1_13,Troop3_13,R13MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_13) >= 1:
                Botattack(Troop3_15,Troop2_13,Troop3_13,R13MinMax,R14MinMax,R16MinMax)
            if len(Troop3_13) >= 1:
                count = 1
                for i in Troop3_15:
                    if count >= len(Troop3_15):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_15.remove(i)
                        Troop3_13.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_15.remove(i)
                        Troop3_13.append(i)
                    count += 1
            if len(Troop3_13) == 0:
                if len(Troop2_13) == 0:
                    if len(Troop1_13) == 0:
                        count = 1
                        for i in Troop3_15:
                            if count >= len(Troop3_15):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_15.remove(i)
                                Troop3_13.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_15.remove(i)
                                Troop3_13.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_16) >= 1:
                Botattack(Troop3_15,Troop2_16,Troop3_16,R16MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_16) >= 1:
                Botattack(Troop3_15,Troop1_16,Troop3_16,R16MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_16) >= 1:
                count = 1 
                for i in Troop3_15:
                    if count >= len(Troop3_15):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_15.remove(i)
                        Troop3_16.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_15.remove(i)
                        Troop3_16.append(i)
                    count += 1  
            if len(Troop2_16) == 0:
                if len(Troop1_16) == 0:
                    if len(Troop3_16) == 0:
                        count = 1
                        for i in Troop3_15:
                            if count >= len(Troop3_15):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_15.remove(i)
                                Troop3_16.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_15.remove(i)
                                Troop3_16.append(i)
                            count += 1

    if len(Troop3_16) > 1:
        RanChoice = random.randint(1,3)
        if RanChoice == 1:
            if len(Troop1_15) >= 1:
                Botattack(Troop3_16,Troop1_15,Troop3_15,R15MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_15) >= 1:
                Botattack(Troop3_16,Troop2_15,Troop3_15,R15MinMax,R14MinMax,R16MinMax)
            if len(Troop3_15) >= 1:
                count = 1
                for i in Troop3_16:
                    if count >= len(Troop3_16):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_16.remove(i)
                        Troop3_15.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_16.remove(i)
                        Troop3_15.append(i)
                    count += 1
            if len(Troop3_15) == 0:
                if len(Troop2_15) == 0:
                    if len(Troop1_15) == 0:
                        count = 1
                        for i in Troop3_16:
                            if count >= len(Troop3_16):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_16.remove(i)
                                Troop3_15.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_16.remove(i)
                                Troop3_15.append(i)
                            count += 1
        if RanChoice == 2:
            if len(Troop2_17) >= 1:
                Botattack(Troop3_16,Troop2_17,Troop3_17,R17MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_17) >= 1:
                Botattack(Troop3_16,Troop1_17,Troop3_17,R17MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_17) >= 1:
                count = 1 
                for i in Troop3_16:
                    if count >= len(Troop3_16):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 700  
                        Troop3_16.remove(i)
                        Troop3_17.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 700
                        Troop3_16.remove(i)
                        Troop3_17.append(i)
                    count += 1  
            if len(Troop2_17) == 0:
                if len(Troop1_17) == 0:
                    if len(Troop3_17) == 0:
                        count = 1
                        for i in Troop3_16:
                            if count >= len(Troop3_16):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 700
                                Troop3_16.remove(i)
                                Troop3_17.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 700
                                Troop3_16.remove(i)
                                Troop3_17.append(i)
                            count += 1
        if RanChoice == 3:
            if len(Troop2_5) >= 1:
                Botattack(Troop3_16,Troop2_5,Troop3_5,R5MinMax,R14MinMax,R16MinMax)
            elif len(Troop1_5) >= 1:
                Botattack(Troop3_16,Troop1_5,Troop3_5,R5MinMax,R4MinMax,R16MinMax)  
            elif len(Troop3_5) >= 1:
                count = 1 
                for i in Troop3_16:
                    if count >= len(Troop3_16):
                        break
                    elif count == 1:
                        i.rect.x = 945
                        i.rect.y = 530  
                        Troop3_16.remove(i)
                        Troop3_5.append(i)
                    else:
                        i.rect.x = 970
                        i.rect.y = 530
                        Troop3_16.remove(i)
                        Troop3_5.append(i)
                    count += 1  
            if len(Troop2_5) == 0:
                if len(Troop1_5) == 0:
                    if len(Troop3_5) == 0:
                        count = 1
                        for i in Troop3_16:
                            if count >= len(Troop3_16):
                                break
                            elif count == 1:
                                i.rect.x = 945
                                i.rect.y = 530
                                Troop3_16.remove(i)
                                Troop3_5.append(i)
                            else:
                                i.rect.x = 945
                                i.rect.y = 530
                                Troop3_16.remove(i)
                                Troop3_5.append(i)
                            count += 1

    if len(Troop3_17) > 1:
        RanChoice = random.randint(1,1)
        if RanChoice == 1:
            if len(Troop1_16) >= 1:
                Botattack(Troop3_17,Troop1_16,Troop3_16,R16MinMax,R4MinMax,R16MinMax)                    
            if len(Troop2_16) >= 1:
                Botattack(Troop3_17,Troop2_16,Troop3_16,R16MinMax,R14MinMax,R16MinMax)
            if len(Troop3_16) >= 1:
                count = 1
                for i in Troop3_17:
                    if count >= len(Troop3_17):
                        break
                    elif count == 1:
                        i.rect.x = 400
                        i.rect.y = 600  
                        Troop3_17.remove(i)
                        Troop3_16.append(i)
                    else:
                        i.rect.x = 450
                        i.rect.y = 650
                        Troop3_17.remove(i)
                        Troop3_16.append(i)
                    count += 1
            if len(Troop3_16) == 0:
                if len(Troop2_16) == 0:
                    if len(Troop1_16) == 0:
                        count = 1
                        for i in Troop3_17:
                            if count >= len(Troop3_17):
                                break
                            elif count == 1:
                                i.rect.x = 400
                                i.rect.y = 600
                                Troop3_17.remove(i)
                                Troop3_16.append(i)
                            else:
                                i.rect.x = 450
                                i.rect.y = 600
                                Troop3_17.remove(i)
                                Troop3_16.append(i)
                            count += 1





def WinLossCheck():
    if len(Troop1_1) == 0:
        if len(Troop1_2) == 0:
            if len(Troop1_3) == 0:
                if len(Troop1_4) == 0:
                    if len(Troop1_5) == 0:
                        if len(Troop1_6) == 0:
                            if len(Troop1_7) == 0:
                                if len(Troop1_8) == 0:
                                    if len(Troop1_10) == 0:
                                        if len(Troop1_11) == 0:
                                            if len(Troop1_12) == 0:
                                                if len(Troop1_13) == 0:
                                                    if len(Troop1_14) == 0:
                                                        if len(Troop1_15) == 0:
                                                            if len(Troop1_16) == 0:
                                                                if len(Troop1_17) == 0:
                                                                    print("You Lost")
                                                                    import Menu
                                                                    sys.exit()
    if len(Troop2_1) and len(Troop3_1) == 0:
        if len(Troop2_2) and len(Troop3_2) == 0:
            if len(Troop2_3) and len(Troop3_3) == 0:
                if len(Troop2_4) and len(Troop3_4) == 0:
                    if len(Troop2_5) and len(Troop3_5) == 0:
                        if len(Troop2_6) and len(Troop3_6) == 0:
                            if len(Troop2_7) and len(Troop3_7) == 0:
                                if len(Troop2_8) and len(Troop3_8) == 0:
                                    if len(Troop2_9) and len(Troop3_9) == 0:
                                        if len(Troop2_10) and len(Troop3_10) == 0:
                                            if len(Troop2_11) and len(Troop3_11) == 0:
                                                if len(Troop2_12) and len(Troop3_12) == 0:
                                                    if len(Troop2_13) and len(Troop3_13) == 0:
                                                        if len(Troop2_14) and len(Troop3_14) == 0:
                                                            if len(Troop2_15) and len(Troop3_15) == 0:
                                                                if len(Troop2_16) and len(Troop3_16) == 0:
                                                                    if len(Troop2_16) and len(Troop3_16) == 0:
                                                                        print("You Won")
                                                                        import Menu
                                                                        sys.exit()




def Botattack(Troop1,Troop2,FortRegion,Region,DefendingStartR,RegionStart):
    ran1 = random.randint(1,6)
    ran2 = random.randint(1,6)
    ranAmount2 = ran2*len(Troop2)
    ranAmount1 = ran1*len(Troop1) - 1
    if ranAmount1 > ranAmount2:
        count = 1
        count2 = 1
        count3 = 1 
        for i in Troop1:
            if count > len(Troop1):
                break
            if count == 1:
                i.rect.x = (Region[0] + Region[1]) / 2
                i.rect.y = (Region[2] + Region[3]) / 2
                Troop1.remove(i)
                FortRegion.append(i)
            else:
                i.rect.x = ((Region[0] + Region[1]) / 2) + 50
                i.rect.y = ((Region[2] + Region[3]) / 2)
                Troop1.remove(i)
                FortRegion.append(i)
        count += 1
        for i in Troop2:
            if count3 == 1:
                Troop2.remove(i)
                all_sprites_list.remove(i)
            elif len(Troop2) == 0:
                break
            elif count3 == 2:
                Troop2.remove(i)
                DefendingStartR.append(i)
                i.rect.x = (RegionStart[0] + RegionStart[1]) / 2
                i.rect.y = (RegionStart[2] + RegionStart[3]) / 2
            else:
                Troop2.remove(i)
                DefendingStartR.append(i)
                i.rect.x = (RegionStart[0] + RegionStart[1]) / 2 + 50
                i.rect.y = (RegionStart[2] + RegionStart[3]) / 2  
            count3 += 1   
    else:
        print("Loss")
        count2 = 1
        for i in Troop1:
            if count2 == 2:
                break
            AllTroops.remove(i)
            Troop1.remove(i) 
            all_sprites_list.remove(i)


def CheckInRegion(x,y):
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global R7
    global R8
    global R9
    global R10
    global R11
    global R12
    global R13
    global R14
    global R15
    global R16
    global R17
    R1 = False
    R2 = False
    R3 = False
    R4 = False
    R5 = False
    R6 = False
    R7 = False
    R8 = False
    R9 = False
    R10 = False
    R11 = False
    R12 = False
    R13 = False
    R14 = False
    R15 = False
    R16 = False
    R17 = False
    if (1050 < x and 1240 > x) and (450 < y and 564 > y):
        R1 = True
        return R1
    if (975 < x and 1200 > x) and (200 < y and 340 > y):
        R2 = True
        return R2
    if (973 < x and 1202 > x) and (166 < y and 192 > y):
        R3 = True
        return R3        
    if (950 < x and 1250 > x) and (340 < y and 450 > y):
        R4 = True
        return R4
    if (937 < x and 974 > x) and (510 < y and 605 > y):
        R5 = True
        return R5
    if (1090 < x and 1162 > x) and (647 < y and 762 > y):
        R6 = True
        return R6
    if (1165 < x and 1221 > x) and (646 < y and 760 > y):
        R7 = True
        return R7 
    if (1016 < x and 1090 > x) and (660 < y and 772 > y):
        R8 = True
        return R8
    if (635 < x and 761 > x) and (337 < y and 374 > y):
        R9 = True
        return R9 
    if (691 < x and 840 > x) and (149 < y and 224 > y):
        R10 = True
        return R10
    if (427 < x and 507 > x) and (127 < y and 234 > y):
        R11 = True
        return R11
    if (426 < x and 482 > x) and (237 < y and 287 > y):
        R12 = True
        return R12
    if (254 < x and 407 > x) and (238 < y and 412 > y):
        R13 = True
        return R13
    if (245 < x and 425 > x) and (121 < y and 236 > y):
        R14 = True
        return R14
    if (344 < x and 500 > x) and (472 < y and 577 > y):
        R15 = True
        return R15
    if (339 < x and 496 > x) and (568 < y and 679 > y):
        R16 = True
        return R16
    if (320 < x and 468 > x) and (690 < y and 739 > y):
        R16 = True
        return R17


def attack(Troop1,Troop2,FortRegion, DefendingStartR,StartRegion,AttackRegion,DStartRegion):
    ran1 = random.randint(1,6)
    ran2 = random.randint(1,6)
    attackAmount = int(input("How many troops do you want to send?: "))
    if attackAmount < len(Troop1) and attackAmount > 0:
        ranAmount1 = ran1*attackAmount
        ranAmount2 = ran2*len(Troop2)
        #print("Player 1 score - ", ranAmount1)
        #print("Player 2 score - ", ranAmount2)
        count = 1
        
        for i in Troop1:
            if count > attackAmount:
                break
            if count == 1:
                i.rect.x = (AttackRegion[0] + AttackRegion[1]) / 2.2
                i.rect.y = (AttackRegion[2] + AttackRegion[3]) / 2
            else:   
                i.rect.x = (AttackRegion[0] + AttackRegion[1]) / 2 + 50
                i.rect.y = (AttackRegion[0] + AttackRegion[1]) / 2
            i.AttackP1()
            count += 1 
        for i in Troop2:
            if i in AllTroop3:
                i.AttackP3()
            if i in AllTroop2:
                i.AttackP2()
        click = pygame.mouse.get_pressed()

        if ranAmount1 > ranAmount2:
            for i in Troop1:
                i.IdleP1()
            for i in Troop2:
                if i in AllTroop3:
                    i.IdleP3()
                if i in AllTroop2:
                    i.IdleP2()
            lengthTR1 = len(Troop1)
            print("You won attack!")
            if lengthTR1 + 1 == 4:
                Player1Troop4 = PlayerTroop1("Player1TroopIdle.JPG.png")
                Troop1.append(Player1Troop4)
                AllTroop1.append(Player1Troop4)                         ####
                AllTroops.append(Player1Troop4)
                all_sprites_list.add(Player1Troop4)
                Player1Troop4.rect.x = (StartRegion[0] + StartRegion[1]) / 2
                Player1Troop4.rect.y = (StartRegion[2] + StartRegion[3]) / 2
            elif lengthTR1 + 1 == 3:
                Player1Troop3 = PlayerTroop1("Player1TroopIdle.JPG.png")
                Troop1.append(Player1Troop3)
                AllTroop1.append(Player1Troop3)                         ####
                AllTroops.append(Player1Troop3)
                all_sprites_list.add(Player1Troop3)
                Player1Troop3.rect.x = (StartRegion[0] + StartRegion[1]) / 2
                Player1Troop3.rect.y = (StartRegion[2] + StartRegion[3]) / 2
            elif lengthTR1 + 1 == 5:
                Player1Troop5 = PlayerTroop1("Player1TroopIdle.JPG.png")
                Troop1.append(Player1Troop5)
                AllTroop1.append(Player1Troop5)                         ####
                AllTroops.append(Player1Troop5)
                all_sprites_list.add(Player1Troop5)
                Player1Troop5.rect.x = (StartRegion[0] + StartRegion[1]) / 2
                Player1Troop5.rect.y = (StartRegion[2] + StartRegion[3]) / 2
            count = 1
            for i in Troop1:
                if count > attackAmount:
                    break
                if count == 1:
                    i.rect.x = (AttackRegion[0] + AttackRegion[1]) / 2
                    i.rect.y = (AttackRegion[2] + AttackRegion[3]) / 2
                    Troop1.remove(i)
                    FortRegion.append(i)
                else:
                    i.rect.x = (AttackRegion[0] + AttackRegion[1]) / 2 + 50
                    i.rect.y = (AttackRegion[0] + AttackRegion[1]) / 2
                    Troop1.remove(i)
                    FortRegion.append(i)
                count += 1
            for i in Troop2:
                i.rect.x = (DStartRegion[0] + DStartRegion[1]) / 2
                i.rect.y = (DStartRegion[2] + DStartRegion[3]) / 2
                Troop2.remove(i)
                DefendingStartR.append(i)
        else:
            count2 = 1
            
            print("You lost attack")
            for i in Troop1:
                i.IdleP1()
            for i in Troop2:
                if i in AllTroop3:
                    i.IdleP3()
                if i in AllTroop2:
                    i.IdleP2()
            for i in Troop1:
                if count2 == 2:
                    break
                AllTroops.remove(i)
                AllTroop1.remove(i)
                Troop1.remove(i) 
                all_sprites_list.remove(i)
                count2 += 2
    else:
        print("Invalid amount of troops")

def timeout():
    time.sleep(3)

RegionOption = int(input("What region would you like to select: "))

def ValidToFightUser(CheckInRegions,RegionOption):
    AttackCheck = False
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    R1MinMax = (xSize - 350,xSize - 160,ySize - 450,ySize - 336)
    R2MinMax = (xSize - 425,xSize - 200,ySize - 700,ySize - 560)
    R3MinMax = (xSize - 427,xSize - 198,ySize - 735,ySize - 708)
    R4MinMax = (xSize - 450,xSize - 150,ySize - 560,ySize - 450)
    R5MinMax = (xSize - 463,xSize - 426,ySize - 390,ySize - 295)
    R6MinMax = (xSize - 310,xSize - 238,ySize - 233,ySize - 138)
    R7MinMax = (xSize - 235,xSize - 179,ySize - 234,ySize - 140)
    R8MinMax = (xSize - 384,xSize - 310,ySize - 240,ySize - 128)
    R9MinMax = (xSize - 765,xSize - 639,ySize - 560,ySize - 326)
    R10MinMax = (xSize - 709,xSize - 560,ySize - 751,ySize - 676)
    R11MinMax = (xSize - 973,xSize - 893,ySize - 773,ySize - 666)
    R12MinMax = (xSize - 974,xSize - 918,ySize - 663,ySize - 613)
    R13MinMax = (xSize - 1146,xSize - 993,ySize - 662,ySize - 488)
    R14MinMax = (xSize - 1155,xSize - 975, ySize - 780, ySize - 665)
    R15MinMax = (xSize - 1056,xSize - 900,ySize - 428,ySize - 323)
    R16MinMax = (xSize - 1061,xSize - 904,ySize - 332,ySize - 221)
    R17MinMax = (xSize - 1080,xSize - 932,ySize - 210,ySize - 161)
    RC1 = (xSize - 350 < cur[0] and xSize - 160 > cur[0]) and (ySize - 450 < cur[1] and ySize - 336 > cur[1])
    RC2 = (xSize - 425 < cur[0] and xSize - 160 > cur[0]) and (ySize - 700 < cur[1] and ySize - 560 > cur[1])
    RC3 = (xSize - 427 < cur[0] and xSize - 160 > cur[0]) and (ySize - 735 < cur[1] and ySize - 708 > cur[1])
    RC4 = (xSize - 450 < cur[0] and xSize - 160 > cur[0]) and (ySize - 560 < cur[1] and ySize - 450 > cur[1])
    RC5 = (xSize - 463 < cur[0] and xSize - 160 > cur[0]) and (ySize - 390 < cur[1] and ySize - 295 > cur[1])
    RC6 = (xSize - 310 < cur[0] and xSize - 160 > cur[0]) and (ySize - 233 < cur[1] and ySize - 138 > cur[1])
    RC7 = (xSize - 235 < cur[0] and xSize - 160 > cur[0]) and (ySize - 234 < cur[1] and ySize - 140 > cur[1])
    RC8 = (xSize - 384 < cur[0] and xSize - 160 > cur[0]) and (ySize - 240 < cur[1] and ySize - 128 > cur[1])
    RC9 = (xSize - 765 < cur[0] and xSize - 160 > cur[0]) and (ySize - 560 < cur[1] and ySize - 326 > cur[1])
    RC10 = (xSize - 709 < cur[0] and xSize - 160 > cur[0]) and (ySize - 751 < cur[1] and ySize - 676 > cur[1])
    RC11 = (xSize - 973 < cur[0] and xSize - 160 > cur[0]) and (ySize - 773 < cur[1] and ySize - 666 > cur[1])
    RC12 = (xSize - 974 < cur[0] and xSize - 160 > cur[0]) and (ySize - 663 < cur[1] and ySize - 613 > cur[1])
    RC13 = (xSize - 1146 < cur[0] and xSize - 160 > cur[0]) and (ySize - 662 < cur[1] and ySize - 488 > cur[1])
    RC14 = (xSize - 1155 < cur[0] and xSize - 160 > cur[0]) and (ySize - 780 < cur[1] and ySize - 665 > cur[1])
    RC15 = (xSize - 1056 < cur[0] and xSize - 160 > cur[0]) and (ySize - 428 < cur[1] and ySize - 323 > cur[1])
    RC16 = (xSize - 1061 < cur[0] and xSize - 160 > cur[0]) and (ySize - 332 < cur[1] and ySize - 221 > cur[1])
    RC17 = (xSize - 1080 < cur[0] and xSize - 160 > cur[0]) and (ySize - 210 < cur[1] and ySize - 161 > cur[1])
    currentX = pygame.mouse.get_pos()[0]
    currentY = pygame.mouse.get_pos()[1]
    #1
    if RegionOption == 1:
        if len(Troop1_1) >= 1:
            if len(Troop2_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_1,Troop2_4,Troop1_4,Troop2_14,R4MinMax,R4MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_5) >= 1:
                if RC5:
                    if click[0] == 1:
                        attack(Troop1_1,Troop2_5,Troop1_5,Troop2_14,R4MinMax,R5MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_6) >= 1:
                if RC6:
                    if click[0] == 1:
                        attack(Troop1_1,Troop2_6,Troop1_6,Troop2_14,R4MinMax,R6MinMax,R14MinMax)
                        AttackCheck = True                      
            if len(Troop3_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_1,Troop3_4,Troop1_4,Troop3_16,R4MinMax,R4MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_5) >= 1:
                if RC5:
                    if click[0] == 1:
                        attack(Troop1_4,Troop3_5,Troop1_5,Troop3_16,R4MinMax,R5MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_6) >= 1:
                if RC6:
                    if click[0] == 1:
                        attack(Troop1_1,Troop3_6,Troop1_6,Troop3_16,R4MinMax,R6MinMax,R16MinMax)
                        AttackCheck = True    
            if AttackCheck == False:
                if len(Troop1_5) >= 1:
                    if RC5:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_1:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_1.remove(i)
                                        Troop1_5.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_1.remove(i)
                                        Troop1_5.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_4) >= 1:
                    if RC4:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_1:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_1.remove(i)
                                        Troop1_4.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_1.remove(i)
                                        Troop1_4.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_6) >= 1:
                    if RC6:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_1:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_1.remove(i)
                                        Troop1_4.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_1.remove(i)
                                        Troop1_4.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_4) == 0:
                if len(Troop2_4) == 0:
                    if len(Troop3_4) == 0:
                        if RC4:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_1:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_1.remove(i)
                                            Troop1_4.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_1.remove(i)
                                            Troop1_4.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_5) == 0:
                if len(Troop2_5) == 0:
                    if len(Troop3_5) == 0:
                        if RC5:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_1:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_1.remove(i)
                                            Troop1_5.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_1.remove(i)
                                            Troop1_5.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_6) == 0:
                if len(Troop2_6) == 0:
                    if len(Troop3_6) == 0:
                        if RC1:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_1) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_1:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_1.remove(i)
                                            Troop1_6.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_1.remove(i)
                                            Troop1_6.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 2:
        if len(Troop1_2) >= 1:
            if len(Troop2_3) >= 1:
                if RC3:
                    if click[0] == 1: 
                        attack(Troop1_2,Troop2_3,Troop1_3,Troop2_14,R4MinMax,R3MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_4) >= 1:
                if RC4:
                    if click[0] == 1:
                        attack(Troop1_1,Troop2_4,Troop1_4,Troop2_14,R4MinMax,R4MinMax,R14MinMax)    
                        AttackCheck = True              
            if len(Troop3_3) >= 1:
                if RC3:
                    if click[0] == 1: 
                        attack(Troop1_1,Troop3_3,Troop1_3,Troop3_16,R4MinMax,R3MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_4) >= 1:
                if RC4:
                    if click[0] == 1:
                        attack(Troop1_1,Troop3_4,Troop1_4,Troop3_16,R4MinMax,R4MinMax,R16MinMax)
                        AttackCheck = True 
            if AttackCheck == False:
                if len(Troop1_3) >= 1:
                    if RC3:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_2) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_2:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_2.remove(i)
                                        Troop1_3.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_2.remove(i)
                                        Troop1_3.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_4) >= 1:
                    if RC4:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_2) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_2:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_2.remove(i)
                                        Troop1_4.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_2.remove(i)
                                        Troop1_4.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_3) == 0:
                if len(Troop2_3) == 0:
                    if len(Troop3_3) == 0:
                        if RC3:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_2) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_2:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_2.remove(i)
                                            Troop1_3.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_2.remove(i)
                                            Troop1_3.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_4) == 0:
                if len(Troop2_4) == 0:
                    if len(Troop3_4) == 0:
                        if RC4:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_2) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_2:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_2.remove(i)
                                            Troop1_4.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_2.remove(i)
                                            Troop1_4.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 3:
        if len(Troop1_3) >= 1:
            if len(Troop2_10) >= 1:
                if RC10:
                    if click[0] == 1: 
                        attack(Troop1_3,Troop2_10,Troop1_10,Troop2_14,R4MinMax,R10MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_2) >= 1:
                if RC2:
                    if click[0] == 1:
                        attack(Troop1_3,Troop2_2,Troop1_2,Troop2_14,R4MinMax,R2MinMax,R14MinMax)   
                        AttackCheck = True                  
            if len(Troop3_10) >= 1:
                if RC10:
                    if click[0] == 1: 
                        attack(Troop1_3,Troop3_10,Troop1_10,Troop3_16,R4MinMax,R10MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_2) >= 1:
                if RC2:
                    if click[0] == 1:
                        attack(Troop1_3,Troop3_2,Troop1_2,Troop3_16,R4MinMax,R2MinMax,R16MinMax)  
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_10) >= 1:
                    if RC10:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_3) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_3:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_3.remove(i)
                                        Troop1_10.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_3.remove(i)
                                        Troop1_10.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_2) >= 1:
                    if RC2:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_3) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_3:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_3.remove(i)
                                        Troop1_2.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_3.remove(i)
                                        Troop1_2.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_10) == 0:
                if len(Troop2_10) == 0:
                    if len(Troop3_10) == 0:
                        if RC10:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_3) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_3:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_3.remove(i)
                                            Troop1_10.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_3.remove(i)
                                            Troop1_10.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_2) == 0:
                if len(Troop2_2) == 0:
                    if len(Troop3_2) == 0:
                        if RC2:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_3) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_3:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_3.remove(i)
                                            Troop1_2.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_3.remove(i)
                                            Troop1_2.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 4:
        if len(Troop1_4) >= 1:
            if len(Troop2_2) >= 1:
                if RC2:
                    if click[0] == 1: 
                        attack(Troop1_4,Troop2_2,Troop1_2,Troop2_14,R4MinMax,R2MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_1) >= 1:
                if RC1:
                    if click[0] == 1:
                        attack(Troop1_4,Troop2_1,Troop1_1,Troop2_14,R4MinMax,R1MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_9) >= 1:
                if RC9:
                    if click[0] == 1:
                        attack(Troop1_4,Troop2_9,Troop1_9,Troop2_14,R4MinMax,R9MinMax,R14MinMax)
                        AttackCheck = True                      
            if len(Troop3_2) >= 1:
                if RC2:
                    if click[0] == 1: 
                        attack(Troop1_4,Troop3_2,Troop1_2,Troop3_16,R4MinMax,R2MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_1) >= 1:
                if RC1:
                    if click[0] == 1:
                        attack(Troop1_4,Troop3_1,Troop1_1,Troop3_16,R4MinMax,R1MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_9) >= 1:
                if RC9:
                    if click[0] == 1:
                        attack(Troop1_4,Troop3_9,Troop1_9,Troop3_16,R4MinMax,R9MinMax,R16MinMax) 
                        AttackCheck = True   
            if AttackCheck == False:
                if len(Troop1_2) >= 1:
                    if RC2:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_4:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_4.remove(i)
                                        Troop1_2.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_4.remove(i)
                                        Troop1_2.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_1) >= 1:
                    if RC1:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_4:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_4.remove(i)
                                        Troop1_1.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_4.remove(i)
                                        Troop1_1.append(i)
                                    count += 1
                            elif TroopAmount == 75:
                                pass
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_9) >= 1:
                    if RC9:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_4:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_4.remove(i)
                                        Troop1_9.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_4.remove(i)
                                        Troop1_9.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_9) == 0:
                    if len(Troop2_9) == 0:
                        if len(Troop3_9) == 0:
                            if RC9:
                                if click[0] == 1:
                                    TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                    if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                        count = 0
                                        for i in Troop1_4:
                                            if count > (TroopAmount - 1):
                                                break
                                            elif count == 1:
                                                i.rect.x = currentX + 50
                                                i.rect.y = currentY  
                                                Troop1_4.remove(i)
                                                Troop1_9.append(i)
                                            else:
                                                i.rect.x = currentX
                                                i.rect.y = currentY
                                                Troop1_4.remove(i)
                                                Troop1_9.append(i)
                                            count += 1
                                    else:
                                        print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_2) == 0:
                    if len(Troop2_2) == 0:
                        if len(Troop3_2) == 0:
                            if RC2:
                                if click[0] == 1:
                                    TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                    if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                        count = 0
                                        for i in Troop1_4:
                                            if count > (TroopAmount - 1):
                                                break
                                            elif count == 1:
                                                i.rect.x = currentX + 50
                                                i.rect.y = currentY  
                                                Troop1_4.remove(i)
                                                Troop1_2.append(i)
                                            else:
                                                i.rect.x = currentX
                                                i.rect.y = currentY
                                                Troop1_4.remove(i)
                                                Troop1_2.append(i)
                                            count += 1
                                    else:
                                        print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_1) == 0:
                    if len(Troop2_1) == 0:
                        if len(Troop3_1) == 0:
                            if RC1:
                                if click[0] == 1:
                                    TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                    if TroopAmount < len(Troop1_4) and TroopAmount >= 1:
                                        count = 0
                                        for i in Troop1_4:
                                            if count > (TroopAmount - 1):
                                                break
                                            elif count == 1:
                                                i.rect.x = currentX + 50
                                                i.rect.y = currentY  
                                                Troop1_4.remove(i)
                                                Troop1_1.append(i)
                                            else:
                                                i.rect.x = currentX
                                                i.rect.y = currentY
                                                Troop1_4.remove(i)
                                                Troop1_1.append(i)
                                            count += 1
                                    else:
                                        print("Invalid amount of troops")

    if RegionOption == 5:
        if len(Troop1_5) >= 1:
            if len(Troop2_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_5,Troop2_4,Troop1_4,Troop2_14,R4MinMax,R4MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_16) >= 1:
                if RC16:
                    if click[0] == 1:
                        attack(Troop1_5,Troop2_16,Troop1_16,Troop2_14,R4MinMax,R16MinMax,R14MinMax) 
                        AttackCheck = True              
            if len(Troop3_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_5,Troop3_4,Troop1_4,Troop3_16,R4MinMax,R4MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_16) >= 1:
                if RC16:
                    if click[0] == 1:
                        attack(Troop1_5,Troop3_16,Troop1_16,Troop3_16,R4MinMax,R16MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_2) >= 1:
                    if RC4:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_5) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_5:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_5.remove(i)
                                        Troop1_2.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_5.remove(i)
                                        Troop1_2.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_1) >= 1:
                    if RC16:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_5) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_5:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_5.remove(i)
                                        Troop1_1.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_5.remove(i)
                                        Troop1_1.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_9) == 0:
                if len(Troop2_9) == 0:
                    if len(Troop3_9) == 0:
                        if RC4:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_5) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_5:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_5.remove(i)
                                            Troop1_9.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_5.remove(i)
                                            Troop1_9.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_2) == 0:
                if len(Troop2_2) == 0:
                    if len(Troop3_2) == 0:
                        if RC16:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_5) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_5:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_5.remove(i)
                                            Troop1_2.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_5.remove(i)
                                            Troop1_2.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 6:
        if len(Troop1_6) >= 1:
            if len(Troop2_5) >= 1:
                if RC5:
                    if click[0] == 1: 
                        attack(Troop1_6,Troop2_5,Troop1_5,Troop2_14,R4MinMax,R5MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_7) >= 1:
                if RC7:
                    if click[0] == 1:
                        attack(Troop1_6,Troop2_7,Troop1_7,Troop2_14,R4MinMax,R7MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_8) >= 1:
                if RC8:
                    if click[0] == 1:
                        attack(Troop1_6,Troop2_8,Troop1_8,Troop2_14,R4MinMax,R8MinMax,R14MinMax)  
                        AttackCheck = True                    
            if len(Troop3_5) >= 1:
                if RC5:
                    if click[0] == 1: 
                        attack(Troop1_6,Troop3_5,Troop1_5,Troop3_16,R4MinMax,R5MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_7) >= 1:
                if RC7:
                    if click[0] == 1:
                        attack(Troop1_6,Troop3_5,Troop1_7,Troop3_16,R4MinMax,R7MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_8) >= 1:
                if RC8:
                    if click[0] == 1:
                        attack(Troop1_6,Troop3_8,Troop1_8,Troop3_16,R4MinMax,R8MinMax,R16MinMax) 
                        AttackCheck = True
            if AttackCheck == False:   
                if len(Troop1_5) >= 1:
                    if RC5:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_6:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_6.remove(i)
                                        Troop1_5.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_6.remove(i)
                                        Troop1_5.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_7) >= 1:
                    if RC7:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_6:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_6.remove(i)
                                        Troop1_7.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_6.remove(i)
                                        Troop1_7.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_8) >= 1:
                    if RC8:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_6:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_6.remove(i)
                                        Troop1_8.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_6.remove(i)
                                        Troop1_8.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_5) == 0:
                if len(Troop2_5) == 0:
                    if len(Troop3_5) == 0:
                        if RC5:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_6:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_6.remove(i)
                                            Troop1_5.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_6.remove(i)
                                            Troop1_5.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_7) == 0:
                if len(Troop2_7) == 0:
                    if len(Troop3_7) == 0:
                        if RC7:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_6:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_6.remove(i)
                                            Troop1_7.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_6.remove(i)
                                            Troop1_7.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_8) == 0:
                if len(Troop2_8) == 0:
                    if len(Troop3_8) == 0:
                        if RC8:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_6) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_6:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_6.remove(i)
                                            Troop1_8.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_6.remove(i)
                                            Troop1_8.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
                                
    if RegionOption == 7:
        if len(Troop1_7) >= 1:
            if len(Troop2_6) >= 1:
                if RC6:
                    if click[0] == 1: 
                        attack(Troop1_7,Troop2_6,Troop1_6,Troop2_14,R4MinMax,R6MinMax,R14MinMax)
                        AttackCheck = True
            if len(Troop3_6) >= 1:
                if RC6:
                    if click[0] == 1: 
                        attack(Troop1_7,Troop3_6,Troop1_6,Troop3_16,R4MinMax,R6MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_6) >= 1:
                    if RC6:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_7) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_7:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_7.remove(i)
                                        Troop1_6.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_7.remove(i)
                                        Troop1_6.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_6) == 0:
                if len(Troop2_6) == 0:
                    if len(Troop3_6) == 0:
                        if RC6:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_7) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_7:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_7.remove(i)
                                            Troop1_6.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_7.remove(i)
                                            Troop1_6.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 8:
        if len(Troop1_8) >= 1:
            if len(Troop2_6) >= 1:
                if RC6:
                    if click[0] == 1: 
                        attack(Troop1_8,Troop2_6,Troop1_6,Troop2_14,R4MinMax,R6MinMax,R14MinMax)   
                        AttackCheck = True                
            if len(Troop3_6) >= 1:
                if RC6:
                    if click[0] == 1: 
                        attack(Troop1_8,Troop3_6,Troop1_6,Troop3_16,R4MinMax,R6MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_6) >= 1:
                    if RC6:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_8) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_8:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_8.remove(i)
                                        Troop1_6.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_8.remove(i)
                                        Troop1_6.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_6) == 0:
                if len(Troop2_6) == 0:
                    if len(Troop3_6) == 0:
                        if RC6:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_8) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_8:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_8.remove(i)
                                            Troop1_6.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_8.remove(i)
                                            Troop1_6.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 9:
        if len(Troop1_9) >= 1:
            if len(Troop2_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_9,Troop2_4,Troop1_4,Troop2_14,R4MinMax,R4MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_9,Troop2_12,Troop1_12,Troop2_14,R4MinMax,R12MinMax,R14MinMax)
                        AttackCheck = True
            if len(Troop3_4) >= 1:
                if RC4:
                    if click[0] == 1: 
                        attack(Troop1_9,Troop3_4,Troop1_4,Troop3_16,R4MinMax,R4MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_9,Troop3_12,Troop1_12,Troop3_16,R4MinMax,R12MinMax,R16MinMax) 
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_4) >= 1:
                    if RC4:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_9) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_9:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_9.remove(i)
                                        Troop1_4.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_9.remove(i)
                                        Troop1_4.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_12) >= 1:
                    if RC12:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_9) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_9:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_9.remove(i)
                                        Troop1_12.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_9.remove(i)
                                        Troop1_12.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_4) == 0:
                if len(Troop2_4) == 0:
                    if len(Troop3_4) == 0:
                        if RC4:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_9) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_9:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_9.remove(i)
                                            Troop1_4.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_9.remove(i)
                                            Troop1_4.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_12) == 0:
                if len(Troop2_12) == 0:
                    if len(Troop3_12) == 0:
                        if RC12:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_9) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_9:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_9.remove(i)
                                            Troop1_12.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_9.remove(i)
                                            Troop1_12.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 10:
        if len(Troop1_10) >= 1:
            if len(Troop2_3) >= 1:
                if RC3:
                    if click[0] == 1: 
                        attack(Troop1_10,Troop2_3,Troop1_3,Troop2_14,R4MinMax,R3MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_11) >= 1:
                if RC11:
                    if click[0] == 1:
                        attack(Troop1_10,Troop2_11,Troop1_11,Troop2_14,R4MinMax,R11MinMax,R14MinMax) 
                        AttackCheck = True                
            if len(Troop3_3) >= 1:
                if RC3:
                    if click[0] == 1: 
                        attack(Troop1_10,Troop3_3,Troop1_3,Troop3_16,R4MinMax,R3MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_11) >= 1:
                if RC11:
                    if click[0] == 1:
                        attack(Troop1_10,Troop3_11,Troop1_11,Troop3_16,R4MinMax,R11MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_3) >= 1:
                    if RC3:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_10) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_10:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_10.remove(i)
                                        Troop1_3.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_10.remove(i)
                                        Troop1_3.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_11) >= 1:
                    if RC11:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_10) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_10:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_10.remove(i)
                                        Troop1_11.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_10.remove(i)
                                        Troop1_11.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_3) == 0:
                if len(Troop2_3) == 0:
                    if len(Troop3_3) == 0:
                        if RC3:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_10) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_10:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_10.remove(i)
                                            Troop1_3.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_10.remove(i)
                                            Troop1_3.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_11) == 0:
                if len(Troop2_11) == 0:
                    if len(Troop3_11) == 0:
                        if RC11:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_10) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_10:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_10.remove(i)
                                            Troop1_11.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_10.remove(i)
                                            Troop1_11.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 11:
        if len(Troop1_11) >= 1:
            if len(Troop2_10) >= 1:
                if RC10:
                    if click[0] == 1: 
                        attack(Troop1_11,Troop2_10,Troop1_10,Troop2_14,R4MinMax,R10MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_11,Troop2_12,Troop1_12,Troop2_14,R4MinMax,R12MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_14) >= 1:
                if RC14:
                    if click[0] == 1:
                        attack(Troop1_11,Troop2_14,Troop1_14,Troop2_14,R4MinMax,R14MinMax,R14MinMax)  
                        AttackCheck = True                    
            if len(Troop3_10) >= 1:
                if RC10:
                    if click[0] == 1: 
                        attack(Troop1_11,Troop3_10,Troop1_10,Troop3_16,R4MinMax,R10MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_11,Troop3_10,Troop1_12,Troop3_16,R4MinMax,R12MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_14) >= 1:
                if RC14:
                    if click[0] == 1:
                        attack(Troop1_11,Troop3_14,Troop1_14,Troop3_16,R4MinMax,R14MinMax,R16MinMax) 
                        AttackCheck = True
            if AttackCheck == False:   
                if len(Troop1_10) >= 1:
                    if RC10:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_11:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_11.remove(i)
                                        Troop1_10.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_11.remove(i)
                                        Troop1_10.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_12) >= 1:
                    if RC12:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_11:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_11.remove(i)
                                        Troop1_12.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_11.remove(i)
                                        Troop1_12.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_14) >= 1:
                    if RC14:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_11:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_11.remove(i)
                                        Troop1_14.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_11.remove(i)
                                        Troop1_14.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_10) == 0:
                if len(Troop2_10) == 0:
                    if len(Troop3_10) == 0:
                        if RC10:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_11:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_11.remove(i)
                                            Troop1_10.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_11.remove(i)
                                            Troop1_10.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_12) == 0:
                if len(Troop2_12) == 0:
                    if len(Troop3_12) == 0:
                        if RC12:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_11:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_11.remove(i)
                                            Troop1_12.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_11.remove(i)
                                            Troop1_12.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_14) == 0:
                if len(Troop2_14) == 0:
                    if len(Troop3_14) == 0:
                        if RC14:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_11) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_11:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_11.remove(i)
                                            Troop1_14.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_11.remove(i)
                                            Troop1_14.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 12:
        if len(Troop1_12) >= 1:
            if len(Troop2_9) >= 1:
                if RC9:
                    if click[0] == 1: 
                        attack(Troop1_12,Troop2_9,Troop1_9,Troop2_14,R4MinMax,R9MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_11) >= 1:
                if RC11:
                    if click[0] == 1:
                        attack(Troop1_12,Troop2_11,Troop1_11,Troop2_14,R4MinMax,R11MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_12,Troop2_13,Troop1_13,Troop2_14,R4MinMax,R13MinMax,R14MinMax)  
                        AttackCheck = True                    
            if len(Troop3_9) >= 1:
                if RC9:
                    if click[0] == 1: 
                        attack(Troop1_12,Troop3_9,Troop1_9,Troop3_16,R4MinMax,R9MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_11) >= 1:
                if RC11:
                    if click[0] == 1:
                        attack(Troop1_12,Troop3_11,Troop1_11,Troop3_16,R4MinMax,R11MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_12,Troop3_13,Troop1_13,Troop3_16,R4MinMax,R13MinMax,R16MinMax)   
                        AttackCheck = True
            if AttackCheck == False: 
                if len(Troop1_9) >= 1:
                    if RC9:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_12:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_12.remove(i)
                                        Troop1_9.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_12.remove(i)
                                        Troop1_9.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_11) >= 1:
                    if RC11:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_12:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_12.remove(i)
                                        Troop1_11.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_12.remove(i)
                                        Troop1_11.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_13) >= 1:
                    if RC13:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_12:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_12.remove(i)
                                        Troop1_13.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_12.remove(i)
                                        Troop1_13.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_9) == 0:
                if len(Troop2_9) == 0:
                    if len(Troop3_9) == 0:
                        if RC9:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_12:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_12.remove(i)
                                            Troop1_9.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_12.remove(i)
                                            Troop1_9.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_11) == 0:
                if len(Troop2_11) == 0:
                    if len(Troop3_11) == 0:
                        if RC11:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_12:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_12.remove(i)
                                            Troop1_11.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_12.remove(i)
                                            Troop1_11.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_13) == 0:
                if len(Troop2_13) == 0:
                    if len(Troop3_13) == 0:
                        if RC13:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_12) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_12:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_12.remove(i)
                                            Troop1_13.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_12.remove(i)
                                            Troop1_13.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 13:
        if len(Troop1_13) >= 1:
            if len(Troop2_14) >= 1:
                if RC14:
                    if click[0] == 1: 
                        attack(Troop1_14,Troop2_14,Troop1_14,Troop2_14,R4MinMax,R14MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_14,Troop2_12,Troop1_12,Troop2_14,R4MinMax,R12MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_15) >= 1:
                if RC15:
                    if click[0] == 1:
                        attack(Troop1_14,Troop2_15,Troop1_15,Troop2_14,R4MinMax,R15MinMax,R14MinMax) 
                        AttackCheck = True                    
            if len(Troop3_14) >= 1:
                if RC14:
                    if click[0] == 1: 
                        attack(Troop1_14,Troop3_14,Troop1_14,Troop3_16,R4MinMax,R14MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_12) >= 1:
                if RC12:
                    if click[0] == 1:
                        attack(Troop1_14,Troop3_12,Troop1_12,Troop3_16,R4MinMax,R12MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_15) >= 1:
                if RC15:
                    if click[0] == 1:
                        attack(Troop1_14,Troop3_15,Troop1_15,Troop3_16,R4MinMax,R15MinMax,R16MinMax) 
                        AttackCheck = True 
            if AttackCheck == False:  
                if len(Troop1_14) >= 1:
                    if RC14:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_13:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_13.remove(i)
                                        Troop1_14.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_13.remove(i)
                                        Troop1_14.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_12) >= 1:
                    if RC12:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_13:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_13.remove(i)
                                        Troop1_12.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_13.remove(i)
                                        Troop1_12.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_15) >= 1:
                    if RC15:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_13:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_13.remove(i)
                                        Troop1_15.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_13.remove(i)
                                        Troop1_15.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_14) == 0:
                if len(Troop2_14) == 0:
                    if len(Troop3_14) == 0:
                        if RC14:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_13:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_13.remove(i)
                                            Troop1_14.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_13.remove(i)
                                            Troop1_14.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_12) == 0:
                if len(Troop2_12) == 0:
                    if len(Troop3_12) == 0:
                        if RC12:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_13:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_13.remove(i)
                                            Troop1_12.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_13.remove(i)
                                            Troop1_12.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_15) == 0:
                if len(Troop2_15) == 0:
                    if len(Troop3_15) == 0:
                        if RC15:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_13) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_13:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_13.remove(i)
                                            Troop1_15.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_13.remove(i)
                                            Troop1_15.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 14:
        if len(Troop1_14) >= 1:
            if len(Troop2_11) >= 1:
                if RC11:
                    if click[0] == 1: 
                        attack(Troop1_14,Troop2_11,Troop1_11,Troop2_14,R4MinMa,R11MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_14,Troop2_13,Troop1_13,Troop2_14,R4MinMax,R13MinMax,R14MinMax)    
                        AttackCheck = True            
            if len(Troop3_11) >= 1:
                if RC11:
                    if click[0] == 1: 
                        attack(Troop1_14,Troop3_11,Troop1_11,Troop3_16,R4MinMax,R11MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_14,Troop3_13,Troop1_13,Troop3_16,R4MinMax,R13MinMax,R16MinMax) 
                        AttackCheck = True 
            if AttackCheck == False:
                if len(Troop1_11) >= 1:
                    if RC11:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_14) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_14:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_14.remove(i)
                                        Troop1_11.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_14.remove(i)
                                        Troop1_11.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_13) >= 1:
                    if RC13:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_14) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_14:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_14.remove(i)
                                        Troop1_13.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_14.remove(i)
                                        Troop1_13.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_11) == 0:
                if len(Troop2_11) == 0:
                    if len(Troop3_11) == 0:
                        if RC11:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_14) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_14:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_14.remove(i)
                                            Troop1_11.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_14.remove(i)
                                            Troop1_11.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_13) == 0:
                if len(Troop2_13) == 0:
                    if len(Troop3_13) == 0:
                        if RC13:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_14) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_14:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_14.remove(i)
                                            Troop1_13.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_14.remove(i)
                                            Troop1_13.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


    if RegionOption == 15:
        if len(Troop1_15) >= 1:
            if len(Troop2_16) >= 1:
                if RC16:
                    if click[0] == 1: 
                        attack(Troop1_15,Troop2_16,Troop1_16,Troop2_14,R4MinMax,R16MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_15,Troop2_13,Troop1_13,Troop2_14,R4MinMax,R13MinMax,R14MinMax)  
                        AttackCheck = True                
            if len(Troop3_16) >= 1:
                if RC16:
                    if click[0] == 1: 
                        attack(Troop1_15,Troop3_16,Troop1_16,Troop3_16,R4MinMax,R16MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_13) >= 1:
                if RC13:
                    if click[0] == 1:
                        attack(Troop1_15,Troop3_13,Troop1_13,Troop3_16,R4MinMax,R13MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_16) >= 1:
                    if RC16:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_15) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_15:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_15.remove(i)
                                        Troop1_16.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_15.remove(i)
                                        Troop1_16.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_13) >= 1:
                    if RC13:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_15) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_15:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_15.remove(i)
                                        Troop1_13.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_15.remove(i)
                                        Troop1_13.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if len(Troop1_16) == 0:
                if len(Troop2_16) == 0:
                    if len(Troop3_16) == 0:
                        if RC16:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_15) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_15:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_15.remove(i)
                                            Troop1_16.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_15.remove(i)
                                            Troop1_16.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_13) == 0:
                if len(Troop2_13) == 0:
                    if len(Troop3_13) == 0:
                        if RC13:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_15) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_15:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_15.remove(i)
                                            Troop1_13.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_15.remove(i)
                                            Troop1_13.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 16:
        if len(Troop1_16) >= 1:
            if len(Troop2_15) >= 1:
                if RC15:
                    if click[0] == 1: 
                        attack(Troop1_16,Troop2_15,Troop1_15,Troop2_14,R4MinMax,R15MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_17) >= 1:
                if RC17:
                    if click[0] == 1:
                        attack(Troop1_16,Troop2_17,Troop1_17,Troop2_14,R4MinMax,R17MinMax,R14MinMax)
                        AttackCheck = True
            elif len(Troop2_5) >= 1:
                if RC5:
                    if click[0] == 1:
                        attack(Troop1_16,Troop2_5,Troop1_5,Troop2_14,R4MinMax,R5MinMax,R14MinMax)  
                        AttackCheck = True                    
            if len(Troop3_15) >= 1:
                if RC15:
                    if click[0] == 1: 
                        attack(Troop1_16,Troop3_15,Troop1_15,Troop3_16,R4MinMax,R15MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_17) >= 1:
                if RC17:
                    if click[0] == 1:
                        attack(Troop1_16,Troop3_17,Troop1_17,Troop3_16,R4MinMax,R17MinMax,R16MinMax)
                        AttackCheck = True
            elif len(Troop3_5) >= 1:
                if RC5:
                    if click[0] == 1:
                        attack(Troop1_16,Troop3_5,Troop1_5,Troop3_16,R4MinMax,R5MinMax,R16MinMax) 
                        AttackCheck = True
            if AttackCheck == False:   
                if len(Troop1_15) >= 1:
                    if RC15:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_16:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_16.remove(i)
                                        Troop1_15.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_16.remove(i)
                                        Troop1_15.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if AttackCheck == False:
                if len(Troop1_17) >= 1:
                    if RC17:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_16:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_16.remove(i)
                                        Troop1_17.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_16.remove(i)
                                        Troop1_17.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")  
            if AttackCheck == False:
                if len(Troop1_5) >= 1:
                    if RC5:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_16:
                                    if count > (TroopAmount - 1):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_16.remove(i)
                                        Troop1_5.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_16.remove(i)
                                        Troop1_5.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_15) == 0:
                if len(Troop2_15) == 0:
                    if len(Troop3_15) == 0:
                        if RC15:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_16:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_16.remove(i)
                                            Troop1_15.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_16.remove(i)
                                            Troop1_15.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_17) == 0:
                if len(Troop2_17) == 0:
                    if len(Troop3_17) == 0:
                        if RC17:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_16:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_16.remove(i)
                                            Troop1_17.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_16.remove(i)
                                            Troop1_17.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")
            if len(Troop1_5) == 0:
                if len(Troop2_5) == 0:
                    if len(Troop3_5) == 0:
                        if RC5:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_16) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_16:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_16.remove(i)
                                            Troop1_5.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_16.remove(i)
                                            Troop1_5.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")

    if RegionOption == 17:
        if len(Troop1_17) >= 1:
            if len(Troop2_16) >= 1:
                if RC16:
                    if click[0] == 1: 
                        attack(Troop1_17,Troop2_16,Troop1_16,Troop2_14,R4MinMax,R16MinMax,R14MinMax)   
                        AttackCheck = True              
            if len(Troop3_16) >= 1:
                if RC16:
                    if click[0] == 1: 
                        attack(Troop1_17,Troop3_16,Troop1_6,Troop3_16,R4MinMax,R16MinMax,R16MinMax)
                        AttackCheck = True
            if AttackCheck == False:
                if len(Troop1_16) >= 1:
                    if RC16:
                        if click[0] == 1: 
                            TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                            if TroopAmount < len(Troop1_17) and TroopAmount >= 1:
                                count = 0
                                for i in Troop1_17:
                                    if count > (TroopAmount):
                                        break
                                    elif count == 1:
                                        i.rect.x = currentX + 50
                                        i.rect.y = currentY  
                                        Troop1_17.remove(i)
                                        Troop1_16.append(i)
                                    else:
                                        i.rect.x = currentX
                                        i.rect.y = currentY
                                        Troop1_17.remove(i)
                                        Troop1_16.append(i)
                                    count += 1
                            else:
                                print("Invalid amount of troops")
            if len(Troop1_16) == 0:
                if len(Troop2_16) == 0:
                    if len(Troop3_16) == 0:
                        if RC16:
                            if click[0] == 1:
                                TroopAmount = int(input("Please enter the amount of troops you want to move - "))
                                if TroopAmount < len(Troop1_17) and TroopAmount >= 1:
                                    count = 0
                                    for i in Troop1_17:
                                        if count > (TroopAmount - 1):
                                            break
                                        elif count == 1:
                                            i.rect.x = currentX + 50
                                            i.rect.y = currentY  
                                            Troop1_17.remove(i)
                                            Troop1_16.append(i)
                                        else:
                                            i.rect.x = currentX
                                            i.rect.y = currentY
                                            Troop1_17.remove(i)
                                            Troop1_16.append(i)
                                        count += 1
                                else:
                                    print("Invalid amount of troops")


def regionCol():
    Map1_1 = pygame.image.load("Map1_1.png")
    Map1_4 = pygame.image.load("Map1_4.png")
    Map3_4 = pygame.image.load("Map3_4.png")
    Map1_2 = pygame.image.load("Map1_2.png")
    Map3_1 = pygame.image.load("Map3_1.png")
    Map1_3 = pygame.image.load("Map1_3.png")
    Map1_5 = pygame.image.load("Map1_5.png")
    Map1_6 = pygame.image.load("Map1_6.png")
    Map1_7 = pygame.image.load("Map1_7.png")
    Map1_8 = pygame.image.load("Map1_8.png")
    Map1_9 = pygame.image.load("Map1_9.png")
    Map1_10 = pygame.image.load("Map1_10.png")
    Map1_11 = pygame.image.load("Map1_11.png")
    Map1_12 = pygame.image.load("Map1_12.png")
    Map1_13 = pygame.image.load("Map1_13.png")
    Map1_14 = pygame.image.load("Map1_14.png")
    Map1_15 = pygame.image.load("Map1_15.png")
    Map1_16 = pygame.image.load("Map1_16.png")
    Map1_17 = pygame.image.load("Map1_17.png")
    Map2_1 = pygame.image.load("Map2_1.png")
    Map2_2 = pygame.image.load("Map2_2.png")
    Map2_3 = pygame.image.load("Map2_3.png")
    Map2_4 = pygame.image.load("Map2_4.png")
    Map2_5 = pygame.image.load("Map2_5.png")
    Map2_6 = pygame.image.load("Map2_6.png")
    Map2_7 = pygame.image.load("Map2_7.png")
    Map2_8 = pygame.image.load("Map2_8.png")
    Map2_9 = pygame.image.load("Map2_9.png")
    Map2_10 = pygame.image.load("Map2_10.png")
    Map2_11 = pygame.image.load("Map2_11.png")
    Map2_12 = pygame.image.load("Map2_12.png")
    Map2_13 = pygame.image.load("Map2_13.png")
    Map2_14 = pygame.image.load("Map2_14.png")
    Map2_15 = pygame.image.load("Map2_15.png")
    Map2_16 = pygame.image.load("Map2_16.png")
    Map2_17 = pygame.image.load("Map2_17.png")
    Map3_2 = pygame.image.load("Map3_2.png")
    Map3_3 = pygame.image.load("Map3_3.png")
    Map3_5 = pygame.image.load("Map3_5.png")
    Map3_6 = pygame.image.load("Map3_6.png")
    Map3_7 = pygame.image.load("Map3_7.png")
    Map3_8 = pygame.image.load("Map3_8.png")
    Map3_9 = pygame.image.load("Map3_9.png")
    Map3_10 = pygame.image.load("Map3_10.png")
    Map3_11 = pygame.image.load("Map3_11.png")
    Map3_12 = pygame.image.load("Map3_12.png")
    Map3_13 = pygame.image.load("Map3_13.png")
    Map3_14 = pygame.image.load("Map3_14.png")
    Map3_15 = pygame.image.load("Map3_15.png")
    Map3_16 = pygame.image.load("Map3_16.png")
    Map3_17 = pygame.image.load("Map3_17.png")



    if len(Troop1_4) >= 1:
        screen.blit(Map1_4, (920,285))
    if len(Troop3_4) >= 1:
        screen.blit(Map3_4, (920,285))
    if len(Troop1_2) >= 1:
        screen.blit(Map1_2, (658,32))
    if len(Troop3_1) >= 1:
        screen.blit(Map3_1, (965,425))
    if len(Troop1_3) >= 1:
        screen.blit(Map1_3, (913,85))
    if len(Troop1_5) >= 1:
        screen.blit(Map1_5, (900,480))
    if len(Troop1_6) >= 1:
        screen.blit(Map1_6, (1045,605))
    if len(Troop1_7) >= 1:
        screen.blit(Map1_7, (1140,620))
    if len(Troop1_8) >= 1:
        screen.blit(Map1_8, (915,620))
    if len(Troop1_9) >= 1:
        screen.blit(Map1_9, (595,270))
    if len(Troop1_10) >= 1:
        screen.blit(Map1_10, (675,140))
    if len(Troop1_11) >= 1:
        screen.blit(Map1_11, (420,125))
    if len(Troop1_12) >= 1:
        screen.blit(Map1_12, (410,215))
    if len(Troop1_13) >= 1:
        screen.blit(Map1_13, (242,235))
    if len(Troop1_14) >= 1:
        screen.blit(Map1_14, (235,115))
    if len(Troop1_15) >= 1:
        screen.blit(Map1_15, (335,435))
    if len(Troop1_16) >= 1:
        screen.blit(Map1_16, (323,565))
    if len(Troop1_17) >= 1:
        screen.blit(Map1_17, (285,620))
    if len(Troop1_1) >=1 :
        screen.blit(Map1_1, (965,425))
    if len(Troop2_1) >= 1:
        screen.blit(Map2_1, (965,425))
    if len(Troop2_2) >= 1:
        screen.blit(Map2_2, (658,32))
    if len(Troop2_3) >= 1:
        screen.blit(Map2_3, (913,85))
    if len(Troop2_4) >= 1:
        screen.blit(Map2_4, (920,285))
    if len(Troop2_5) >= 1:
        screen.blit(Map2_5, (900,480))
    if len(Troop2_6) >= 1:
        screen.blit(Map2_6, (1045,605))
    if len(Troop2_7) >= 1:
        screen.blit(Map2_7, (1140,620))
    if len(Troop2_8) >= 1:
        screen.blit(Map2_8, (915,620))
    if len(Troop2_9) >= 1:
        screen.blit(Map2_9, (595,270))
    if len(Troop2_10) >= 1:
        screen.blit(Map2_10, (675,140))
    if len(Troop2_11) >= 1:
        screen.blit(Map2_11, (420,125))
    if len(Troop1_12) >= 1:
        screen.blit(Map2_12, (410,215))
    if len(Troop2_13) >= 1:
        screen.blit(Map2_13, (242,235))
    if len(Troop2_14) >= 1:
        screen.blit(Map2_14, (235,115))
    if len(Troop2_15) >= 1:
        screen.blit(Map2_15, (335,435))
    if len(Troop2_16) >= 1:
        screen.blit(Map2_16, (323,565))
    if len(Troop2_17) >= 1:
        screen.blit(Map2_17, (285,620))
    if len(Troop3_2) >= 1:
        screen.blit(Map3_2, (658,32))
    if len(Troop3_3) >= 1:
        screen.blit(Map3_3, (913,85))
    if len(Troop3_5) >= 1:
        screen.blit(Map3_5, (900,480))
    if len(Troop3_6) >= 1:
        screen.blit(Map3_6, (1045,605))
    if len(Troop3_7) >= 1:
        screen.blit(Map3_7, (1140,620))
    if len(Troop3_8) >= 1:
        screen.blit(Map3_8, (915,620))
    if len(Troop3_9) >= 1:
        screen.blit(Map3_9, (595,270))
    if len(Troop3_10) >= 1:
        screen.blit(Map3_10, (675,140))
    if len(Troop3_11) >= 1:
        screen.blit(Map3_11, (420,125))
    if len(Troop3_12) >= 1:
        screen.blit(Map3_12, (410,215))
    if len(Troop3_13) >= 1:
        screen.blit(Map3_13, (242,235))
    if len(Troop3_14) >= 1:
        screen.blit(Map3_14, (235,115))
    if len(Troop3_15) >= 1:
        screen.blit(Map3_15, (335,435))
    if len(Troop3_16) >= 1:
        screen.blit(Map3_16, (323,565))
    if len(Troop3_17) >= 1:
        screen.blit(Map3_17, (285,620))




clock = pygame.time.Clock()

while running:
    ySize = pygame.display.Info().current_h 
    xSize = pygame.display.Info().current_w
    #cur = pygame.mouse.get_pos()
    #print(cur)
    ValidToFightUser(CheckInRegion,RegionOption)
    WinLossCheck()
    if xSize < 1400 or ySize < 900:
        screen = pygame.display.set_mode((1400,900), pygame.RESIZABLE)
    Map = pygame.image.load(Background)
    all_sprites_list.update()
    screen.fill((0,191,255))
    screen.blit(Map,(xSize/6,ySize/8.2))
    option_text()
    regionCol()
    NextTurn(NextTurnList)
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                import Pause
    pygame.display.flip()
    clock.tick(60) 
pygame.display.update()
