import pygame
from sys import exit

from enemy import Enemy
from player import Player
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Power Redirect")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player((400, 300))
enemy_bullets = pygame.sprite.Group()
enemy = Enemy((100, 100), player, 'ranged', enemy_bullets)
all_sprites.add(player, enemy)


running = True
while running:
    dt = clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update(keys)
    enemy.update()
    enemy_bullets.update()

    # Collision detection (basic bounding box for now)
    if pygame.sprite.collide_rect(player, enemy):
        print("Collision!")

    # Draw
    screen.fill("white")
    all_sprites.draw(screen)
    enemy_bullets.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()
