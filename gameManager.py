from re import S
import pygame
import enemy
import random 

class GameManager:
    def __init__(self, player, enemy_bullets, player_bullets, enemies, hurt_group):
        self.enemy_wave = 1
        self.enemy_bullets = enemy_bullets
        self.player_bullets = player_bullets
        self.player = player
        self.hurt_group = hurt_group
        self.spawn_positions = [pygame.Vector2(900, 400), pygame.Vector2(-100,400), 
                               pygame.Vector2(400, 900), pygame.Vector2(400, 900)]
        self.spawn_cooldown = 5000
        self.last_spawn = self.spawn_cooldown 
        self.enemies = enemies
        self.enemy_possibilities = ["melee", "ranged", "melee", "melee"]
    
    def selectEnemyType(self):
        choice = random.choices(
            population = ["melee", "ranged"],
            weights = [70, 40],
            k=1
        )[0]
        return choice 

    def update(self):
        elapsed_time = pygame.time.get_ticks()
        
        if elapsed_time - self.last_spawn >= self.spawn_cooldown:
            self.enemies.add(enemy.Enemy(self.spawn_positions[random.randint(0, 3)], self.player, self.selectEnemyType(), self.enemy_bullets, self.player_bullets))
            self.hurt_group.add(self.enemies)
            self.last_spawn = elapsed_time