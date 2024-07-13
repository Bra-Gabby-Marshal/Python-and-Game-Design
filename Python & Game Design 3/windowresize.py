# # import package pygame 
# import pygame 

# # Initialize Pygame
# pygame.init()

# # Form screen with 400x400 size 
# # with not resizable 
# screen = pygame.display.set_mode((400, 400)) 

# # Set title 
# pygame.display.set_caption('Not resizable') 

# # Define blue color
# blue = (0, 0, 255)

# # Run window 
# running = True
# while running: 
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT: 
#             running = False
            
#     # Fill screen with blue color
#     screen.fill(blue)
    
#     # Update the display
#     pygame.display.flip()

# # Quit pygame after closing window 
# pygame.quit() 

# import package pygame 
import pygame 

# Initialize Pygame
pygame.init()
# Define blue color
blue = (0, 0, 255)
# Form screen with 400x400 size 
# and with resizable 
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE) 

# Set title 
pygame.display.set_caption('Resizable') 

# Run window 
running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
    # Fill screen with blue color
    screen.fill(blue)
    
    # Update the display
    pygame.display.flip()

# Quit pygame after closing window 
pygame.quit() 
