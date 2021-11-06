from Consts import *
from game_objects import *
from Player import Player
from objects import Platform, Stair
import pygame

if __name__ == '__main__':
    platforms = []

    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    player = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
                        Stair(event.pos[0] - stair_w // 2, event.pos[1] - stair_h // 2)
                    elif player is None:
                        player = Player(event.pos[0] - player_step, event.pos[1] - player_step)
                    else:
                        player.setPos(event.pos)
                if event.button == 3:
                    Platform(event.pos[0] - platform_w // 2, event.pos[1] - platform_h // 2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move(player_step, 0)
                if event.key == pygame.K_LEFT:
                    player.move(-player_step, 0)
                if event.key == pygame.K_UP:
                    player.move(0, -player_step)
                if event.key == pygame.K_DOWN:
                    player.move(0, player_step)
                if event.key == pygame.K_SPACE:
                    player.jump()
                # if event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE:
                #     player.jump(player_h, jump_m)
                # if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE:
                #     player.jump(-player_h, jump_m)

        screen.fill(pygame.Color(screen_color))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
