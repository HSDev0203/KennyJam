import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.target = target
        self.speed = 2

    def update(self):
        direction = self.target.pos - self.pos
        if direction.length_squared() > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos
