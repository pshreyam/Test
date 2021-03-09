import pygame
import sys
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.withdraw()

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sketch with pygame")
clock = pygame.time.Clock()

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (103, 47, 120)
YELLOW = (247, 222, 27)

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

            if x in range(10, 30):
                if y in range(10, 30):
                    color = RED
                elif y in range(50, 70):
                    color = BLACK
                elif y in range(90, 110):
                    color = BLUE
                elif y in range(130, 150):
                    color = GREEN
                elif y in range(170, 190):
                    color = PURPLE
                elif y in range(210, 230):
                    color = YELLOW
                elif y in range(SCREEN_HEIGHT-10-20, SCREEN_HEIGHT-10):
                    color = WHITE

            if x not in range(0, 40):
                point = pygame.rect.Rect(x - size/2, y - size /2, size, size)
                pygame.draw.ellipse(screen, color, point)

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                x, y = event.pos

                if x not in range(0, 40):
                    point = pygame.rect.Rect(x - size/2, y - size /2, size, size)
                    pygame.draw.ellipse(screen, color, point)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # CLear screen with escape
                screen.fill(WHITE)
            
            if event.key == pygame.K_s:
                if pygame.key.get_mods() and pygame.KMOD_CTRL:
                    filename = filedialog.asksaveasfilename(
                        defaultextension=".jpg", 
                        filetypes=[("JPEG", '*.jpg'), ("PNG", "*.png")]
                    )

                    if filename:
                        pygame.image.save(screen.subsurface((40, 0, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40)), filename)

            if event.key == pygame.K_LEFTBRACKET:
                # Minimum size 20
                if size > 20:
                    size -= 10
        
            if event.key == pygame.K_RIGHTBRACKET:
                # Maximum size 100
                if size < 100:
                    size += 10

    menu_bar = pygame.rect.Rect(0, 0, 40, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (44, 47, 82), menu_bar)

    red_button = pygame.rect.Rect(10, 10, 20, 20)
    pygame.draw.rect(screen, RED, red_button)

    black_button = pygame.rect.Rect(10, 50, 20, 20)
    pygame.draw.rect(screen, BLACK, black_button)

    blue_button = pygame.rect.Rect(10, 90, 20, 20)
    pygame.draw.rect(screen, BLUE, blue_button)

    green_button = pygame.rect.Rect(10, 130, 20, 20)
    pygame.draw.rect(screen, GREEN, green_button)

    purple_button = pygame.rect.Rect(10, 170, 20, 20)
    pygame.draw.rect(screen, PURPLE, purple_button)

    yellow_button = pygame.rect.Rect(10, 210, 20, 20)
    pygame.draw.rect(screen, YELLOW, yellow_button)

    eraser_button = pygame.rect.Rect(10, SCREEN_HEIGHT-10-20, 20, 20)
    pygame.draw.rect(screen, WHITE, eraser_button)

    # pygame.draw.aaline(screen, BLACK, (40, 0), (40, SCREEN_HEIGHT))

    pygame.display.update()
    clock.tick(FPS)
