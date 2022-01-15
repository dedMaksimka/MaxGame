from Consts import *
from game_objects import *
import pygame


def check_collision(obj):
    collide = pygame.sprite.spritecollideany(obj, all_groups)
    if not collide:
        return
    if obj.rect.y > collide.rect.y + 1:
        obj.rect.y -= side - 1 + obj.rect.y - collide.rect.y
        return
    # if obj.rect.x > collide.rect.x + 1:
    #     obj.rect.x -= side - 1 + obj.rect.x - collide.rect.x
    #     return
    # if obj.rect.x < collide.rect.x + 1:
    #     obj.rect.x += side - 1 + obj.rect.x - collide.rect.x
    #     return



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((player_w, player_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(player_color), (0, 0, player_w, player_h))
        self.rect = pygame.Rect(x, y, player_w, player_h)
        self.v = 0
        self.jumps = 0
        self.course = 1

    def update(self):
        collide = pygame.sprite.spritecollideany(self, all_groups)
        # if collide and self.rect.y - collide.rect.y < side - 1:
        #     self.rect.y -= side - 1 + self.rect.y - collide.rect.y
        if collide:
            self.jumps = 0
        if not collide or self.v < 0:
            self.v += gravity / fps
            rect = self.rect
            rect.y += self.v
            self.rect = rect
        if pygame.sprite.spritecollideany(self, enemies_group):
            pygame.time.set_timer(LOSE_EVENT, 1)

    def move(self, x, y):
        t = pygame.sprite.spritecollideany(self, stair_group)
        t2 = pygame.sprite.spritecollideany(self, blocks_group)
        if (y != 0 and t or y == 0 and not t2):
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
