import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive 2D Drawing")

# Variables
drawing = False
start_pos = None
current_shape = "line"  # Default shape
color = RED
shapes = []  # To store drawn shapes

# Font for instructions
font = pygame.font.Font(None, 24)
instructions = [
    "Press '1' for Line, '2' for Rectangle, '3' for Circle",
    "Press 'R', 'G', 'B' to change color to Red, Green, Blue",
    "Click and drag to draw. Press 'C' to clear the screen.",
]

def draw_instructions():
    y_offset = 10
    for line in instructions:
        text = font.render(line, True, BLACK)
        screen.blit(text, (10, y_offset))
        y_offset += 25

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                if current_shape == "line":
                    shapes.append(("line", start_pos, end_pos, color))
                elif current_shape == "rectangle":
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    shapes.append(("rectangle", rect, color))
                elif current_shape == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    shapes.append(("circle", start_pos, radius, color))
            drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = "line"
            elif event.key == pygame.K_2:
                current_shape = "rectangle"
            elif event.key == pygame.K_3:
                current_shape = "circle"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_c:
                shapes.clear()

    # Clear screen
    screen.fill(WHITE)

    # Redraw all shapes
    for shape in shapes:
        if shape[0] == "line":
            pygame.draw.line(screen, shape[3], shape[1], shape[2], 2)
        elif shape[0] == "rectangle":
            pygame.draw.rect(screen, shape[2], shape[1], 2)
        elif shape[0] == "circle":
            pygame.draw.circle(screen, shape[3], shape[1], shape[2], 2)

    # Draw current instructions
    draw_instructions()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
