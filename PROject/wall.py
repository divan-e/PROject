import pygame
import spritePro as s
from spritePro import Sprite

class Wall(Sprite):
    def __init__(self, pos, size ):
        super().__init__(
            pygame.Surface(size),
            size = size,
            pos = pos,
            speed = 0,
            anchor= s.Anchor.TOP_LEFT
        )
        self.image.fill((0,0,0,0))
    
    def update(self, screen = None):
        pass

        




















# Система коллизий SpritePro предоставляет автоматическое разрешение столкновений:

# Установить цели для столкновений
# obstacles = [wall1, wall2, wall3] sprite.set_collision_targets(obstacles)

# Добавить одну цель
# sprite.add_collision_target(wall4)

# Добавить несколько целей
# sprite.add_collision_targets([wall5, wall6])

# Удалить цель
# sprite.remove_collision_target(wall1)

# Удалить несколько целей
# sprite.remove_collision_targets([wall2, wall3])

# Очистить все цели
# sprite.clear_collision_targets()

