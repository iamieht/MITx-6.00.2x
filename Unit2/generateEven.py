import random

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)


print(genEven())