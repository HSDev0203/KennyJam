from tkinter import dialog
from tkinter.filedialog import dialogstates
from numpy import append
import pygame
from sys import exit

from player import Player
from dialogue import DialogueManager
from hud import Hud
from gameManager import GameManager
import soundeffects

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Power Redirect")
clock = pygame.time.Clock()
intro = True

ground_tile = pygame.image.load("Assets/ground_tile.png")
ground_tile = pygame.transform.scale(ground_tile, (32, 32))

grab_indicator_outline = pygame.image.load("Assets/grab_indicator_outline.png")
grab_indicator_outline = pygame.transform.scale(grab_indicator_outline, (160, 160))
grab_indicator_1 = pygame.image.load("Assets/grab_indicator_1.png")
grab_indicator_1 = pygame.transform.scale(grab_indicator_1, (160, 160))
grab_indicator_2 = pygame.image.load("Assets/grab_indicator_2.png")
grab_indicator_2 = pygame.transform.scale(grab_indicator_2, (160, 160))

all_sprites = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
hurt_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player((400, 300), hurt_group, False, player_bullets, all_sprites, enemy_group=enemies)
all_sprites.add(player)
hurt_group.add(enemy_bullets)

hud = Hud(player, screen)
gameManager = GameManager(player, enemy_bullets, player_bullets, enemies, hurt_group)

dialogue_manager = DialogueManager(screen)
dialogue_manager.runningDialogues = dialogue_manager.introDiologues
dialog_key = False
game_over = False
loss_sound_toggle = True
score = 0

game_over_font = pygame.font.Font("Assets/fonts/P8.ttf", 75)
score_font = pygame.font.Font("Assets/fonts/P8.ttf", 20)

game_over_text_surface_1 = game_over_font.render("GAME OVER", True, 'White')
game_over_text_surface_2 = game_over_font.render("press r to restart", True, 'White')
score_text_surface = score_font.render(f"Score:{score}", False, (255, 255, 255))

game_over_text_surface_1_rect = game_over_text_surface_1.get_rect(center = (400,350))
game_over_text_surface_2_rect = game_over_text_surface_2.get_rect(center = (400,450))
score_text_rect = score_text_surface.get_rect(topright = (700, 32)) 

running = True
while running:
    score_text_surface = score_font.render(f"Score: {(score)}", False, (255, 255, 255))
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
                loss_sound_toggle = True

                all_sprites = pygame.sprite.Group()
                enemy_bullets = pygame.sprite.Group()
                player_bullets = pygame.sprite.Group()
                hurt_group = pygame.sprite.Group()
                enemies = pygame.sprite.Group()

                player = Player((400, 300), hurt_group, False, player_bullets, all_sprites, enemy_group=enemies)
                all_sprites.add(player)
                hurt_group.add(enemy_bullets)

                hud = Hud(player, screen)
                gameManager = GameManager(player, enemy_bullets, player_bullets, enemies, hurt_group)

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
        enemy_bullets.update()
        player_bullets.update()
        gameManager.update()
        enemies.update()
    
    dialogue_manager.update(dialog_key)
    
    if dialogue_manager.running != True:
        intro = False
    dialog_key = False
        
    if not player.holding_bullet:
        for projectile in enemy_bullets:
            if player.pos.distance_to(projectile.pos) < player.grab_rad:
                projectile.grabbable = True
                bul_in_rad = True


    # Draw
    screen.fill("white")
    for row in range(25):
        for col in range(25):
            x = col * 32
            y = row * 32
            screen.blit(ground_tile, (x, y))
            
    if player.holding_bullet:

        grab_indicator_2_rect = grab_indicator_2.get_rect(center = player.pos)
        screen.blit(grab_indicator_2, grab_indicator_2_rect)

        # Draw crosshair on nearest enemy
        try:
            if player.get_nearest_enemy().pos != None:
                pygame.draw.line(screen, 'White', (player.get_nearest_enemy().pos.x, 0), (player.get_nearest_enemy().pos.x, player.get_nearest_enemy().pos.y - 16), 2 )
                pygame.draw.line(screen, 'White', (player.get_nearest_enemy().pos.x, player.get_nearest_enemy().pos.y + 16), (player.get_nearest_enemy().pos.x, 800), 2 )
                pygame.draw.line(screen, 'White', (0, player.get_nearest_enemy().pos.y), (player.get_nearest_enemy().pos.x - 16, player.get_nearest_enemy().pos.y), 2 )
                pygame.draw.line(screen, 'White', (player.get_nearest_enemy().pos.x + 16, player.get_nearest_enemy().pos.y), (800, player.get_nearest_enemy().pos.y), 2 )
        except:
            print("tried to access unknown enemy")

    elif bul_in_rad:

        grab_indicator_1_rect = grab_indicator_1.get_rect(center = player.pos)
        screen.blit(grab_indicator_1, grab_indicator_1_rect)
    else:
        pass
    grab_indicator_outline_rect = grab_indicator_outline.get_rect(center = player.pos)
    screen.blit(grab_indicator_outline, grab_indicator_outline_rect)
    #grab_indicator_outline = pygame.draw.circle(screen, 'White', player.pos, 75, 2)
    all_sprites.draw(screen)
    enemies.draw(screen)
    enemy_bullets.draw(screen)
    dialogue_manager.draw()
    hud.draw()

    if player.holding_bullet and (len(player.mouse_path) > 1):
        pygame.draw.lines(screen, 'White', False, player.mouse_path, 5)

    red_overlay = pygame.Surface((800, 800), pygame.SRCALPHA)  # Use SRCALPHA for per-pixel alpha
    if game_over == True:

        if loss_sound_toggle:
            soundeffects.game_loss_sound.play()
        loss_sound_toggle = False
        
        red_overlay.fill((0, 0, 0, 175))  # RGBA (last value is alpha: 0=transparent, 255=opaque)
        screen.blit(red_overlay, (0, 0))

        screen.blit(game_over_text_surface_1, game_over_text_surface_1_rect)
        screen.blit(game_over_text_surface_2, game_over_text_surface_2_rect)

    screen.blit(score_text_surface, score_text_rect)
    pygame.display.flip()

pygame.quit()
exit()
