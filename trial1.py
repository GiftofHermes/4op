import random

big_numbers = (100,75,50,25)
small_numbers = (1,2,3,4,5,6,7,8,9,10)

def generate_goal():
    return random.randrange(100,1000)

def generate_little():
    return random.randrange(1,11)

def generate_big():
    return random.choice(big_numbers)



goal = generate_goal()

big = generate_big()
one = generate_little()
two = generate_little()
three = generate_little()
four = generate_little()
five = generate_little()

print('The goal is: ', goal)
print('Numbers are', big,one,two,three,four,five)

