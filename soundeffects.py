import pygame

pygame.mixer.init()

attack_sounds = [pygame.mixer.Sound('Assets/sfx/shoot.wav'), pygame.mixer.Sound('Assets/sfx/shoot_2.wav'), pygame.mixer.Sound('Assets/sfx/shoot_3.wav')]
enemy_hurt_sound = pygame.mixer.Sound('Assets/sfx/hitHurt.wav')
text_skip_sound = pygame.mixer.Sound('Assets/sfx/text.wav')
player_hurt_sound = pygame.mixer.Sound('Assets/sfx/player_hurt.wav')
dash_sound = pygame.mixer.Sound('Assets/sfx/dash.wav')
game_loss_sound = pygame.mixer.Sound('Assets/sfx/wilhelm_scream.wav')
