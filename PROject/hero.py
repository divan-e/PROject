from spritePro import Sprite
import walk
import pygame
 


player_aim_count = 0

'''
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
        self.anim_timer = 0
        self.anim_speed = 0.25


    def update(self):
        self.veloсity_1 = self.velocity.x
        self.velocity_2 = self.velocity.y

        self.handle_keyboard_input(
            left_key=pygame.K_a,
            right_key=pygame.K_d,
            up_key=pygame.K_w,
            down_key=pygame.K_s
        )

        if self.velocity.x != 0 or self.velocity.y != 0:
            self.state = "run"
        else:
            self.state = "stand"

        self.update_anim()

        super().update()

    
    def update_anim(self):
        if self.state == 'run':
            self.anim_timer += self.anim_speed
            if self.anim_timer >= 1:
                self.anim_timer = 0
                self.anim_kadr = (self.anim_kadr + 1) % 23

                self.image = walk.walk_right[self.anim_kadr]

        else:
            self.image = walk.walk_right[7]
            self.anim_timer = 0
'''
screen_width, screen_hidth = 1000, 700

class Player(Sprite):
    def __init__(self):
        super().__init__(walk.walk_right_p[7],
                        (80, 75), #181, 174
                        pos = (screen_width//2,screen_hidth //2),
                        speed = 5)
        
        self.auto_flip = True

        self.animation = {
            'run_right' : [img.convert_alpha() for img in walk.walk_right_p],
            'run_left' : [img.convert_alpha() for img in walk.walk_left_p],
            'stand_r' : walk.walk_right_p[7].convert_alpha(),
            'stand_l' : walk.walk_left_p[7].convert_alpha()
        }


        self.state = 'stand_r'

        self.anim_kadr = 0
        self.anim_timer = 0
        self.anim_speed = 0.5

        self.last_anim = 'r'


        self.sprite_sheets = len(walk.walk_right_p) 



    def update(self, dt):
        self.handle_keyboard_input(
            up_key = pygame.K_w,
            down_key = pygame.K_s,
            left_key = pygame.K_a,
            right_key = pygame.K_d
        )

        self.velocity_x = self.velocity.x
        self.velocity_y = self.velocity.y

        if self.velocity_x > 0:
            self.state = 'run_right'
            self.last_anim = 'r'
        elif self.velocity_x < 0:
            self.state = 'run_left'
            self.last_anim = 'l'
        else:
            if self.last_anim == 'r':
                self.state = 'stand_r'
            if self.last_anim == 'l':
                self.state = 'stand_l'

        self.update_anim()
        super().update(dt)



    def update_anim(self):

        self.all_sprite_sheet = self.sprite_sheets 

        if self.state == 'run_right' or self.state == 'run_left':
            self.anim_timer += self.anim_speed
            if self.anim_timer >= 1:
                self.anim_timer = 0
                self.anim_kadr = (self.anim_kadr + 1)  % self.sprite_sheets 
                if self.state == 'run_right':
                    self.image = walk.walk_right_p[self.anim_kadr]
                else:
                    self.image = walk.walk_left_p[self.anim_kadr]
                
        else:
            if self.state == 'stand_r':
                self.image = walk.walk_right_p[7]
            else:
                self.image = walk.walk_left_p[7]



        

        

            
"""            self.anim_timer = 0

            self.image = walk.walk_right[7]

"""

                


