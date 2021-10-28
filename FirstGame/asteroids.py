import pygame,os,random

class Stat:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.size = random.randrange(1,10)
        self.healt = health
        self.ast_img = None
    def draw(self, window):
        window.blit(self.ast_img, (self.x, self.y))

class Asteroid(Stat):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=health)
        self.sprites = []
        self.current_sprite = 0
        self.animation_speed = 0.05
        self.is_animating = True
        ast_img = pygame.image.load(os.path.join("FirstGame","Assets","Asteroid_(anim1).png"))
        ast_img = pygame.transform.scale(ast_img, (self.size * 25, self.size * 12))
        ast_img = pygame.transform.rotate(ast_img, 180)
        self.sprites.append(ast_img)
        ast_img = pygame.image.load(os.path.join("FirstGame","Assets","Asteroid_(anim2).png"))
        ast_img = pygame.transform.scale(ast_img, (self.size * 25, self.size * 12))
        ast_img = pygame.transform.rotate(ast_img, 180)
        self.sprites.append(ast_img)
        ast_img = pygame.image.load(os.path.join("FirstGame","Assets","Asteroid_(anim3).png"))
        ast_img = pygame.transform.scale(ast_img, (self.size * 25, self.size * 12))
        ast_img = pygame.transform.rotate(ast_img, 180)
        self.sprites.append(ast_img)
        self.ast_img = ast_img
        self.mask = pygame.mask.from_surface(self.ast_img)

    def update(self):
        if self.is_animating == True:
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.ast_img = self.sprites[int(self.current_sprite)]
        else:
            self.ast_img = self.sprites[0]

    def move(self, vel):
        self.x -= vel
      

