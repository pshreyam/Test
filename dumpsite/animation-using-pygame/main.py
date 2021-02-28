import pygame
import sys
import random

pygame.init()
sc_width, sc_height = 800, 500
screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption('Animation')
clock = pygame.time.Clock()

FPS = 60

# Objects
class Ball:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw_ball(self):
        self.ball = pygame.Rect(random.randint(10, sc_width), random.randint(10, sc_width), self.size, self.size)
        pygame.draw.ellipse(screen, self.color, self.ball)

# Colors
pink = (204, 6, 145)
blue = (7, 14, 224)
red = (224, 18, 7)
lightgreen = (7, 224, 83)

class Speed:
    x_speed = 10
    y_speed = 10
    
small_ball = Ball(20, pink)
medium_ball = Ball(30, red)
large_ball = Ball(40, blue)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(lightgreen)

    small_ball.draw_ball()
    medium_ball.draw_ball()
    large_ball.draw_ball()

    pygame.display.flip()
    clock.tick(FPS)
