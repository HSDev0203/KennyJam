import time
import pygame
from bullet import Bullet

from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, hurt_group, holding_bullet, player_bullets_group, all_sprites_group):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))  # Green
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.health = 3
        self.speed = 5
        self.hurt_group = hurt_group
        self.enemy_wave = 1

        self.last_hit = 0 
        self.invinsibility_time = 1500
        self.last_dash = 0
        self.dash_delay = 500
        self.is_dashing = False
        self.direction = pygame.Vector2(0, 0)

        self.grab_rad = 90
        self.holding_bullet = holding_bullet
        self.player_bullets_group = player_bullets_group
        self.all_sprites_group = all_sprites_group

    def update(self, keys):
        now = pygame.time.get_ticks()
        if now - self.last_dash >= self.dash_delay:
            cooldown = True
        else:
            cooldown = False

        if not self.is_dashing:
            self.direction = pygame.Vector2(0, 0)

            if keys[pygame.K_w] and self.pos.y > 0: self.direction.y = -1
            if keys[pygame.K_s] and self.pos.y < 800: self.direction.y = 1
            if keys[pygame.K_a] and self.pos.x > 0 : self.direction.x = -1
            if keys[pygame.K_d] and self.pos.x < 800: self.direction.x = 1

        
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and cooldown: 
            dx = pygame.mouse.get_pos()[0] - self.pos.x
            dy = pygame.mouse.get_pos()[1] - self.pos.y
            self.direction.x = dx / ((dx**2 + dy**2)**0.5)
            self.direction.y = dy / ((dx**2 + dy**2)**0.5)
            self.speed = 20
            self.is_dashing = True
            self.last_dash = pygame.time.get_ticks()
        if self.speed > 5:
            self.speed -= 1
        else: 
            self.is_dashing = False

        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()
            self.pos += self.direction * self.speed
            self.rect.center = self.pos
        # Check collision between player and enemies
        hits_enemy = pygame.sprite.spritecollide(self,self.hurt_group, False)

        if hits_enemy and self.health > 0 and now - self.last_hit > self.invinsibility_time:
            self.health -= 1  # Apply damage
            self.last_hit = pygame.time.get_ticks()
        for sprite in self.hurt_group:
            hits_bullet = pygame.sprite.spritecollide(self, sprite.enemy_bullets, True)
            
            if hits_bullet and self.health > 0 and now - self.last_hit > self.invinsibility_time:
                self.health -= 1  # Apply damage
                self.last_hit = pygame.time.get_ticks()


    def redirect(self):
        # 1. Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # 2. Calculate direction vector from player to mouse
        direction = pygame.Vector2(mouse_pos) - self.pos
        if direction.length_squared() == 0:
            direction = pygame.Vector2(1, 0)  # Prevent zero-length vector
        direction = direction.normalize()
        
        # 3. Create new bullet moving in that direction
        bullet_speed = 6
        bullet = Bullet(self.pos, direction * bullet_speed)  # Pass screen bounds
        
        # 4. Add to sprite groups
        self.player_bullets_group.add(bullet)
        self.all_sprites_group.add(bullet)



    

