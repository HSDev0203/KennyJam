import pygame

import player

class Hud:
    def __init__(player, screen):
        player = player
        screen = screen
    
    heart_position = (10, 10)
    heart_image_full = pygame.image.load("hud_heart/hud_heart.png")
    heart_image_empty = pygame.image.load("hud_heart/hud_heart_empty.png")

    def draw():
        if Hud.player.health == 3:
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0], Hud.heart_position[1])
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0] + 10,Hud.heart_position[1])
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0] + 20,Hud.heart_position[1])
        if Hud.player.health == 3:
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0], Hud.heart_position[1])
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0] + 10,Hud.heart_position[1])
            Hud.screen.blit(Hud.heart_image_full, Hud.heart_position[0] + 20,Hud.heart_position[1])   