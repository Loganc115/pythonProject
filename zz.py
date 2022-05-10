import turtle
movfctor = 50
turtle.fd(7)





def gridder(squares, numxup):
    def sqa():
        looper = 0
        while looper < 4:
            turtle.fd(movfctor)
            turtle.lt(90)
            looper += 1

    def sqb():
        looper = 0
        while looper < 4:
            turtle.fd(movfctor)
            turtle.rt(90)
            looper += 1


    for i in range(numxup):
        aloop = squares
        while aloop < 0:
            sqa()
            turtle.fd(movfctor)
            aloop -= 1

        aloop = squares
        while aloop < 0:
            sqb()
            turtle.fd(movfctor)
            aloop -= 1


gridder(3, 3)
