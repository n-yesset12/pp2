
import pygame
import sys
import random
import time
import psycopg2

# ---------- DB SETUP ----------
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

def connect():
    return psycopg2.connect(**DB_PARAMS)

def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_user_level(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else 1

def save_score(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

# ---------- PYGAME SETUP ----------
pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Weighted Food with Timer & DB Save")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# ---------- USERNAME INPUT SCREEN ----------
def get_username_screen():
    input_active = True
    username = ""
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_active

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username.strip() != "":
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15:
                        username += event.unicode

        screen.fill(BLACK)
        prompt = font.render("Enter your username:", True, WHITE)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - 80))

        txt_surface = font.render(username, True, WHITE)
        input_box.w = max(200, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

# ---------- GAME VARIABLES ----------
username = get_username_screen()
user_id = get_or_create_user(username)
level = get_user_level(user_id)
print(f"Welcome {username}, starting at level {level}!")

LEVEL_SPEEDS = {1: 8, 2: 12, 3: 16}
speed = LEVEL_SPEEDS.get(level, 8)

snake = [(5, 5)]
direction = (1, 0)
score = 0
food = None
food_lifetime = 5  # seconds

def generate_food():
    pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    weight = random.choice([1, 2, 5])
    spawn_time = time.time()
    return (pos, weight, spawn_time)

def draw_snake():
    for segment in snake:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

def draw_food(f):
    if not f:
        return
    pos, weight, _ = f
    color = RED if weight == 1 else YELLOW if weight == 2 else (255, 165, 0)
    rect = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def draw_info():
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 130, 10))

# ---------- MAIN GAME LOOP ----------
running = True
paused = False
food = generate_food()

while running:
    clock.tick(speed)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused. Saving score...")
                    save_score(user_id, score, level)
                else:
                    print("Game resumed.")

    if paused:
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

    if new_head in snake:
        print("Game over. Saving final score...")
        save_score(user_id, score, level)
        running = False

    snake.insert(0, new_head)

    if food:
        food_pos, weight, spawn_time = food
        if new_head == food_pos:
            score += weight
            food = generate_food()
        elif time.time() - spawn_time > food_lifetime:
            food = generate_food()
        else:
            snake.pop()
    else:
        food = generate_food()

    draw_snake()
    draw_food(food)
    draw_info()
    pygame.display.flip()

pygame.quit()
sys.exit()

