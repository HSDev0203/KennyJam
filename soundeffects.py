import pygame

pygame.mixer.init()

attack_sounds = [pygame.mixer.Sound('Assets/sfx/shoot_1.wav'), 
                 pygame.mixer.Sound('Assets/sfx/shoot_2.wav')]
attack_sounds[0].set_volume(1.2)
attack_sounds[1].set_volume(0.5)

player_shoot_sound = pygame.mixer.Sound('Assets/sfx/player_shoot.wav')

enemy_hurt_sound = pygame.mixer.Sound('Assets/sfx/enemy_hurt.wav')

text_skip_sound = pygame.mixer.Sound('Assets/sfx/text_skip.wav')
text_skip_sound.set_volume(0.45)

player_hurt_sound = pygame.mixer.Sound('Assets/sfx/player_hurt.wav')

dash_sound = pygame.mixer.Sound('Assets/sfx/dash.wav')
dash_sound.set_volume(0.5)
