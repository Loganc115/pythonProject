import turtle
print(turtle.window_width())
print(turtle.window_height())
turtle.speed(150)
turtle.penup()
turtle.goto(-(turtle.window_width()/2), -(turtle.window_height()/2))
turtle.pendown()

def square(movfctor):
    looper = 0
    while looper < 4:
        turtle.fd(movfctor)
        turtle.lt(90)
        looper += 1
    turtle.fd(movfctor)


def subp(x,movfctor):
    y=x
    while y > 0:
        square(movfctor)
        y -= 1


def griduprside(movfctor):
    turtle.lt(90)
    turtle.fd(movfctor * 2)
    turtle.lt(90)


def continiousa(x, y, scale):
    movfctor=scale
    height=y
    while height > 0:
        subp(x,movfctor)
        griduprside(movfctor)
        height -=1
        subp(x,movfctor)
        turtle.lt(-180)
        height -= 1
continiousa(9,7,50)


turtle.mainloop()
