import pygame

class DialogueManager:
    def __init__(self, screen):
        
        self.screen = screen
        self.introDiologues = ["Welcome to Re-Direct! (press space to continue)", 
                                "In this game, you use your enemy's POWER against them...",
                                "When an enemy's BULLET is within your GRAB RADIUS,",
                                "Left click or press E."
                                "Then, draw a circle with your cursor to REDIRECT",
                                "their attack back at them!",
                                "Use WASD to move and press shift to DODGE",
                                "Have fun and good luck! (press space to start)"]
        self.runningDialogues = []


        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Font
        self.font = pygame.font.Font("Assets/fonts/EightBitDragon.ttf", 18)

        self.current_line = 0

        # Dialogue box dimensions
        self.dialogue_box = pygame.Rect(0, 600, 800, 200)

        self.running = True


    def update(self, skip_key):
        if self.running:
            if skip_key:
                self.current_line += 1
                if self.current_line >= len(self.runningDialogues):
                    self.running = False  # End dialogue

    def draw(self):
        if self.current_line < len(self.runningDialogues):

            pygame.draw.rect(self.screen, self.WHITE, self.dialogue_box)
            pygame.draw.rect(self.screen, self.BLACK, self.dialogue_box.inflate(-4, -4))

            text_surface = self.font.render(self.runningDialogues[self.current_line], False, self.WHITE)
            self.screen.blit(text_surface, (self.dialogue_box.x + 20, self.dialogue_box.y + 40))

