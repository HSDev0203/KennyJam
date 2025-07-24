import time
import pygame
from bullet import Bullet
import soundeffects
from utilities import is_circle
from utilities import calculate_circularity
from utilities import circularity_to_accuracy
import soundeffects
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, hurt_group, holding_bullet, player_bullets_group, all_sprites_group, enemy_group):
        super().__init__()

        player_front_1 = pygame.image.load("Assets/player_front_1.png")
        player_front_1 = pygame.transform.scale(player_front_1, (32, 32))
        player_front_2 = pygame.image.load("Assets/player_front_2.png")
        player_front_2 = pygame.transform.scale(player_front_2, (32, 32))
        self.player_front_spritesheet = [player_front_1, player_front_2]
        player_right_1 = pygame.image.load("Assets/player_side_1.png")
        player_right_1 = pygame.transform.scale(player_right_1, (32, 32))
        player_right_2 = pygame.image.load("Assets/player_side_2.png")
        player_right_2 = pygame.transform.scale(player_right_2, (32, 32))
        self.player_right_spritesheet = [player_right_1, player_right_2]
        player_left_1 = pygame.transform.flip(player_right_1, True, False)
        player_left_2 = pygame.transform.flip(player_right_2, True, False)
        self.player_left_spritesheet = [player_left_1, player_left_2]
        self.player_index = 0

        self.image = player_front_1
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.health = 3
        self.speed = 5
        self.hurt_group = hurt_group
        self.enemy_wave = 1

        # Invinsibility
        self.last_hit = 0 
        self.invinsibility_time = 1500

        # Movement Related
        self.last_dash = 0
        self.dash_delay = 500
        self.is_dashing = False
        self.direction = pygame.Vector2(0, 0)

        # Redirecting Bullets
        self.grab_rad = 90
        self.holding_bullet = holding_bullet
        self.player_bullets_group = player_bullets_group
        self.all_sprites_group = all_sprites_group
        self.enemy_group = enemy_group

        # Drawing Paths
        self.mouse_path = []       # List of (x, y) points
        self.max_path_length = 100  # Only keep the last 100 positions
        self.circle_completed = False

    def animation_state(self, keys):
        if keys[pygame.K_d]:
            player_spritesheet = self.player_right_spritesheet
        elif keys[pygame.K_a]:
            player_spritesheet = self.player_left_spritesheet
        else:
            player_spritesheet = self.player_front_spritesheet

        self.player_index += 0.025
        if self.player_index >= len(player_spritesheet): 
            self.player_index = 0
        self.image = player_spritesheet[int(self.player_index)]

    def update(self, keys):
        self.animation_state(keys)

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
            # dx = pygame.mouse.get_pos()[0] - self.pos.x
            # dy = pygame.mouse.get_pos()[1] - self.pos.y
            # self.direction.x = dx / ((dx**2 + dy**2)**0.5)
            # self.direction.y = dy / ((dx**2 + dy**2)**0.5)
            self.speed = 20
            self.is_dashing = True
            self.last_dash = pygame.time.get_ticks()
            if abs(self.direction.x) > 0 or abs(self.direction.y) > 0:
                soundeffects.dash_sound.play()

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
            soundeffects.player_hurt_sound.play()
        for sprite in self.hurt_group:
            hits_bullet = pygame.sprite.spritecollide(self, sprite.enemy_bullets, True)
            if hits_bullet and self.health > 0 and now - self.last_hit > self.invinsibility_time:
                self.health -= 1  # Apply damage
                self.last_hit = pygame.time.get_ticks()
                soundeffects.player_hurt_sound.play()
        
        if self.holding_bullet:
            self.mouse_path.append(pygame.mouse.get_pos())
            if len(self.mouse_path) > self.max_path_length:
                self.mouse_path.pop(0)
            if not self.circle_completed:
                if is_circle(self.mouse_path):
                    print("Circle complete!")
                    self.circle_completed = True

    def get_nearest_enemy(self):
        nearest = None
        min_distance = float('inf')

        for enemy in self.enemy_group:
            dist = self.pos.distance_to(enemy.pos)
            if dist < min_distance:
                nearest = enemy
                min_distance = dist
        
        return nearest

    
    def redirect(self):
        if not self.circle_completed:
            print("You must complete the circle before redirecting!")
            return
        
        '''
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        # Calculate direction vector from player to mouse
        direction = pygame.Vector2(mouse_pos) - self.pos
        if direction.length_squared() == 0:
            direction = pygame.Vector2(1, 0)  # Prevent zero-length vector
        direction = direction.normalize()
        '''

        nearest = self.get_nearest_enemy()
        if nearest:
            direction = nearest.pos - self.pos
        else:
            print("No enemies found — firing straight!")
            direction = pygame.Vector2(1, 0)
        
        # Create new bullet moving in that direction with speed based on circle accuracy
        circle_score = calculate_circularity(self.mouse_path)
        accuracy = circularity_to_accuracy(circle_score)
        min_speed = 2
        max_speed = 8
        bullet_speed = min_speed + (accuracy) * (max_speed - min_speed)
        min_size = 1
        max_size = 6
        bullet_size = int(min_size + (accuracy) * (max_size - min_size))

        bullet = Bullet(self.pos, direction, bullet_size, bullet_speed, grabbable=False, owner='player')
        
        # Add to sprite groups
        self.player_bullets_group.add(bullet)
        self.all_sprites_group.add(bullet)
        soundeffects.attack_sounds[randint(0, len(soundeffects.attack_sounds) - 1)].play()




    

