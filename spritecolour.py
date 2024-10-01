
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2
OBJECT_SIZE = 50

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.speed = SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

# Object sprite
class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBJECT_SIZE, OBJECT_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH / 4, HEIGHT / 4))

# Create sprite groups
player = Player()
object = Object()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(object)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill(WHITE)

    # Update sprites
    player.update()

    # Check for collision
    if player.rect.colliderect(object.rect):
        player.image.fill(RED)  # Change player color to red

    # Draw sprites
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(144)
