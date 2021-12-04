import pygame

pygame.init()

all_sprites = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
platforms_group = pygame.sprite.Group()
st_group = pygame.sprite.Group()
blocks_group = pygame.sprite.Group()

#Events

LOSE_EVENT = pygame.USEREVENT + 1
