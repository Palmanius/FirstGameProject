import pygame,os
def controls(player):
    keys = pygame.key.get_pressed()
    player.pos_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player.pos_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5