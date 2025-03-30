
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App - Advanced Shapes")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Colors and default values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK
drawing = False
start_pos = None
tool = "square"  # Default tool

# Fill background
screen.fill(WHITE)

# Tool buttons
tools = ["square", "right_triangle", "equilateral_triangle", "rhombus"]
tool_buttons = {tool: pygame.Rect(10 + i * 140, 10, 130, 30) for i, tool in enumerate(tools)}

def draw_ui():
    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        label = font.render(name.replace("_", " ").title(), True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 5))
        if tool == name:
            pygame.draw.rect(screen, BLACK, rect, 2)

# Draw shapes
def draw_square(surf, start, end, color):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], side, side)
    pygame.draw.rect(surf, color, rect, 2)

def draw_right_triangle(surf, start, end, color):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surf, color, points, 2)

def draw_equilateral_triangle(surf, start, end, color):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    height = int(math.sqrt(3) / 2 * side)
    top = (x1 + side // 2, y1)
    left = (x1, y1 + height)
    right = (x1 + side, y1 + height)
    pygame.draw.polygon(surf, color, [top, left, right], 2)

def draw_rhombus(surf, start, end, color):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surf, color, points, 2)

# Main loop
while True:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check tool click
                for name, rect in tool_buttons.items():
                    if rect.collidepoint(event.pos):
                        tool = name
                        break
                else:
                    drawing = True
                    start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if tool == "square":
                    draw_square(screen, start_pos, end_pos, current_color)
                elif tool == "right_triangle":
                    draw_right_triangle(screen, start_pos, end_pos, current_color)
                elif tool == "equilateral_triangle":
                    draw_equilateral_triangle(screen, start_pos, end_pos, current_color)
                elif tool == "rhombus":
                    draw_rhombus(screen, start_pos, end_pos, current_color)
                drawing = False

    pygame.display.flip()
    clock.tick(60)
