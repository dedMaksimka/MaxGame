from Consts import *
from game_objects import *
from Player import Player
from objects import *
import pygame

def keyboard_move_dispatcher(keys):
    if keys[pygame.K_RIGHT]:
        player.move(player_step, 0)
        player.course = 1
    if keys[pygame.K_LEFT]:
        player.move(-player_step, 0)
        player.course = -1
    if keys[pygame.K_UP]:
        player.move(0, -player_step)
    if keys[pygame.K_DOWN]:
        player.move(0, player_step)

def keyboard_dispatcher(event):
    if event.key == pygame.K_SPACE:
        player.jump()
    if event.key == pygame.K_s:
        Arrow(player)
    # if event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE:
    #     player.jump(player_h, jump_m)
    # if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE:
    #     player.jump(-player_h, jump_m)


def mouse_dispatcher(event):
    global player
    if event.button == 1:
        if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
            Stair(event.pos[0] - stair_w // 2, event.pos[1] - stair_h // 2)
        elif player is None:
            player = Player(event.pos[0] - player_step, event.pos[1] - player_step)
        else:
            player.setPos(event.pos)
    if event.button == 3:
        Platform(event.pos[0] - platform_w // 2, event.pos[1] - platform_h // 2)


def load_level(filename):
    filename = "data/maps/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_level(level):
    global player
    Fone()
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Platform(x * side, y * side)
            elif level[y][x] == '@':
                 player = Player(x * side, y * side)
            elif level[y][x] == 'L':
                Stair(x * side, y * side)
            elif level[y][x] == 'E':
                Enemy(x * side, y * side)
            elif level[y][x] == 'B':
                Block(x * side, y * side)


if __name__ == '__main__':
    level_map = load_level("Level1.txt")
    #size = width, height = len(level_map[0]) * side, len(level_map) * side
    print(size)
    #update_size(len(level_map[0]), len(level_map))
    print(size)
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    camera = Camera()
    player = None
    generate_level(level_map)
    platforms_group.draw(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == LOSE_EVENT:
                pygame.time.set_timer(LOSE_EVENT, 0)
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_dispatcher(event)
            if event.type == pygame.KEYDOWN:
                keyboard_dispatcher(event)

        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        keyboard_move_dispatcher(pygame.key.get_pressed())
        screen.fill(pygame.Color(screen_color))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
