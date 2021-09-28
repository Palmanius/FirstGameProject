import pygame, sys
from player import Player


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

def redraw_window():
    WIN.fill(WHITE)
    moving_sprites.draw(WIN)
    moving_sprites.update()
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.animate()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.stop_animating()
        redraw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
