import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.y_velocity = 0

    def update(self):
        self.rect.y += self.y_velocity

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

player = Player(100, 300)
player_group = pygame.sprite.Group()
player_group.add(player)

platform = Platform(50, 400, 100, 20)
platform_group = pygame.sprite.Group()
platform_group.add(platform)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_group.update()
    collided = pygame.sprite.spritecollide(player, platform_group, False)

    if collided:
        player.y_velocity = 0
    screen.fill((255, 255, 255))
    player_group.draw(screen)
    platform_group.draw(screen)
    pygame.display.flip()

pygame.quit()