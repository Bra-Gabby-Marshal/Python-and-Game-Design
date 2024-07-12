import pygame, sys
from pygame.locals import * # Importing pygame modules

pygame.init() # Initialize the pygame
blue = (0, 0, 255)
DISPLAYSURF = pygame.display.set_mode((400, 300), pygame.RESIZABLE) # To make the window resizable
pygame.display.set_caption('Python & Game Design 3') # Window Tittle

img = pygame.image.load('gameIcon.png') # Changing the image of the window
pygame.display.set_icon(img) # Setting the image as icon

screen = DISPLAYSURF
# Run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(blue) # Fill screen with blue color

    pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75) #Drawing a circle on the screen

    pygame.display.flip() #Update the display
pygame.quit()

