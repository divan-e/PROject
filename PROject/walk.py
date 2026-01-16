import pygame

def load_walk_right_p():
    return [
        pygame.transform.scale(
            pygame.image.load(f"SpriteSheet/dibil{i}.png"),  
            (80, 75)                                        
        )
        for i in range(1, 24)  
    ]

walk_right_p = load_walk_right_p()
walk_left_p = [pygame.transform.flip(img, True, False) for img in walk_right_p]

def load_walk_right_m():
    return [
        pygame.transform.scale(
            pygame.image.load(f"SpriteSheet_monster/monster_right{i}.png"),  
            (75, 70)                                        
        )
        for i in range(1, 10)  
    ]

walk_right_m = load_walk_right_m()
walk_left_m = [pygame.transform.flip(img, True, False) for img in walk_right_m]
walk_stop_m_r = pygame.image.load("Images/monster_stop.png")
walk_stop_m_l = pygame.transform.flip(walk_stop_m_r, True, False)