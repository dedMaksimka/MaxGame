from Consts import *
from game_objects import *
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(platforms_group)
        self.image = pygame.Surface((platform_w, platform_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(platform_color), (0, 0, platform_w, platform_h))
        self.rect = pygame.Rect(x, y, platform_w, platform_h)


class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(st_group)
        self.image = pygame.Surface((stair_w, stair_h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color(stair_color), (0, 0, stair_w, stair_h))
        self.rect = pygame.Rect(x, y, stair_w, stair_h)