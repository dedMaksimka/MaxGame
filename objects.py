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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(enemies_group)
        self.image = pygame.Surface((player_w, player_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(enemy_color), (0, 0, player_w, player_h))
        self.rect = pygame.Rect(x, y, player_w, player_h)
        self.v = 0
        self.speed = enemy_speed

    def update(self):
        collide = (pygame.sprite.spritecollideany(self, platforms_group) or
                   pygame.sprite.spritecollideany(self, st_group))
        if not collide or self.v < 0:
            self.v += gravity / fps
            rect = self.rect
            rect.y += self.v
            self.rect = rect
        rect = self.rect
        rect.x += self.speed / fps
        print(rect.x, width - enemy_w)
        if rect.x > width - enemy_w:
            self.speed *= -1
        elif rect.x < 0:
            self.speed *= -1
        print(self.speed, rect)
        self.rect = rect