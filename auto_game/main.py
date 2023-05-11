import os
import sys

list_of_dirs = ["images", "src", "modules"]

parent_dir = sys.argv[1]


for path in list_of_dirs:
    path = os.path.join(parent_dir, path)
    os.mkdir(path)


some_code = """
import pygame

pygame.init()

clock = pygame.time.Clock()
REFRESH_RATE = 60

screen = pygame.display.set_mode( (500, 500) )

pygame.display.set_caption("MY NEW GAME!!!")

finish = False

while finish == False:

    for event in pygame.event.get():

       
        if event.type == pygame.QUIT:
            finish = True
            
    clock.tick(REFRESH_RATE)
    
    pygame.display.update()
"""
new_file = os.path.join(parent_dir, "src")
new_file = os.path.join(new_file, "main.py")

f = open(new_file, 'w')

f.write(some_code)


f.close()
