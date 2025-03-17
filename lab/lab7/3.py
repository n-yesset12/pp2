import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)
STEP = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")

x, y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - BALL_RADIUS - STEP >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + BALL_RADIUS + STEP <= HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x - BALL_RADIUS - STEP >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + BALL_RADIUS + STEP <= WIDTH:
                x += STEP

pygame.quit()
