import pygame
from Consts import *

pygame.init()

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
stair_group = pygame.sprite.Group()
blocks_group = pygame.sprite.Group()
all_groups = pygame.sprite.Group()

class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        #obj.rect.y += self.dy

    def update(self, target):
        # if target.rect.x >= size[0] // 2:
        self.dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)
        #self.dy = -(target.rect.y + target.rect.h // 2 - size[1] // 2)


#Events

LOSE_EVENT = pygame.USEREVENT + 1
