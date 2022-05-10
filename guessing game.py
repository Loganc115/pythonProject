#I am logan Clementi
from numpy import random
print("I am guessing a number between 1 and 3")

number= random.randint(1, 3)
numberstr=str(number)
guess=int(input("guess a number"))

if number == guess:
    print("you got it!")
else:
    if number >= guess:
        print(' you were too low! better luck next time!, the number was ' + numberstr)
    else:
        print(' you were too low! better luck next time!, the number was ' + numberstr)

pass
