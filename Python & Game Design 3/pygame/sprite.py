import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Example")

# Define the Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, position):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Create a surface for the sprite
        self.image.fill(color)  # Fill it with the specified color
        self.rect = self.image.get_rect()  # Get the rect for positioning
        self.rect.center = position  # Position the sprite at the given position

def update(self):
        # Update the sprite's position or other properties
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Create a sprite group and add the player sprites
all_sprites = pygame.sprite.Group()
player1 = Player((255, 0, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # Red player at center
player2 = Player((0, 255, 0), (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))  # Green player at left center
player3 = Player((0, 0, 255), (3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))  # Blue player at right center

all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(player3)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw all sprites
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()