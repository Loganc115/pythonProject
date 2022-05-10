
import turtle
from numpy import random


turtle.speed(200)
turtle.pensize(3)
turtle.colormode(255)
def turtlerangle():
    turtle.fd(50)
    turtle.lt(90)
def square():
    turtlerangle()
    turtlerangle()
    turtlerangle()
    turtlerangle()
def turtle_randominwindow():
    xrand = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
    yrand = random.randint(-turtle.window_height()/2, turtle.window_height()/2)
    turtle.goto(xrand,yrand)
def randomness(x):
    for n in range(0,x):
        turtle.color(random.randint(0,255+1), random.randint(0, 255 +1), random.randint(0,255 +1 ))
        turtle.penup()
        turtle_randominwindow()
        turtle.pendown()
        square()


randomness(100)
turtle.mainloop()