import pygame
from animation import Animator

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, size=4, speed=5, grabbable=False, owner='enemy'):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.spritesheet = None
        self.animation = None
        self.size = size * 4
        self.pos = pygame.Vector2(pos)
        self.velocity = direction.normalize() * speed
        self.grabbable = grabbable
        self.owner = owner  # 'enemy' or 'player'

        enem_bul_frame1 = pygame.image.load("Assets/tile_0095.png")
        enem_bul_frame1 = pygame.transform.scale(enem_bul_frame1, (32, 32))
        enem_bul_frame2 = pygame.image.load("Assets/tile_0096.png")
        enem_bul_frame2 = pygame.transform.scale(enem_bul_frame2, (32, 32))
        self.spritesheet = [enem_bul_frame1, enem_bul_frame2]
        
        if owner == 'enemy':
            color =(255, 0, 77)
        else:
            color = (41, 173, 255)
        pygame.draw.rect(self.image, color, (0, 0, self.size, self.size))
        
        self.animation = Animator(self.image, self.spritesheet, self, 10)


    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        self.animation = Animator(self.image, self.spritesheet, self, 10)

        # Kill if off screen (assuming 800x800 window)
        if (self.pos.x < 0 or self.pos.x > 800 or
            self.pos.y < 0 or self.pos.y > 800):
            self.kill()