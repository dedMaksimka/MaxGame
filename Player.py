from Consts import *
from game_objects import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((player_w, player_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(player_color), (0, 0, player_w, player_h))
        self.rect = pygame.Rect(x, y, player_w, player_h)
        self.v = 0
        self.jumps = 0

    def update(self):
        collide = (pygame.sprite.spritecollideany(self, platforms_group) or
                   pygame.sprite.spritecollideany(self, st_group))
        if collide:
            self.jumps = 0
        if not collide or self.v < 0:
            self.v += gravity / fps
            rect = self.rect
            rect.y += self.v
            self.rect = rect

    def move(self, x, y):
        if y != 0 and pygame.sprite.spritecollideany(self, st_group) or y == 0:
            self.rect = self.rect.move(x, y)
        self.update()

    def jump(self):
        if self.jumps > 1:
            return
        self.v = player_jump_speed
        self.jumps += 1
        self.update()

    def setPos(self, pos):
        self.rect.x = pos[0] - player_step
        self.rect.y = pos[1] - player_step
        self.v = 0