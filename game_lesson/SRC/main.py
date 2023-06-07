import pygame
import random
from Character import Slime
from bullet import Bullet

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



bulls_list = []
bulls_list2 = []



c1 = Slime()
c2 = Slime()
astro = Slime(r"C:\Users\micha\Desktop\Progix-course-in-Python\game_lesson\IMAGES\astroid.png")

c1.image = c1.diraction()

c1.set_pos(50, 300)
c2.set_pos(350, 300)
astro.set_pos(250 , 20)

all_sprites_list.add(c1)
all_sprites_list.add(c2)
all_sprites_list.add(astro)


finish = False

f = False
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
            if event.key == pygame.K_DOWN:
                c1.move(0, 5)
            if event.key == pygame.K_d:
                c2.move(5, 0)
            if event.key == pygame.K_a:
                c2.move(-5, 0)
            if event.key == pygame.K_s:
                c2.move(0, 5)
            if event.key == pygame.K_w:
                c2.isJump = True
            if event.key == pygame.K_f:
                b = c2.shoot()
                bulls_list.append(b)
                all_sprites_list.add(b)

            if event.key == pygame.K_l:
                b = c1.shoot()
                b.image = b.diraction()
                bulls_list2.append(b)
                all_sprites_list.add(b)

                
    screen.blit(backgruond, (0,0))

    if pygame.sprite.collide_rect(c1, astro) == True:
        all_sprites_list.remove(c1)

    for i in bulls_list:
        if pygame.sprite.collide_rect(i, c1) == True:
            all_sprites_list.remove(c1)
            all_sprites_list.remove(i)
        if i.rect.x != -100:
            i.move(-5, 0)
        else:
            bulls_list.remove(i)

    for i in bulls_list2:
        if pygame.sprite.collide_rect(i, c2) == True:
            all_sprites_list.remove(c2)
            all_sprites_list.remove(i)
        if i.rect.x < 500:
            i.move(5, 0)
        else:
            bulls_list2.remove(i)

# אם לוחצים על האסטרואיד עם העכבר מודפס היי
    if c2.is_clicked() == True:
        print("hii")



    if pygame.sprite.collide_rect(c1, c2) == True:
        print("hello")

    c1.jump()
    c2.jump()

    astro.move(0, 5)
    pygame.key.set_repeat(30)

# אם העכבר עובר מעל האסטרואיד הוא גדל
    astro.up_and_doun()

# זה חשוב להדפיס על מסך המשחק את כל האובייקטים
    all_sprites_list.draw(screen)  

    clock.tick(REFRESH_RATE)
    
    pygame.display.update()


