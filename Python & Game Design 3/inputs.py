import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Move the Rectangle')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial position of the rectangle
rect_x, rect_y = 100, 100
rect_width, rect_height = 60, 40
rect_speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the list of keys currently being pressed
    keys = pygame.key.get_pressed()

    # Update the position of the rectangle based on the keys pressed
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the red rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
