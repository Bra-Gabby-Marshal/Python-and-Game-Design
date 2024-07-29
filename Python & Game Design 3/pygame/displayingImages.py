import pygame, sys
from pygame.locals import * # Importing pygame modules

X = 600
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X,Y))

# set the pygame window name
pygame.display.set_caption('Images')

# create a surface object, image is drawn on it.
imp = pygame.image.load("download.jpeg")

# Using blit to copy content from one surface to other
scrn.blit(imp, (0,0))

pygame.display.flip()
status = True

while (status):

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            status = False
pygame.quit()