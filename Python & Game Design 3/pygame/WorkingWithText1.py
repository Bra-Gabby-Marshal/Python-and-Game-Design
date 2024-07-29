import pygame, sys
from pygame.locals import *

pygame.font.init() # Initialize the Pygame font module

# Check if font is initialized or not
if not pygame.font.get_init():
    print("Font module not initialized!")
    sys.exit()

white = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((500, 500), pygame.RESIZABLE) # Make the window resizable
pygame.display.set_caption('Working with Text') # Window Title

# Create a font object by specifying font name and size
font1 = pygame.font.SysFont('freesansbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 50)

# Text to display
text1 = font1.render('Python & Game Design 3', True, (0, 255, 0))
text2 = font2.render('Working with Text', True, (0, 255, 0))

# Create a rectangle for the text surface 
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

# Setting the first text in the center
textRect1.center = (250, 250)
# Position the second text below the first
textRect2.center = (250, 350)

img = pygame.image.load('gameIcon.png') # Changing the image of the window
pygame.display.set_icon(img) # Setting the image as icon

screen = DISPLAYSURF
running = True
while running:
    screen.fill(white) # Fill screen with white color

    # Displaying text
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2) 

    # Iterate over events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Update the display
pygame.quit()
