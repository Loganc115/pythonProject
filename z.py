import turtle
turtle.setheading(90)

def longforward(x):
    turtle.fd(x*2)

def turnaround():
    turtle.lt(180)

def cross():
    turtle.setheading(90)
    longforward(50)
    turnaround()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turnaround()
    longforward(50)
cross()
turtle.mainloop()
print('deus vult, brother')