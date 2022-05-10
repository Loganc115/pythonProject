import turtle
impo$ python3 -m pip install -U .[voice]
rt math
turtle.shape("turtle")
t = turtle.Turtle()
def triangle(y):
    x=90

    p=(90-y)
    t.fd(x)
    t.left(p)
    t.fd(x)
    t.left((p*1.5))
    z = math.sqrt(p**2+p**2)
    t.fd(z)
import turtle
import math
turtle.shape("turtle")
t = turtle.Turtle()
def triangle(x,a,rotation):
    print(t.position)
    Rangle=(90-rotation)
    t.fd(x)
    t.left(Rangle)
    t.fd(a)
    toa=math.tan(a / x)
    theta=(toa/toa**2)
    print(theta*100)
    t.lt((theta*100)-rotation)
    turtle.setheading(90)
    hypotenuse=math.sqrt(x**2+a**2)
    t.fd(hypotenuse)
    t.penup()
    print(t.position)
    t.goto(0,0)


    t.pendown()
    t.rt(theta+Rangle)

triangle(90,60, 0)

triangle(90,60, 90)

turtle.mainloop()

def triangle(y):
    x=90

    p=(90-y)
    t.fd(x)
    t.left(p)
    t.fd(x)
    t.left((p*1.5))
    z = math.sqrt(p**2+p**2)
    t.fd(z)