import turtle
import math

import turtle
import math
def triangle(x,a,rotation):
    turtle.lt(rotation)

    turtle.fd(x)
    turtle.left(90)
    turtle.fd(a)
    #toa=math.tan((a / x))
   # print(toa)
    #theta=(toa/toa**2)
    #print(theta)
   # turtle.lt((theta*100)-rotation)

    #hypotenuse=math.sqrt(x**2+a**2)
   # turtle.fd(hypotenuse)
   #print(turtle.position)
    turtle.setheading(180)
    turtle.goto(0,0)
x=range(0, 360, 10)
for i in x:
    triangle(90,60, (i))

turtle.mainloop()
