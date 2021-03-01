# Practiced from Tech With Tim

import pygame
import os
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game!')

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP) * 13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP*2 + ((RADIUS*2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS*2))
    letters.append([x, y, chr(A + i)])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)

# load images
images = []
for i in range(7):
    image = pygame.image.load(f'./images/hangman{i}.png')
    images.append(image)

# game variables
hangman_status = 0
wordlist = ['PYTHON', 'PYGAME', 'TIMER']
word = random.choice(wordlist)
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons 
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr = letter
                dis = ((x - m_x) ** 2 + (y - m_y) ** 2) ** (1/2)
                if dis < RADIUS:
                    guessed.append(ltr)
                    if ltr not in word:
                        hangman_status += 1
                    letters.remove(letter)

    draw()
    
    won = True
    for ltr in word:
        if ltr not in guessed:
            won = False
            break
    
    if won:
        display_message('You won!')
        break

    if hangman_status == 6:
        display_message('You lost!')
        break

pygame.quit()
