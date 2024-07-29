import pygame
import random

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoidance Game")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load sounds
collision_sound = pygame.mixer.Sound("cinematic-hit-159487.mp3")
game_over_sound = pygame.mixer.Sound("mixkit-sad-game-over-trombone-471.wav")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5
        self.lives = 10  # Add life counter
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = random.randint(5, 10)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset_position()
    
    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

# Create sprite groups
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
obstacles = pygame.sprite.Group()

for _ in range(10):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        collision_sound.play()  # Play collision sound
        player.lives -= 1
        for hit in hits:
            hit.reset_position()
        if player.lives <= 0:
            game_over_sound.play()  # Play game over sound
            running = False  # End the game when lives reach zero

    # Draw / render
    window.fill(WHITE)
    all_sprites.draw(window)
    
    # Display lives
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {player.lives}', True, BLACK)
    window.blit(lives_text, (10, 10))

    # Double buffering
    pygame.display.flip()

    # Maintain the frame rate
    clock.tick(FPS)

# Game over message
window.fill(WHITE)
game_over_text = font.render('Game Over', True, BLACK)
window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(3000)  # Display the game over message for 3 seconds

pygame.quit()
