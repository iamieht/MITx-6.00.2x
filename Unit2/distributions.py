import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

print('Dist1:', dist1())
print('Dist2:', dist2())
print('Dist3:', dist3())
print('Dist4:', dist4())