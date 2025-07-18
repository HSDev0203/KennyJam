import pygame

class Animator:
    def __init__(self, screen, spriteSheet, parent, framerate = 60, looping = False):
        self.parent = parent
        self.pos = parent.pos
        self.screen = screen
        self.looping = looping
        self.framerate = framerate
        self.spriteSheet = spriteSheet
        self.imageIndex = 0
        self.currentImage = spriteSheet[self.imageIndex]
        self.rect = self.currentImage.get_rect(center=self.parent.pos)
        self.run = True
        self.current_frame = 0
        self.clock = pygame.time.Clock()

    def play(self):
        self.pos = self.parent.pos
        self.current_frame += 1
        if self.run and self.current_frame % self.framerate == 0:
            self.current_frame = 0
            if self.imageIndex >= len(self.spriteSheet):
                self.imageIndex = 0

            self.currentImage = self.spriteSheet[self.imageIndex]

            self.imageIndex += 1
        
        if self.run:
            self.rect = self.currentImage.get_rect(center=self.parent.pos)
            self.screen.blit(self.currentImage, self.rect.topleft) 



