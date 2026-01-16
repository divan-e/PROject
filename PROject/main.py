import pygame
import spritePro as s 
from hero import Player
import wall
from enemy import Typoi

s.init()

GAME_ACTIVE = 0
GAME_WIN = 1
GAME_LOSE = 2
GAME_MENU = 3
game_state = GAME_ACTIVE

SCREEN = s.get_screen((1000, 700), 'PROject Aisek', 'Images/sfera.png')

background = s.Sprite('Images/start_fon.webp', (1000, 700), (500, 350))
player = Player()
walls = [
        wall.Wall((0, 0), (150, 700)),
        wall.Wall((0, 0), (450, 150)),
        wall.Wall((550, 0), (400, 150)),
        wall.Wall((850, 0), (150, 300)),
        wall.Wall((850, 400), (150, 300)),
        wall.Wall((0, 550), (450, 150)),
        wall.Wall((550, 550), (400, 150)),
    ]
player.set_collision_targets(walls)
vrag = Typoi((400, 400), (75, 70))

health = 3

running = True
while running:

    if health <= 0:
        running = False

    for event in s.events:
        if event.type == pygame.KEYDOWN:
            player.handle_keyboard_input()
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    vrag.move_towards((player.get_position()), vrag.speed)

    s.update()
            