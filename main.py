from Consts import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((player_w, player_h), pygame.SRCALPHA, alpha)
        pygame.draw.rect(self.image, pygame.Color(player_color), (0, 0, player_w, player_h))
        self.rect = pygame.Rect(x, y, player_w, player_h)
        self.v = player_speed

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
        self.rect.x = pos[0] - player_step
        self.rect.y = pos[1] - player_step


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


if __name__ == '__main__':
    platforms = []
    pygame.init()
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    platforms_group = pygame.sprite.Group()
    st_group = pygame.sprite.Group()

    running = True
    clock = pygame.time.Clock()
    square = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
                        Stair(event.pos[0] - stair_w * 0,5, event.pos[1] - stair_h * 0,5)
                    elif square is None:
                        square = Player(event.pos[0] - player_step, event.pos[1] - player_step)
                    else:
                        square.setPos(event.pos)
                if event.button == 3:
                    Platform(event.pos[0] - 0, event.pos[1] - player_h)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    square.move(player_step, 0)
                if event.key == pygame.K_LEFT:
                    square.move(-player_step, 0)
                if event.key == pygame.K_UP:
                    square.move(0, -player_step)
                if event.key == pygame.K_DOWN:
                    square.move(0, player_step)
                if event.key == pygame.K_SPACE:
                    square.jump(0, -jump_m)
                if event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE:
                    square.jump(player_h, jump_m)
                if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE:
                    square.jump(-player_h, jump_m)

        screen.fill(pygame.Color(screen_color))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()