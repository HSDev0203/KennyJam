import pygame

import player

class Hud:
    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
    
    heart_position = (32, 32)
    heart_full = pygame.image.load("hud_heart/hud_heart.png")
    heart_full = pygame.transform.scale(heart_full, (32, 32))
    heart_empty = pygame.image.load("hud_heart/hud_heart_empty.png")
    heart_empty = pygame.transform.scale(heart_empty, (32, 32))

    def draw(self):
        if self.player.health == 3:
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0] + 64, Hud.heart_position[1]))
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0] + 128, Hud.heart_position[1]))
        if self.player.health == 2:
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0] + 64, Hud.heart_position[1]))
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0] + 128, Hud.heart_position[1]))  
        if self.player.health == 1:
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0] + 64, Hud.heart_position[1]))
            self.screen.blit(Hud.heart_full, (Hud.heart_position[0] + 128, Hud.heart_position[1]))
        if self.player.health == 0:
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0], Hud.heart_position[1]))
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0] + 64, Hud.heart_position[1]))
            self.screen.blit(Hud.heart_empty, (Hud.heart_position[0] + 128, Hud.heart_position[1]))
        