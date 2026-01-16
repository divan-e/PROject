from spritePro import Sprite
import spritePro as s
import walk


class Typoi(Sprite):
    def __init__(self, pos, size):
        super().__init__(
            sprite='Images/monster_stop.png',
            pos=pos,
            size=size,
            speed=1.7,
        )
        self.auto_flip = True

        self.walk_right_m = [img.convert_alpha() for img in walk.walk_right_m]
        self.walk_left_m = [img.convert_alpha() for img in walk.walk_left_m]
        self.walk_stop_m_r = walk.walk_stop_m_r.convert_alpha()
        self.walk_stop_m_l = walk.walk_stop_m_l.convert_alpha()

        self.animation = {
                'run_right' : [img.convert_alpha() for img in walk.walk_right_m],
                'run_left' : [img.convert_alpha() for img in walk.walk_left_m],
                'stand_r' : walk.walk_stop_m_r.convert_alpha(),
                'stand_l' : walk.walk_stop_m_l.convert_alpha()
            }
        
        self.state = 'stand_r'

        self.anim_kadr = 0
        self.anim_timer = 0
        self.anim_speed = 0.25

        self.last_anim = 'stand_r'

        self.image = self.walk_stop_m_r

        self.sprite_sheets = len(walk.walk_right_m) 



    def update(self, dt):
        self.velocity_x = self.velocity.x
        self.velocity_y = self.velocity.y

        if self.velocity_x > 0:
            self.state = 'run_right'
            self.last_anim = 'stand_r'
        elif self.velocity_x < 0:
            self.state = 'run_left'
            self.last_anim = 'stand_l'
       

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
                    self.image = walk.walk_right_m[self.anim_kadr]
                else:
                    self.image = walk.walk_left_m[self.anim_kadr]
                
        else:
            self.anim_timer = 0
            if self.last_anim == 'stand_r':
                self.image = walk.walk_stop_m_r
            else:
                self.image = walk.walk_stop_m_l

# self.animation = {
#                 'run_right' : [img.convert_alpha() for img in walk.walk_right_m],
#                 'run_left' : [img.convert_alpha() for img in walk.walk_left_m],
#                 'stand_r' : walk.walk_stop_m_r.convert_alpha(),
#                 'stand_l' : walk.walk_stop_m_l.convert_alpha()
#             }
        
#         self.state = 'stand_r'

#         self.anim_kadr = 0
#         self.anim_timer = 0
#         self.anim_speed = 0.25

#         self.last_anim = 'r'
        


   

        # if self.enemy.rect.colliderect(self.player.rect):
    