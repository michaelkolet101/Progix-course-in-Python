import pygame
from bullet import Bullet
import random
import time

IMAGE_SIZE = (100, 100)

class Slime(pygame.sprite.Sprite):

    def __init__(self, img=r"C:\Users\micha\Desktop\game_lesson\IMAGES\example.png"):
        super().__init__()
        self.IMAGE_SIZE = (100, 100)
        self.image = pygame.image.load(img).convert()
        self.image = pygame.transform.scale(self.image, self.IMAGE_SIZE)
        self.image.set_colorkey("black")
        self.my_list = pygame.sprite.Group()

        self.rect = self.image.get_rect(center=(10,10))
    
        self.isJump = False
        self.jumpCount = 10 

    def get_pos(self):
        return self.rect.x, self.rect.y
    
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def move(self, new_x, new_y):
        self.rect.x += new_x
        self.rect.y += new_y

        self.center()




    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump == True:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect.y -= self.jumpCount**2 * 0.3 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
        self.center()


    def center(self):
        if self.rect.y < -100 or self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = random.randint(1, 499)
        if self.rect.x > 600 or self.rect.x < -100:
            self.rect.x = 0

    def diraction(self):
        return pygame.transform.flip(self.image, True, False)
    
    def get_image_size(self):
        return self.IMAGE_SIZE

    def shoot(self):
        bullet = Bullet()

        bullet.set_pos(self.rect.x, self.rect.y + 50)
        return bullet

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def moush_over(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def big_img(self):
        self.image = pygame.transform.scale(self.image, (200, 200))

    def small_img(self):
        self.image = pygame.transform.scale(self.image, self.IMAGE_SIZE)

    def up_and_doun(self):
        if self.moush_over() == True:
            self.big_img()
        else:
            self.small_img()
