# Game Settings
size = [800, 600]
fps = 60
alpha = 32
side = 20
mini_side = 3

def update_size(count_w, count_h):
    global size
    size[0], size[1] = count_w * side, count_h * side
# Game objects

gravity = 15

# Player Settings
player_h, player_w = side, side
player_step = 5
player_jump_speed = -7
jump_m = 50

# Enemy
enemy_speed = 100
enemy_h, enemy_w = side, side
enemy_hp = 300

# Stuff Settings
platform_h, platform_w = side, side
stair_h, stair_w = side, side
block_h, block_w = side, side
arrow_h, arrow_w = mini_side, mini_side
arrow_speed = 200

# Colors
stair_color = 'red'
screen_color = 'black'
platform_color = 'grey'
player_color = 'blue'
enemy_color = 'yellow'
arrow_color = 'green'

#The_Event
