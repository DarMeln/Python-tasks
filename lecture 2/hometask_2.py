#Task 1
def oddNums(x):
    counter = 0
    for i in range(x+1):
        if not i%2==0:
            print(i, end = ' ')
            counter+=1
    print('\ncount = ', counter)

#Task 2
def devideByC(a, b, c):
    counter = 0
    for i in range(a+1, b): #between a & b
        if i%c==0:
            counter+=1
    return counter

#Task 3
def factorialRecursive(num):
    if num==0: return 1
    else: return num * factorialRecursive(num-1)

#or with dynamic programming:
def factorialDP(num):
    res = 1
    while num:
        res = res*num
        num-=1
    return res

#Task 4
def rangeList(end, start = 0, step=1):
    res = []
    while start < end:
        res.append(start)
        start+=step
    return res

    

        
