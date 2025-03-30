
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# Drawing options
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "black": BLACK}
current_color = BLACK
tool = "circle"  # can be "circle", "rect", or "eraser"
radius = 10
drawing = False
start_pos = None

screen.fill(WHITE)

# Color buttons
color_buttons = {
    "red": pygame.Rect(10, 10, 30, 30),
    "green": pygame.Rect(50, 10, 30, 30),
    "blue": pygame.Rect(90, 10, 30, 30),
    "black": pygame.Rect(130, 10, 30, 30),
}

# Tool buttons
tool_buttons = {
    "circle": pygame.Rect(200, 10, 80, 30),
    "rect": pygame.Rect(290, 10, 80, 30),
    "eraser": pygame.Rect(380, 10, 80, 30),
}

font = pygame.font.SysFont(None, 24)

def draw_ui():
    for name, rect in color_buttons.items():
        pygame.draw.rect(screen, COLORS[name], rect)
        if current_color == COLORS[name]:
            pygame.draw.rect(screen, BLACK, rect, 3)

    for name, rect in tool_buttons.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        label = font.render(name.capitalize(), True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 5))
        if tool == name:
            pygame.draw.rect(screen, BLACK, rect, 3)

def get_color_click(pos):
    for name, rect in color_buttons.items():
        if rect.collidepoint(pos):
            return COLORS[name]
    return None

def get_tool_click(pos):
    for name, rect in tool_buttons.items():
        if rect.collidepoint(pos):
            return name
    return None

while True:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                color_clicked = get_color_click(event.pos)
                tool_clicked = get_tool_click(event.pos)
                if color_clicked:
                    current_color = color_clicked
                elif tool_clicked:
                    tool = tool_clicked
                else:
                    drawing = True
                    start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, current_color, rect, 0)
                drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if drawing and tool in ["circle", "eraser"]:
                color = WHITE if tool == "eraser" else current_color
                pygame.draw.circle(screen, color, event.pos, radius)

    pygame.display.flip()
    clock.tick(60)
