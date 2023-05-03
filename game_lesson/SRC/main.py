import pygame

pygame.init()

clock = pygame.time.Clock()
REFRESH_RATE = 60

screen = pygame.display.set_mode( (500, 500) )

pygame.display.set_caption("MY NEW GAME!!!")


backgruond = pygame.image.load(r"C:\Users\micha\Desktop\game_lesson\IMAGES\bg.jpg").convert()

# שינוי גודל התמונה שיהיה כמו הגודל של מסך המשחק
backgruond = pygame.transform.scale(backgruond, (500, 500))

# הדמות במשחק
bird = pygame.image.load(r"C:\Users\micha\Desktop\game_lesson\IMAGES\example.png").convert()
bird = pygame.transform.scale(bird, (100, 100))
bird.set_colorkey('black')

finish = False

circle_x = 0
circle_y = 250

while finish == False:

    screen.blit(backgruond, (0,0))
    #screen.fill('red')
    
    screen.blit(bird, (circle_x, circle_y))
    screen.blit(bird, (circle_x + 50, circle_y + 50))
    screen.blit(bird, (circle_x + 100, circle_y + 100))
    #pygame.draw.circle(screen, 'white', [circle_x, circle_y], 50, 0)

    
    if circle_x > 500:
        circle_x = -100

    if circle_x < -100:
        circle_x = 500
    
        

    # רשימת האירועים שיכולים לקרות
    for event in pygame.event.get():

        # לחצו על יציאה מהמשחק ולכן המשחק יוצא
        if event.type == pygame.QUIT:
            finish = True

        # לעשות פקודה אם לחצנו מקש שהוא חץ ימינה אז הדמות יזוז ימינה
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                circle_x += 20
                
                
            if event.key == pygame.K_LEFT:
                circle_x -= 20
                

            if event.key == pygame.K_UP:
                circle_y -= 20
                

            if event.key == pygame.K_DOWN:
                circle_y += 20
                
            pygame.key.set_repeat(100)

            

    clock.tick(REFRESH_RATE)
    
    pygame.display.update()


