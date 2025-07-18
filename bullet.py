import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, speed=5):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (5, 5), 5)
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.Vector2(pos)
        self.velocity = direction.normalize() * speed
    
    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos