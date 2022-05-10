import turtle
import math

import turtle
import math
def triangle(x,a,rotation):
    turtle.lt(0)

    turtle.fd(x)
    turtle.left(90)
    turtle.fd(a)
    asdf=math.tan((x/a))
    rtabl=(asdf/(asdf**2))
    print(rtabl)
    print(asdf)
    rtd=90+asdf
    print(rtd)
    turtle.lt(124)

    hypotenuse=math.sqrt(x**2+a**2)
    turtle.fd(hypotenuse/2)

   #print(turtle.position)
    #turtle.setheading(180)
   #turtle.goto(0,0)
x=range(0, 360, 10)
for i in x:
    triangle(90,60, (i))

turtle.mainloop()
