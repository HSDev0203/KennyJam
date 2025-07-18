import pygame

import player

class Hud:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
    
    heart_position = (10, 10)
    heart_image_full = pygame.image.load("hud_heart/hud_heart.png")
    heart_image_empty = pygame.image.load("hud_heart/hud_heart_empty.png")

    def draw(self):
        if self.player.health == 3:
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0] + 100,Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0] + 200,Hud.heart_position[1]))
        if self.player.health == 2:
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0] + 100,Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0] + 200,Hud.heart_position[1]))  
        if self.player.health == 1:
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0] + 100,Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_full, (Hud.heart_position[0] + 200,Hud.heart_position[1]))
        if self.player.health == 0:
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0] + 100,Hud.heart_position[1]))
            self.screen.blit(Hud.heart_image_empty, (Hud.heart_position[0] + 200,Hud.heart_position[1]))
        