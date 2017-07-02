import random

big_numbers = (100,75,50,25)
small_numbers = (1,2,3,4,5,6,7,8,9,10)

def generate_goal(b,l1,l2,l3,l4,l5):
    # return random.randrange(100,1000)

    def method1(b,l1,l2,l3,l4,l5):
        return (l1+l2)*(b+l3)+l4+l5
    def method2(b,l1,l2,l3,l4,l5):
        return (b*l1)+((l2+l3)*(l4*l5))
    def method3(b,l1,l2,l3,l4,l5):
        return (b+l1)*l2+l3*l4*l5
    def method4(b,l1,l2,l3,l4,l5):
        return (l1+l2+l3)*b-l4
    def method5(b,l1,l2,l3,l4,l5):
        return l1*b+(l2*l3)*l4
    def method6(b,l1,l2,l3,l4,l5):
        return b*l1+l2+l3
    def method7(b,l1,l2,l3,l4,l5):
        return b*(l1+l2)-(l3+l4)
    def method8(b,l1,l2,l3,l4,l5):
        return (l1+l2)*b+l3*l4-l5
    def method9(b,l1,l2,l3,l4,l5):
        return l1*b-l2+l3
    def method10(b,l1,l2,l3,l4,l5):
        return l1*l2-l3+l4+l5+b
    def method11(b,l1,l2,l3,l4,l5):
        return b*l1-l2+l3-l4
    def method12(b,l1,l2,l3,l4,l5):
        return b*l1-((abs(l2-l3))*l4)
    def method13(b,l1,l2,l3,l4,l5):
        return (b+l1)*l2*l3+l4*l5
    def method14(b,l1,l2,l3,l4,l5):
        return (b-l1)*(l2+l3)-l4
    def method15(b,l1,l2,l3,l4,l5):
        return  (b+l1)*(abs(l2-l3))+l4
    def method16(b,l1,l2,l3,l4,l5):
        return (l1+l2)*b-l3+l4
    def method17(b,l1,l2,l3,l4,l5):
        return (l1*l2+l3)*b
    def method18(b,l1,l2,l3,l4,l5):
        return (b+l1)*l2-l3
    def method19(b,l1,l2,l3,l4,l5):
        return b+l1*l2+l3-l4
    def method20(b,l1,l2,l3,l4,l5):
        return (b-l1-l2)*l3+l4-l5
    def method21(b,l1,l2,l3,l4,l5):
        return  (b+l1)*l2-l3*l4
    def method22(b,l1,l2,l3,l4,l5):
        return (b+l1+l2)*l3+l4
    def method23(b,l1,l2,l3,l4,l5):
        return (l1+l2)*b-l3
    def method24(b,l1,l2,l3,l4,l5):
        return (b+l1)*l2+l3-l4-l5
    def method25(b,l1,l2,l3,l4,l5):
        return (l1+l2)*b+l3*l4-l5
    def method26(b,l1,l2,l3,l4,l5):
        return (b+l1)*(l2+l3)
    def method27(b,l1,l2,l3,l4,l5):
        return (l1+l2)*(b*l3+l4)
    def method28(b,l1,l2,l3,l4,l5):
        return b*l1*l2+l3*l4-l5
    def method29(b,l1,l2,l3,l4,l5):
        return l1*l2*l3-l4*(b*l5)
    def method30(b,l1,l2,l3,l4,l5):
        return b*l1*l2*(l3+abs(l4-l5))

    all_method_list = [method1, method2, method3, method4, method5,
               method6, method7, method8, method9, method10,
               method11, method12, method13, method14, method15,
               method16, method17, method18, method19, method20,
               method21, method21, method22, method23, method24,
               method25, method26, method27, method28, method29,
               method30]
    high_method_list = [method2, method8, method13, method25,
                        method27, method28, method29, method30]

    # to-do: check for loops, if over xx shuffle (?)
    goal = random.choice(all_method_list)(b,l1,l2,l3,l4,l5)
    counter = 0
    while 100>goal or goal>1000 or (goal%100 == 0):
        goal = random.choice(all_method_list)(b,l1,l2,l3,l4,l5)
        counter +=1
        if counter > 50:
            goal = random.choice(high_method_list)(b,l1,l2,l3,l4,l5)
            (b, l1, l2, l3, l4, l5) = generate_littles(6)

    return (goal)

def generate_littles(num_small):
    """takes how many little numbers to create and returns an array of little numbers"""
    i = 0
    littles = []
    while i < num_small:
        littles.append(0)
        i+=1
    for i in range(len(littles)):
        littles[i] = random.randrange(1,11)

        #there should be only one 1 or 10
        if littles[i] == 1 or littles[i] == 10:
            while littles.count(littles[i]) > 1:
                littles[i] = random.randrange(1, 11)

        #there sheould be at most 2 repeating digits
        while littles.count(littles[i]) > 2:
            littles[i] = random.randrange(1, 11)

    return littles

def generate_bigs(num_big):
    bigs = []
    i = 0
    while i < num_big:
        bigs.append(0)
        i += 1
    for i in range(len(bigs)):
        bigs[i] = random.choice(big_numbers)
        while bigs.count(bigs[i]) > 1:
            bigs[i] = random.choice(big_numbers)
    return bigs

def goal_creation(num_big,num_little):
    """takes number of big and little values and returns a list of numbers and a goal"""
    #to-do: instead of print make this function return values
    bigs = generate_bigs(num_big)
    littles = generate_littles(num_little)
    random.shuffle(littles)
    random.shuffle(bigs)
    goal = generate_goal(*bigs,*littles)
    random.shuffle(littles)

    if len(bigs) > 1:
        bigs = sorted(bigs, reverse= True)


    if(goal-100) < 100:
        print('one hundred: ')
    else:
        print('bigger than one hundred')


    print('The goal is: ', goal)
    print('Numbers are',*bigs,*littles)

#goal_creation(1,5)
#goal_creation(1,5)
#goal_creation(1,5)
#goal_creation(1,5)
#goal_creation(2,4)
#goal_creation(2,4)
#goal_creation(2,4)
#goal_creation(0,6)
#goal_creation(0,6)
#goal_creation(0,6)

for i in range(100):
    goal_creation(0, 6)
