import pygame
import random
from Character import Slime
import pygame.sprite

pygame.init()

clock = pygame.time.Clock()

REFRESH_RATE = 15

screen = pygame.display.set_mode( (500, 500) )

pygame.display.set_caption("MY NEW GAME!!!")


backgruond = pygame.image.load(r"C:\Users\micha\Desktop\game_lesson\IMAGES\bg.jpg").convert()

# # שינוי גודל התמונה שיהיה כמו הגודל של מסך המשחק
backgruond = pygame.transform.scale(backgruond, (500, 500))

all_sprites_list = pygame.sprite.Group()

c1 = Slime()
c2 = Slime()

c1.image = c1.diraction()

c1.rect.x = 250
c1.rect.y = 250

all_sprites_list.add(c1)
all_sprites_list.add(c2)

finish = False


while finish == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                c1.isJump = True
            if event.key == pygame.K_RIGHT:
                c1.move(5, 0)
            if event.key == pygame.K_LEFT:
                c1.move(-5, 0)
        
                
    screen.blit(backgruond, (0,0))
    
    
    if pygame.sprite.collide_rect(c1, c2) == True:
        print("hello")
    
    c2.move(0,12)
    c1.jump()
    pygame.key.set_repeat(30) 
    all_sprites_list.draw(screen)  
    clock.tick(REFRESH_RATE)
    
    pygame.display.update()


