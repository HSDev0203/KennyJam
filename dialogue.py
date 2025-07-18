import pygame

class DialogueManager:
    def __init__(self, screen):
        
        self.screen = screen
        self.introDiologues = ["Hello Welcome to POWER"]
        self.runningDialogues = []


        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Font
        self.font = pygame.font.SysFont("arial", 24)

        self.current_line = 0

        # Dialogue box dimensions
        self.dialogue_box = pygame.Rect(50, 450, 700, 125)

        self.running = True
    def update(self):
        if self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_line += 1
                        if current_line >= len():
                            self.running = False  # End dialogue

    def draw(self):
        pygame.draw.rect(self.screen, self.BLACK, self.dialogue_box)
        pygame.draw.rect(self.screen, self.WHITE, self.dialogue_box.inflate(-10, -10))

        if self.current_line < len(self.runningDialogues):
            text_surface = self.font.render(self.runningDialogues[self.current_line], True, self.BLACK)
            self.screen.blit(text_surface, (self.dialogue_box.x + 20, self.dialogue_box.y + 40))

