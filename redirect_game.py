import pygame
from sys import exit

from enemy import Enemy
from player import Player

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Power Redirect")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player((400, 300))
enemy = Enemy((100, 100), player)
all_sprites.add(player, enemy)


while running:
    dt = clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update(keys)
    enemy.update()

    # Collision detection (basic bounding box for now)
    if pygame.sprite.collide_rect(player, enemy):
        print("Collision!")

    # Draw
    screen.fill("white")
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()
