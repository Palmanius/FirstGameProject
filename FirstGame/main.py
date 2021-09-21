import pygame
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Game")
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60


def redraw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.clock()
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        redraw_window()

    
    pygame.quit()

if __name__ == "__main__":
    main()