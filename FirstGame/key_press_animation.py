import pygame
from player import Player

def key_press(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.animate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.stop_animating()

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.animate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player.stop_animating()

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.animate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.stop_animating()

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.animate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.stop_animating()