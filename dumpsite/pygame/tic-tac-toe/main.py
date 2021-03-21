# https://www.youtube.com/watch?v=mR5pAJdW8fo

import sys
import pygame
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

FPS = 60

run = True

# define variables
line_width = 6
markers = [[0 for _ in range(3)] for _ in range(3)]
clicked = False
player = 1
winner = 0
game_over = False

# define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# define font 
font = pygame.font.SysFont(None, 40)

# create play again rect
again_rect = pygame.Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 160, 50)

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (SCREEN_WIDTH, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, SCREEN_HEIGHT), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner, game_over
    y_pos = 0

    for x in markers:
        # check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        elif sum(x) == -3:
            winner = 2
            game_over = True
        
        # check row
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner = 1
        game_over = True

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
        winner = 2
        game_over = True

def draw_winner(winner):
    screen.fill((255, 255, 255))
    win_text = f"Player {winner} wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 50))
    screen.blit(win_img, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50 ))

    again_txt = "Play Again?"
    again_img = font.render(again_txt, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))

while run:
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                cell_x, cell_y = event.pos
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

    if game_over:
        draw_winner(winner)
        # check if user has clicked for play again
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = event.pos
            if again_rect.collidepoint(pos):
                player = 1
                markers = [[0 for _ in range(3)] for _ in range(3)]
                winner = 0
                game_over = False

    pygame.display.update()
    clock.tick(FPS)