import pygame, sys
from pygame.locals import *  # Importing pygame modules

pygame.init()  # Initialize pygame
DISPLAYSURF = pygame.display.set_mode((600, 600), pygame.RESIZABLE)  # Make the window resizable
pygame.display.set_caption('Python & Game Design 3')  # Window Title

img = pygame.image.load('gameIcon.png')  # Load the image for the window icon
pygame.display.set_icon(img)  # Set the image as the window icon

screen = DISPLAYSURF

# Create a list to store the positions of the circles
circle_positions = []

# Radius of the circles
circle_radius = 60

# Color of the circles
color = (0, 0, 255)

# Run the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)
    
    # Clear the screen with a background color
    screen.fill((255, 255, 255))  # Fill the screen with white background

    # Draw the circles
    for position in circle_positions:
        pygame.draw.circle(screen, color, position, circle_radius)
    
    # Update the display
    pygame.display.update()

pygame.quit()
