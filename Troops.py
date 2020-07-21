import pygame
pygame.init()

class Troop(pygame.sprite.Sprite):
    def __init__(self, TroopImage):
        super(Troop,self).__init__()
        self.TroopImage = TroopImage
        self.AttackImages = []
        self.IdleImages = []
        self.AttackImages.append(pygame.image.load("Player1Attacking.JPG.png").convert_alpha())
        self.AttackImages.append(pygame.image.load("Player2TroopAttack.JPG.png").convert_alpha())
        self.AttackImages.append(pygame.image.load("Player3TroopAttack.JPG.png").convert_alpha())
        self.IdleImages.append(pygame.image.load("Player1TroopIdle.JPG.png").convert_alpha())
        self.IdleImages.append(pygame.image.load("Player2TroopIdle.JPG.png").convert_alpha())
        self.IdleImages.append(pygame.image.load("Player3TroopIdle.JPG.png").convert_alpha())
        self._draw_me()
        self.rect = self.image.get_rect()
    def _draw_me(self):
        pass   
    def AttackP1(self):
        self.image = self.AttackImages[0] 
    def AttackP2(self):
        self.image = self.AttackImages[1] 
    def AttackP3(self):
        self.image = self.AttackImages[2]
    def IdleP1(self):
        self.image = self.IdleImages[0] 
    def IdleP2(self):
        self.image = self.IdleImages[1]
    def IdleP3(self):
        self.image = self.IdleImages[2]
class PlayerTroop1(Troop):
    def _draw_me(self):
        self.image = pygame.image.load(self.TroopImage).convert_alpha() 
