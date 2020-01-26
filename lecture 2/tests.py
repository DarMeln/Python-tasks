from hometask_2 import *
import sys

#task 1
try:
    oddNums(10)
except:
    print('Something went wrong in task 1')

#task 2
res = 3
if devideByC(4,15,3) != res:
    print('task 2: Error!')
    sys.exit()
res = 0
if devideByC(2,3,1) != res:
    print('task 2: Error!')
    sys.exit()

#task 3
res = 720
if factorialRecursive(6) != res:
    print('task 3: recursive: Error!')
    sys.exit()
if factorialDP(6) != res:
    print('task 3: dynamic: Error!')
    sys.exit()

#task 4
res = [0, 1, 2, 3]
if rangeList(4) != res:
    print('task 2: Error!')
    sys.exit()
res = [4, 5, 6]
if rangeList(7,4) != res:
    print('task 2: Error!')
    sys.exit()
res = [1, 3, 5, 7]
if rangeList(8, 1, 2) != res:
    print('task 2: Error!')
    sys.exit()

print('Success')
    
