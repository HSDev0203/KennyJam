from tkinter import dialog
from tkinter.filedialog import dialogstates
from numpy import append
import pygame
from sys import exit

from animation import Animator
from enemy import Enemy
from bullet import Bullet
from player import Player
from dialogue import DialogueManager
from hud import Hud
from gameManager import GameManager

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Power Redirect")
clock = pygame.time.Clock()
intro = True

all_sprites = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
hurt_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player((400, 300), hurt_group, False, player_bullets, all_sprites, enemy_group=enemies)
enemy = Enemy((100, 100), player, 'ranged', enemy_bullets, player_bullets)
all_sprites.add(player, enemy)
hurt_group.add(enemy, enemy_bullets)

hud = Hud(player, screen)
gameManager = GameManager(player, enemy_bullets, player_bullets, enemies, hurt_group)

beeAnimation = [pygame.image.load("bee_animation/bee_a.png"), pygame.image.load("bee_animation/bee_b.png")]
bee = Animator(screen, beeAnimation, player, 10)

dialogue_manager = DialogueManager(screen)
dialogue_manager.runningDialogues = dialogue_manager.introDiologues
dialog_key = False
game_over = False
score = 0

game_over_font = pygame.font.Font("Assets/fonts/P8.ttf", 75)
score_font = pygame.font.Font("Assets/fonts/P8.ttf", 20)

game_over_text_surface_1 = game_over_font.render("GAME OVER", True, (0, 0, 0))
game_over_text_surface_2 = game_over_font.render("press r to restart", True, (0, 0, 0))
score_text_surface = score_font.render(f"Score:{score}", True, (0, 0, 0))

game_over_text_surface_1_rect = game_over_text_surface_1.get_rect(center = (400,350))
game_over_text_surface_2_rect = game_over_text_surface_2.get_rect(center = (400,450))
score_text_rect = score_text_surface.get_rect(topright = (700, 0)) 

running = True
while running:
    score_text_surface = score_font.render(f"Score: {(score)}", True, (0, 0, 0))
    dt = clock.tick(60)
    keys = pygame.key.get_pressed()
    bul_in_rad = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not player.holding_bullet:
            for projectile in enemy_bullets:
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_e) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    if projectile.grabbable:
                        projectile.kill()
                        player.holding_bullet = True
                        print('Holding a Bullet!')
        if (event.type == pygame.KEYUP and event.key == pygame.K_e) or (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
            if player.holding_bullet:
                player.redirect()
                player.holding_bullet = False
                player.circle_completed = False
                player.mouse_path.clear()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                dialog_key = True
            if(event.key == pygame.K_r):
                clock = pygame.time.Clock()
                intro = True
                score = 0

                all_sprites = pygame.sprite.Group()
                enemy_bullets = pygame.sprite.Group()
                player_bullets = pygame.sprite.Group()
                hurt_group = pygame.sprite.Group()
                enemies = pygame.sprite.Group()

                player = Player((400, 300), hurt_group, False, player_bullets, all_sprites, enemy_group=enemies)
                enemy = Enemy((100, 100), player, 'ranged', enemy_bullets, player_bullets)
                all_sprites.add(player, enemy)
                hurt_group.add(enemy, enemy_bullets)

                hud = Hud(player, screen)
                gameManager = GameManager(player, enemy_bullets, player_bullets, enemies, hurt_group)

                beeAnimation = [pygame.image.load("bee_animation/bee_a.png"), pygame.image.load("bee_animation/bee_b.png")]
                bee = Animator(screen, beeAnimation, player, 10)

                dialogue_manager = DialogueManager(screen)
                dialogue_manager.runningDialogues = dialogue_manager.introDiologues
                dialog_key = False
                game_over = False
            
            
    if(player.health <= 0):
        game_over = True

    # Update

    if intro == False and game_over == False:
        score += 1
        player.update(keys)
        enemy.update()
        enemy_bullets.update()
        player_bullets.update()
        gameManager.update()
        enemies.update()
    
    dialogue_manager.update(dialog_key)
    
    if dialogue_manager.running != True:
        intro = False
    dialog_key = False
    
    # Collision detection (basic bounding box for now)
    if pygame.sprite.collide_rect(player, enemy):
        print("Collision!")
        
    if not player.holding_bullet:
        for projectile in enemy_bullets:
            if player.pos.distance_to(projectile.pos) < player.grab_rad:
                projectile.grabbable = True
                bul_in_rad = True


    # Draw
    screen.fill("white")
    red_overlay = pygame.Surface((800, 800), pygame.SRCALPHA)  # Use SRCALPHA for per-pixel alpha
    
    if game_over == True:
        red_overlay.fill((255, 0, 0, 128))  # RGBA (last value is alpha: 0=transparent, 255=opaque)
        
        screen.blit(red_overlay, (0, 0))

            
    if player.holding_bullet:
        grab_indicator = pygame.draw.circle(screen, 'Red', player.pos, 75)
        if len(player.mouse_path) > 1:
            pygame.draw.lines(screen, 'Black', False, player.mouse_path, 5)
    elif bul_in_rad:
        grab_indicator = pygame.draw.circle(screen, 'Orange', player.pos, 75)
    else:
        grab_indicator = pygame.draw.circle(screen, 'White', player.pos, 75)
    grab_indicator_outline = pygame.draw.circle(screen, 'Black', player.pos, 75, 5)
    all_sprites.draw(screen)
    enemies.draw(screen)
    enemy_bullets.draw(screen)
    bee.play()
    dialogue_manager.draw()
    hud.draw()

    if game_over == True:

        screen.blit(game_over_text_surface_1, game_over_text_surface_1_rect)
        screen.blit(game_over_text_surface_2, game_over_text_surface_2_rect)

    screen.blit(score_text_surface, score_text_rect)
    pygame.display.flip()

pygame.quit()
exit()
