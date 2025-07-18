import pygame
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, target, type, bullet_group):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.target = target
        self.type = type
        self.enemy_bullets = bullet_group

        if type == 'melee':
            self.speed = 2.5
        elif type == 'ranged':
            self.speed = 1

        self.last_shot = 0
        self.shoot_delay = 1000


    def update(self):
        direction = self.target.pos - self.pos
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos
        self.attack()
        

    def attack(self):
        if self.type == 'melee':
            print()
        elif self.type == 'ranged':
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shoot_delay:
                direction = self.target.pos - self.pos
                if direction.length_squared() > 0:
                    bullet = Bullet(self.pos, direction)
                    self.enemy_bullets.add(bullet)
                    self.last_shot = now
            
