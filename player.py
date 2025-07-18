import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))  # Green
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.speed = 5

        self.last_dash = 0
        self.dash_delay = 500
        self.is_dashing = False
        self.direction = pygame.Vector2(0, 0)

    def update(self, keys):
        now = pygame.time.get_ticks()
        if now - self.last_dash >= self.dash_delay:
            cooldown = True
        else:
            cooldown = False

        if not self.is_dashing:
            self.direction = pygame.Vector2(0, 0)
            if keys[pygame.K_w]: self.direction.y = -1
            if keys[pygame.K_s]: self.direction.y = 1
            if keys[pygame.K_a]: self.direction.x = -1
            if keys[pygame.K_d]: self.direction.x = 1

        
        if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and cooldown: 
            dx = pygame.mouse.get_pos()[0] - self.pos.x
            dy = pygame.mouse.get_pos()[1] - self.pos.y
            self.direction.x = dx / ((dx**2 + dy**2)**0.5)
            self.direction.y = dy / ((dx**2 + dy**2)**0.5)
            self.speed = 20
            self.is_dashing = True
            self.last_dash = pygame.time.get_ticks()
        if self.speed > 5:
            self.speed -= 1
        else: 
            self.is_dashing = False

        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()
            self.pos += self.direction * self.speed
            self.rect.center = self.pos

    

