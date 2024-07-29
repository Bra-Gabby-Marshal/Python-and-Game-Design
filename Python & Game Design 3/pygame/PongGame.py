import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_y = 0

    def update(self):
        self.rect.y += self.change_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def move_up(self):
        self.change_y = -6

    def move_down(self):
        self.change_y = 6

    def stop(self):
        self.change_y = 0

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.change_y *= -1
        if self.rect.left <= 0:
            self.change_x *= -1
            self.rect.x = WIDTH // 2
            self.rect.y = HEIGHT // 2
            self.change_x = -5  # Reset to initial speed
            self.change_y = 5
            update_score(2)
        if self.rect.right >= WIDTH:
            self.change_x *= -1
            self.rect.x = WIDTH // 2
            self.rect.y = HEIGHT // 2
            self.change_x = 5  # Reset to initial speed
            self.change_y = 5
            update_score(1)

def update_score(player):
    global score1, score2
    if player == 1:
        score1 += 1
    else:
        score2 += 1
    if score1 >= 10:
        display_winner(1)
    elif score2 >= 10:
        display_winner(2)

def display_winner(player):
    global running
    window.fill(BLACK)
    font = pygame.font.Font(None, 74)
    if player == 1:
        text = font.render("Player 1 Wins!", 1, WHITE)
    else:
        text = font.render("Player 2 Wins!", 1, WHITE)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False

# Create sprite groups
all_sprites = pygame.sprite.Group()

player1 = Paddle(50, HEIGHT // 2 - 50)
player2 = Paddle(WIDTH - 60, HEIGHT // 2 - 50)
ball = Ball()

all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(ball)

# Initialize scores
score1, score2 = 0, 0

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.move_up()
            elif event.key == pygame.K_s:
                player1.move_down()
            elif event.key == pygame.K_UP:
                player2.move_up()
            elif event.key == pygame.K_DOWN:
                player2.move_down()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player1.change_y < 0:
                player1.stop()
            elif event.key == pygame.K_s and player1.change_y > 0:
                player1.stop()
            elif event.key == pygame.K_UP and player2.change_y < 0:
                player2.stop()
            elif event.key == pygame.K_DOWN and player2.change_y > 0:
                player2.stop()

    all_sprites.update()

    # Check for ball collision with paddles
    if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
        ball.change_x *= -1.1  # Increase speed after each hit

    window.fill(BLACK)
    all_sprites.draw(window)

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    window.blit(text, (250, 10))
    text = font.render(str(score2), 1, WHITE)
    window.blit(text, (520, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
