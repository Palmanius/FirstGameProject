import pygame,os
vel=5
def controls(player):
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.pos_y > 0:
        player.pos_y -= vel
    elif keys[pygame.K_s] and 450 > player.pos_y:
        player.pos_y += vel
    if keys[pygame.K_a] and player.pos_x > 0:
        player.pos_x -= vel
    elif keys[pygame.K_d] and 850 > player.pos_x:
        player.pos_x += vel
    