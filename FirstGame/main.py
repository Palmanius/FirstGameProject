import pygame, random
from controlls import *
from player import Player
from enemy import *
from asteroids import *
from key_press_animation import *


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

bkgd = pygame.image.load(os.path.join("FirstGame","Assets","Background.png")).convert()
x = 0

enemy_vel = 1
level = 0
enemy_wave = 5
enemies = []

asts_vel = 1
asts_wave = 5
asts = []


player = Player(100,100)


def redraw_window():

    #WIN.fill(WHITE)
    for enemy in enemies:
        enemy.update()
        enemy.draw(WIN)

    for ast in asts:
        ast.update()
        ast.draw(WIN)

    player.draw(WIN)
    player.update()

    pygame.display.update()



def main():#

    global enemy_vel, level, enemies, enemy_wave, asts_vel, asts_wave, asts, x

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            enemy_wave += 5
            for i in range(enemy_wave):
                enemy = Enemy(random.randrange(WIDTH, WIDTH+1500), random.randrange(25,HEIGHT-25))
                enemies.append(enemy)
                ast = Asteroid(random.randrange(WIDTH, WIDTH+1500), random.randrange(25,HEIGHT-25))
                asts.append(ast)

        # Background scrolling

        rel_x = x % bkgd.get_rect().width
        WIN.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))

        if rel_x < WIDTH:
            WIN.blit(bkgd, (rel_x, 0))


        key_press(player)

        x -= 1

        controls(player)
        
        for enemy in enemies:
            enemy.move(enemy_vel)
        redraw_window()
        for ast in asts:
            ast.move(asts_vel)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()   

    
if __name__ == "__main__":
    main()
