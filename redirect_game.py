import pygame
from sys import exit

from enemy import Enemy
from player import Player
from dialogue import DialogueManager

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Power Redirect")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player((400, 300))
enemy = Enemy((100, 100), player)
all_sprites.add(player, enemy)

dialogue_manager = DialogueManager(screen)
dialogue_manager.runningDialogues = dialogue_manager.introDiologues

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
    dialogue_manager.update()


    # Collision detection (basic bounding box for now)
    if pygame.sprite.collide_rect(player, enemy):
        print("Collision!")

    # Draw
    screen.fill("white")
    all_sprites.draw(screen)
    dialogue_manager.draw()
    pygame.display.flip()

pygame.quit()
exit()
