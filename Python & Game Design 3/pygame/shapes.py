import pygame, sys
from pygame.locals import * # Importing pygame modules

pygame.init() # Initialize the pygame
white = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((600, 600), pygame.RESIZABLE) # To make the window resizable
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
    screen.fill(white) # Fill screen with blue color

    #Shape 1
    # # Using draw.rect module of pygame to draw an outlined rectangle
    # pygame.draw.rect(screen,(0,0,255),[100,100,400,100],2)
    
    # 

    #Shape 2
    # pygame.draw.circle(screen, (0,255,0), [300,300], 170, 3)

    #Shape 3
    #pygame.draw.polygon(screen,(255,0,0),[[300,300],[100,400], [100,300]])

    #Shape 4
    # pygame.draw.line(screen, (0,0,0), [100,300], [500,300], 5)

    #Shape 5
    # pygame.draw.rect(screen, (0,0,255), [50,200,500,200])
    # pygame.draw.circle(screen,(0,255,0),[300,300], 100)

    # Shape 6
    # Creating a list of different rects
    rectangle_list = [pygame.Rect(50, 100, 500, 200),
                      pygame.Rect(70, 120, 460, 160),
                      pygame.Rect(90, 140, 420, 120),
                      pygame.Rect(110, 160, 380, 80),
                      pygame.Rect(130, 180, 340, 40)
                      ]
    
    # Creating list of different colors
    color_list = [(0,0,0),
                  (255,255,255),
                  (0,0,255),
                  (0,255,0),
                  (255,0,0)
                  ]
    # Creating a variable which we will use to iterate over the color_list
    color_var = 0

    # Iterating over the rectangle_list using for loop
    for reactangle in rectangle_list:

        # Drawing the rectangle using the draw.rect() method
        pygame.draw.rect(screen, color_list[color_var], reactangle)

        # Increasing the value of color_var by 1 after every iteration
        color_var += 1
    
    # Draw the spahe
    pygame.display.update()

    # pygame.display.flip() #Update the display
pygame.quit()

