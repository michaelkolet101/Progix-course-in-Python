import pygame

pygame.init()

screen = pygame.display.set_mode( (500, 500) )
pygame.display.set_caption("MY NEW GAME!!!")

finish = False

while finish == False:

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    
    pygame.display.update()
    