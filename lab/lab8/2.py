
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40  # Bigger cells
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels')

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont('Arial', 24)

# Snake initialization
snake = [(5, 5)]
direction = (1, 0)

# Food
def generate_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake and pos not in walls:
            return pos

# Level, Score, Speed
level = 1
score = 0
speed = 6

# Wall configuration (can change per level if desired)
walls = []

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake():
    for segment in snake:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_food(pos):
    rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)

def draw_walls():
    for wall in walls:
        rect = pygame.Rect(wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, rect)

def draw_info():
    score_text = font.render(f'Score: {score}', True, WHITE)
    level_text = font.render(f'Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

# Generate first food
food = generate_food()

# Main loop
running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Direction control
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
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Wrap the snake around screen edges
    head = (head[0] % GRID_WIDTH, head[1] % GRID_HEIGHT)

    # Collision with self or walls
    if head in snake or head in walls:
        running = False

    # Eat food
    if head == food:
        snake.insert(0, head)
        score += 1

        # Level up every 4 food
        if score % 4 == 0:
            level += 1
            speed += 1  # Increase speed per level

        food = generate_food()
    else:
        snake.insert(0, head)
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    draw_snake()
    draw_food(food)
    draw_walls()
    draw_info()
    pygame.display.flip()

pygame.quit()
sys.exit()
