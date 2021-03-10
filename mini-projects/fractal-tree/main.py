""" Fractal Tree
Generates fractal tree using recursion
"""

import turtle
import time

screen = turtle.Screen()
screen.title('Fractal Tree')
screen.screensize(500, 500)

t = turtle.Turtle(visible=False)
t.color('green')
t.pensize(10)
t.left(90)
t.backward(100)
t.speed(5000)

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.left(30)
        tree(3 * i/4)
        t.right(60)
        tree(3 * i/4)
        t.left(30)
        t.backward(i)

tree(100)
t.penup()
t.backward(100)
t.write("Fractal Tree", align="center", font=("Monserrat", 20, "normal"))
time.sleep(5)