from Consts import *
from game_objects import *
import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__(all_sprites)
        self.add(arrow_group)
        self.image = pygame.Surface((arrow_w, arrow_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(arrow_color), (0, 0, arrow_w, arrow_h))
        self.rect = pygame.Rect(player.rect.x + player_w // 2, player.rect.y + player_h // 2, arrow_w, arrow_h)
        self.v = 0
        self.x = player.rect.x + player_w // 2
        self.speed = arrow_speed
        self.course = player.course

    def update(self):
        enemy = pygame.sprite.spritecollideany(self, enemies_group)
        collide = pygame.sprite.spritecollideany(self, all_groups)
        if enemy:
            enemy.shoot()
            self.kill()
        elif collide:
            self.kill()
        else:
            rect = self.rect
            self.x += self.course * self.speed / fps
            rect.x = self.x
            self.rect = rect


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, all_groups)
        self.add(blocks_group)
        self.image = pygame.Surface((block_w, block_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(platform_color), (0, 0, block_w, block_h))
        self.rect = pygame.Rect(x, y, block_w, block_h)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, all_groups)
        self.add(platforms_group)
        self.image = pygame.Surface((platform_w, platform_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(platform_color), (0, 0, platform_w, platform_h))
        self.rect = pygame.Rect(x, y, platform_w, platform_h)


class Stair(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, all_groups)
        self.add(stair_group)
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
        self.x = x
        self.v = 0
        self.speed = enemy_speed
        self.hp = enemy_hp

    def shoot(self):
        self.hp -= 100
        if self.hp <= 0:
            self.kill()

    def update(self):
        collide = pygame.sprite.spritecollideany(self, all_groups)
        # if collide and self.rect.y - collide.rect.y < side - 1:
        #     self.rect.y -= side - 1 + self.rect.y - collide.rect.y
        if not collide or self.v < 0:
            self.v += gravity / fps
            rect = self.rect
            rect.y += self.v
            self.rect = rect



        rect = self.rect

        self.x += self.speed / fps
        # print(self.x, size[0] - enemy_w)
        rect.x = self.x
        if rect.x > size[0] - enemy_w or rect.x < 0 or pygame.sprite.spritecollideany(self, blocks_group):
            self.speed *= -1
        # print(self.speed, rect)
        self.rect = rect