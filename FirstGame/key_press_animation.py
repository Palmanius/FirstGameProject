import pygame
from player import Player

def key_press(player):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
        player.animate()

    else:
        player.stop_animating()