import turtle
import math
turtle.shape("turtle")
t = turtle.Turtle()
def triangle(y):
    x=90

    p=(90-y)
    t.fd(x)
    t.left(p)
    t.fd(x)
    t.left((p*2))
    z=math.sqrt(p**2+p**2)
    t.fd(z)
    t.goto(0,0)
    t.rt((x*2-y))

triangle(0)
triangle(180)
turtle.mainloop()
