import pygame
import os
import sys
from Consts import *

pygame.init()

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
stair_group = pygame.sprite.Group()
blocks_group = pygame.sprite.Group()
all_groups = pygame.sprite.Group()
arrow_group = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Camera:
    def __init__(self):
        self.dx = 0

    def apply(self, obj):
        obj.rect.x += self.dx

    def update(self, target):
        # if target.rect.x >= size[0] // 2:
        self.dx = -(target.rect.x + target.rect.w // 2 - size[0] // 2)



#Events

LOSE_EVENT = pygame.USEREVENT + 1
