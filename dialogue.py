import pygame

class DialogueManager:
    def __init__(self, screen):
        
        self.screen = screen
        self.introDiologues = ["Hello Welcome to POWER", "I like neal"]
        self.runningDialogues = []


        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Font
        self.font = pygame.font.SysFont("arial", 24)

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

            pygame.draw.rect(self.screen, self.BLACK, self.dialogue_box)
            pygame.draw.rect(self.screen, self.WHITE, self.dialogue_box.inflate(-10, -10))

            text_surface = self.font.render(self.runningDialogues[self.current_line], True, self.BLACK)
            self.screen.blit(text_surface, (self.dialogue_box.x + 20, self.dialogue_box.y + 40))

