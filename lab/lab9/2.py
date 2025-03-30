
import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Screen and grid setup
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Weighted Food with Timer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Snake setup
snake = [(5, 5)]
direction = (1, 0)

# Score and speed
score = 0
speed = 8

# Food structure: (position, weight, spawn_time)
food = None
food_lifetime = 5  # seconds

# Generate food at a random position, with weight 1, 2, or 5
def generate_food():
    pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    weight = random.choice([1, 2, 5])
    spawn_time = time.time()
    return (pos, weight, spawn_time)

# Draw snake
def draw_snake():
    for segment in snake:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

# Draw food with different color based on weight
def draw_food(f):
    if not f:
        return
    pos, weight, _ = f
    color = RED if weight == 1 else YELLOW if weight == 2 else (255, 165, 0)  # orange for 5
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

# Draw score
def draw_info():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main loop
running = True
food = generate_food()
while running:
    clock.tick(speed)
    screen.fill(BLACK)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

    # Check collision with self
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # Food logic
    if food:
        food_pos, weight, spawn_time = food
        if new_head == food_pos:
            score += weight
            food = generate_food()  # generate new food
        elif time.time() - spawn_time > food_lifetime:
            food = generate_food()  # replace expired food
        else:
            snake.pop()  # keep same length
    else:
        food = generate_food()

    # Draw everything
    draw_snake()
    draw_food(food)
    draw_info()
    pygame.display.flip()

pygame.quit()
sys.exit()
