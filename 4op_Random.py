import random

big_numbers = (100,75,50,25)
small_numbers = (1,2,3,4,5,6,7,8,9,10)

def generate_goal():
    return random.randrange(100,1000)

def generate_littles():
    littles = [0,0,0,0,0,0]
    for i in range(6):
        littles[i] = random.randrange(1,11)
        while littles.count(littles[i]) > 2:
            print(littles)
            littles[i] = random.randrange(1, 11)
    return littles

def generate_big():
    return random.choice(big_numbers)



goal = generate_goal()

#big = generate_big()
littles = generate_littles()

print('The goal is: ', goal)
print('Numbers are',*littles)

