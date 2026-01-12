import pygame
import spritePro as s 
from walk import *
from hero import Player

GAME_ACTIVE = 0
GAME_WIN = 1
GAME_LOSE = 2
GAME_MENU = 3

game_state = GAME_ACTIVE

s.init()
SCREEN = s.get_screen((1000, 700), 'Ходилка', 'Images/start_fon.webp')

player = Player((500, 350))

running = True
while running:
    if game_state == GAME_ACTIVE:
        player.update()

    