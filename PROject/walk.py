import pygame
import spritePro as s


background = s.Sprite('Images/background_forest.jpg', (1000, 700))
enemy = s.Sprite('Images/ghost.png', (130, 130))

def load_walk_right():
    return[
    pygame.image.load(f'SpriteSheet/dibil{i}.png').convert_alpha
    for i in range(1,25)
    ]

walk_right = load_walk_right()
