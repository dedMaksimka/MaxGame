class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("blue"), (0, 0, 20, 20), 20)
        self.rect = pygame.Rect(x, y, 20, 20)
        self.v = 25

    def update(self):
        if not (pygame.sprite.spritecollideany(self, platforms_group) or
                pygame.sprite.spritecollideany(self, st_group)):
            self.rect = self.rect.move(0, fps / self.v)

    def move(self, x, y):
        if y != 0 and pygame.sprite.spritecollideany(self, st_group) or y == 0:
            self.rect = self.rect.move(x, y)
        self.update()

    def jump(self, x, y):
        self.rect = self.rect.move(x, y)
        self.update()

    def setPos(self, pos):
        self.rect.x = pos[0] - 10
        self.rect.y = pos[1] - 10