import pygame, os
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,health = 100,shields = 100):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = []
        self.is_animating = False
        self.size_x = 50
        self.size_y = 50
        self.animation_speed = 0.2
        self.rotation = 0
        self.prevRotate = 0
                
        Spaceship_image = pygame.image.load(os.path.join("FirstGame","Assets","SpaceShip_(moving1).png"))
        Spaceship_image = pygame.transform.rotate(Spaceship_image, 270)
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))
        Spaceship_image = pygame.image.load(os.path.join("FirstGame","Assets","SpaceShip_(moving2).png"))
        Spaceship_image = pygame.transform.rotate(Spaceship_image, 270)
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))
        Spaceship_image = pygame.image.load(os.path.join("FirstGame","Assets","SpaceShip_(moving3).png"))
        Spaceship_image = pygame.transform.rotate(Spaceship_image, 270)
        self.sprites.append(pygame.transform.scale(Spaceship_image,(self.size_x,self.size_y)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = [pos_x,pos_y]
                
    def animate(self):
        self.is_animating = True
    def stop_animating(self):
        self.is_animating = False
    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            print(str(self.prevRotate) + " " + str(self.rotation))

            self.rotation = 90 - self.prevRotate
            self.prevRotate = 90

            for idx in range(0,len(self.sprites)):
                self.sprites[idx] = pygame.transform.rotate(self.sprites[idx], self.rotation)

        if pressed[pygame.K_s]:
            print(str(self.prevRotate) + " " + str(self.rotation))

            self.rotation = 270 - self.prevRotate
            self.prevRotate = 270

            for idx in range(0,len(self.sprites)):
                self.sprites[idx] = pygame.transform.rotate(self.sprites[idx], self.rotation)

        if pressed[pygame.K_a]:
            print(str(self.prevRotate) + " " + str(self.rotation))

            self.rotation = 180 - self.prevRotate
            self.prevRotate = 180

            for idx in range(0,len(self.sprites)):
                self.sprites[idx] = pygame.transform.rotate(self.sprites[idx], self.rotation)

        if pressed[pygame.K_d]:
            print(str(self.prevRotate) + " " + str(self.rotation))

            self.rotation = 0 - self.prevRotate
            self.prevRotate = 0

            for idx in range(0,len(self.sprites)):
                self.sprites[idx] = pygame.transform.rotate(self.sprites[idx], self.rotation)
        

        if self.is_animating == True:
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
            
        else:
            self.image = self.sprites[0]
            pass


    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))
    

