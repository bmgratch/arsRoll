# arsRoll.py - a die rolling module for Ars Magica uses

# All the simulations could be done with random.randint()
from random import randint


def roll(b=None):
    roll = randint(0,9)
    
    #TODO botch dice. not needed for aging
    if b:
        if roll == 0:
            return(0)

        # processing exploding dice
        mult = 1
        while roll == 1:
            mult *= 2 # double on a 1, roll again
            roll = randint(1, 10)
        return(roll * mult)
    
    # if b=None then it is a simple die
    else:
        if roll == 0:
            return(10)
        else:
            return(roll)