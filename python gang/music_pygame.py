import pygame
from pygame import mixer
file = 'my_sound.mp3'

pygame.init()
mixer.init()


# Loading the song
mixer.music.load(file)

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()

    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()

    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break




