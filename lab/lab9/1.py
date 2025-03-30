
import pygame, sys, random, time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer with Weighted Coins")

# Set up colors and fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Game variables
FPS = 60
FramePerSec = pygame.time.Clock()
SPEED = 5
SCORE = 0
COINS = 0
COIN_THRESHOLD = 5  # Increase speed every N coins

# Load images
background = pygame.image.load("assets/AnimatedStreet.png")

# --- Classes ---

# Enemy car
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin with weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.choice([1, 2, 5])  # Coin weight

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# --- Sprite Groups ---
P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(P1, E1)

# Events
SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 2000)

# --- Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_COIN:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

    DISPLAYSURF.blit(background, (0, 0))

    # Show score and coin count
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision with coins
    for coin in pygame.sprite.spritecollide(P1, coins, True):
        COINS += coin.weight
        if COINS % COIN_THRESHOLD == 0:
            SPEED += 1  # Increase speed when enough coins collected

    pygame.display.update()
    FramePerSec.tick(FPS)
