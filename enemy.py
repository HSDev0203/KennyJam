import pygame
from bullet import Bullet
import soundeffects
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, target, type, bullet_group, hurt_group):
        super().__init__()

        if type == 'melee':
            melee_1 = pygame.image.load("Assets/melee_1.png").convert_alpha()
            self.melee_1 = pygame.transform.scale(melee_1, (32, 32))
            self.image = self.melee_1
            self.speed = 2.5
        elif type == 'ranged':
            self.speed = 0.5
            ranged_1 = pygame.image.load("Assets/ranged_1.png").convert_alpha()
            ranged_1 = pygame.transform.scale(ranged_1, (64, 32))
            ranged_2 = pygame.image.load("Assets/ranged_2.png").convert_alpha()
            ranged_2 = pygame.transform.scale(ranged_2, (64, 32))
            self.ranged_walk = [ranged_1, ranged_2]
            self.ranged_index = 0
            self.image = ranged_1

            
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.target = target
        self.type = type
        self.destroyed = False
        self.enemy_bullets = bullet_group
        self.hurt_group = hurt_group

        self.last_shot = 0
        self.is_shooting = False
        self.shoot_delay = 1000
        self.shoot_frame_timer = 1


    def attack(self):
        if self.type == 'melee':
            self.is_shooting = False
        elif self.type == 'ranged':
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.shoot_delay:
                direction = self.target.pos - self.pos
                if direction.length_squared() > 0:
                    bullet = Bullet(self.pos, direction)
                    self.enemy_bullets.add(bullet)
                    self.last_shot = now
                    self.is_shooting = True
                    self.shoot_frame_timer = 0
                    soundeffects.attack_sounds[randint(0, len(soundeffects.attack_sounds) - 1)].play()


    def animation_state(self):
        if self.type == 'melee':
            self.image = self.melee_1
        elif self.type == 'ranged':
            if self.is_shooting and self.shoot_frame_timer < 1:
                self.shoot_frame_timer += 0.125
                self.image = pygame.image.load("Assets/ranged_3.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (64, 32))
            else:
                self.ranged_index += 0.05
                if self.ranged_index >= len(self.ranged_walk): 
                    self.ranged_index = 0
                self.image = self.ranged_walk[int(self.ranged_index)]
        else:
            self.image = self.ranged_walk[0]


    def update(self):
        self.animation_state()
        direction = self.target.pos - self.pos
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos
        if not self.destroyed:
            self.attack()
        
        hits = pygame.sprite.spritecollide(self, self.hurt_group, True)
        
        if hits:
            soundeffects.enemy_hurt_sound.play() 
            self.destroyed = True
            self.kill()
            
