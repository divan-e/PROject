import spritePro as s
from spritePro import Sprite
import walk
import pygame

player_x = 200
player_y = 420
player_aim_count = 0

class Player(Sprite):
    def __init__(self, pos):
        super().__init__(
            walk.walk_right[7], 
            (181, 174),
            (player_x, player_y),
            pos,                         
            5
        )

        self.auto_flip = True
        self.animations = {
            'stand': walk.walk_right[7], 
            'run': walk.walk_right,          
        }
        self.state = 'stand'
        self.anim_kadr = 0
        


    def update(self):
        self.handle_keyboard_input(
            left_key=pygame.K_a,
            right_key=pygame.K_d
        )

        if self.velocity.x != 0:
            self.state = "run"
        else:
            self.state = "idle"

        super().update()

    
    def update_anim(self):
        if player_aim_count == 23:
            player_aim_count = 0
        else:
            player_aim_count += 1

class Player(Sprite):
    def __init__(self, pos):
        super().__init__(
            walk.walk_right[0],
            (181, 174),
            pos,
            5
        )

        self.auto_flip = True

        self.animations = {
            "stand": [walk.walk_right[7]],
            "run": walk.walk_right
        }

        self.state = "stand"
        self.anim_kadr = 0

    def update(self):
        self.handle_keyboard_input(
            left_key=pygame.K_a,
            right_key=pygame.K_d
        )

        if self.velocity.x != 0:
            self.state = "run"
        else:
            self.state = "stand"

        self.update_anim()
        super().update()

    def update_anim(self):
        frames = self.animations[self.state]

        if self.anim_kadr == len(frames) - 1:
            self.anim_kadr = 0
        else:
            self.anim_kadr += 1

        self.set_image(frames[self.anim_kadr])