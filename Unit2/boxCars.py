import random
random.seed(0)

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests

print('Frequency of double 6 =', str(fracBoxCars(100000)*100) + '%')