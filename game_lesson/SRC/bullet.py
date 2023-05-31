import pygame
import random
import time

IMAGE_SIZE = (100, 100)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, img=r"C:\Users\micha\Desktop\Progix-course-in-Python\game_lesson\IMAGES\bullt.JPG"):
        super().__init__()
        self.IMAGE_SIZE = (10, 30)
        self.image = pygame.image.load(img).convert()
        self.image = pygame.transform.scale(self.image, self.IMAGE_SIZE)
        self.image.set_colorkey("white")
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect(center=(10, 10))

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

        if self.rect.x > 500 or self.rect.y > 500:
            self.rect.x = random.randint(1, 499)
            self.rect.y = 0

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect.y -= self.jumpCount ** 2 * 0.3 * neg
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
            self.rect.x = 250

    def diraction(self):
        return pygame.transform.flip(self.image, True, False)


    def get_image_size(self):
        return self.IMAGE_SIZE
