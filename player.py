import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self , pos , groups):
        super().__init__(groups)
        self.image = pygame.image.load('asset/nobita.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        
    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        
        if key[pygame.K_LEFT]:
            self.direction.x = -1
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    
    def update(self):
        self.input()
            

    
