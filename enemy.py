import pygame
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, target, type, bullet_group, hurt_group):
        super().__init__()

        if type == 'melee':
            self.image = pygame.image.load("Assets/tile_0115.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            self.speed = 2.5
        elif type == 'ranged':
            self.speed = 0.5
            self.image = pygame.image.load("Assets/tile_0114.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (32, 32))
            
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.target = target
        self.type = type
        self.destroyed = False
        self.enemy_bullets = bullet_group
        self.hurt_group = hurt_group

        self.last_shot = 0
        self.shoot_delay = 1000


    def update(self):
        
        direction = self.target.pos - self.pos
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos
        if not self.destroyed:
            self.attack()
        
        hits = pygame.sprite.spritecollide(self, self.hurt_group, True)
        
        if hits:
            self.destroyed = True
            self.kill()


        

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
            
