import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
