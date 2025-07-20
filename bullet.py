import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, size=5, speed=5, grabbable=False, owner='enemy'):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)

        # Color by owner
        if owner == 'enemy':
            color =(0, 0, 255)
        else:
            color = (0, 255, 0)
        self.size = size
        pygame.draw.circle(self.image, color, (5, 5), self.size)
        
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.velocity = direction.normalize() * speed
        self.grabbable = grabbable
        self.owner = owner  # 'enemy' or 'player'

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

        # Kill if off screen (assuming 800x800 window)
        if (self.pos.x < 0 or self.pos.x > 800 or
            self.pos.y < 0 or self.pos.y > 800):
            self.kill()