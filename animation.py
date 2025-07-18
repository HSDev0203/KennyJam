import pygame

class Animator:
    def __init__(self, screen, spriteSheet, x, y, framerate = 60, looping = False):
        self.x = x
        self.y = y
        self.screen = screen
        self.looping = looping
        self.framerate = framerate
        self.spriteSheet = spriteSheet
        self.imageIndex = 0
        self.currentImage = spriteSheet[self.imageIndex]
        self.run = True
        self.current_frame = 0
        self.clock = pygame.time.Clock()

    def play(self):
        self.current_frame += 1
        if self.run and self.current_frame % self.framerate == 0:
            self.current_frame = 0
            if self.imageIndex >= len(self.spriteSheet):
                self.imageIndex = 0

            self.currentImage = self.spriteSheet[self.imageIndex]

            self.imageIndex += 1
        
        if self.run:
            self.screen.blit(self.currentImage, (self.x, self.y))



