import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sketch with pygame")
clock = pygame.time.Clock()

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

color = BLACK
size = 25

screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if x in range(10, 30) and y in range(10, 30):
                color = RED

            if x in range(10, 30) and y in range(50, 70):
                color = BLACK

            if x in range(10, 30) and y in range(SCREEN_HEIGHT-10-20, SCREEN_HEIGHT-10):
                color = WHITE

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                x, y = event.pos

                if x not in range(0, 40):
                    point = pygame.rect.Rect(x, y, size, size)
                    pygame.draw.ellipse(screen, color, point)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # CLear screen with escape
                screen.fill(WHITE)

            if event.key == pygame.K_LEFTBRACKET:
                # Minimum size 20
                if size > 20:
                    size -= 10
        
            if event.key == pygame.K_RIGHTBRACKET:
                # Maximum size 100
                if size < 100:
                    size += 10

    menu_bar = pygame.rect.Rect(0, 0, 40, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (97, 237, 109), menu_bar)

    red_button = pygame.rect.Rect(10, 10, 20, 20)
    pygame.draw.rect(screen, RED, red_button)

    black_button = pygame.rect.Rect(10, 50, 20, 20)
    pygame.draw.rect(screen, BLACK, black_button)

    eraser_button = pygame.rect.Rect(10, SCREEN_HEIGHT-10-20, 20, 20)
    pygame.draw.rect(screen, WHITE, eraser_button)

    # pygame.draw.aaline(screen, BLACK, (40, 0), (40, SCREEN_HEIGHT))

    pygame.display.update()
    clock.tick(FPS)