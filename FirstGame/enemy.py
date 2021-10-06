import pygame,os

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.size = 25
        self.healt = health
        self.ship_img = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=health)
        self.sprites = []
        self.current_sprite = 0
        self.animation_speed = 0.05
        self.is_animating = True
        ship_img = pygame.image.load(os.path.join("FirstGame","Assets","Enemyship_(anim1).png"))
        ship_img = pygame.transform.scale(ship_img, (self.size, self.size))
        ship_img = pygame.transform.rotate(ship_img, 90)
        self.sprites.append(ship_img)
        ship_img = pygame.image.load(os.path.join("FirstGame","Assets","Enemyship_(anim2).png"))
        ship_img = pygame.transform.scale(ship_img, (self.size, self.size))
        ship_img = pygame.transform.rotate(ship_img, 90)
        self.sprites.append(ship_img)
        self.ship_img = ship_img
        self.mask = pygame.mask.from_surface(self.ship_img)

    def update(self):
        if self.is_animating == True:
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.ship_img = self.sprites[int(self.current_sprite)]
        else:
            self.ship_img = self.sprites[0]

    def move(self, vel):
        self.x -= vel
      

