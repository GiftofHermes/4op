def goal_check(goal,num1,num2,num3,num4,num5,num6):
    numbers = [num1,num2,num3,num4,num5,num6]
    for i in numbers:
        if goal == numbers[i]:
            return True
    return False