import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, size=4, speed=5, grabbable=False, owner='enemy'):
        super().__init__()

        bullet_1 = pygame.image.load("Assets/bullet_1.png")
        bullet_1 = pygame.transform.scale(bullet_1, (12, 12))
        bullet_2 = pygame.image.load("Assets/bullet_2.png")
        bullet_2 = pygame.transform.scale(bullet_2, (12, 12))
        self.bullet_sprites = [bullet_1, bullet_2]
        self.bullet_index = 0

        self.image = self.bullet_sprites[self.bullet_index]
        self.rect = self.image.get_rect(center=pos)
        self.spritesheet = None
        self.animation = None
        self.size = size * 4
        self.pos = pygame.Vector2(pos)
        self.velocity = direction.normalize() * speed
        self.grabbable = grabbable
        self.owner = owner  # 'enemy' or 'player'

        '''
        if owner == 'enemy':
            color =(255, 0, 77)
        else:
            color = (41, 173, 255)
        pygame.draw.rect(self.image, color, (0, 0, self.size, self.size))
        
        self.animation = Animator(self.image, self.spritesheet, self, 10)
        '''

    def animation_state(self):
        self.bullet_index += 0.1
        if self.bullet_index >= len(self.bullet_sprites): 
            self.bullet_index = 0
        self.image = self.bullet_sprites[int(self.bullet_index)]

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        self.animation_state()

        # Kill if off screen (assuming 800x800 window)
        if (self.pos.x < 0 or self.pos.x > 800 or
            self.pos.y < 0 or self.pos.y > 800):
            self.kill()