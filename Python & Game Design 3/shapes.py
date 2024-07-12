import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Drawing Shapes')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (50, 50, 200, 100))

    # Draw a green circle
    pygame.draw.circle(screen, GREEN, (400, 300), 50)

    # Draw a blue line
    pygame.draw.line(screen, BLUE, (100, 500), (700, 500), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
