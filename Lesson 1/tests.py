from hometask_1 import *
import sys

#task 1
name = 'alison smith'
if capName(name) != 'Alison Smith':
    print('task 1: Error with ', name)
    sys.exit()

name = '123some name'
if capName(name) != '123some Name':
    print('task 1: Error with ', name)
    sys.exit()

#task 2
s = 'aabcccd'
res = {'a':2, 'b':1, 'c':3, 'd':1}
if charFreq(s) != res:
    print('task 2: Error with ', s)
    sys.exit()

#task 3
s = 'make'
if sliceStr(s) != s:
    print('task 3: Error with ', s)
    sys.exit()

s = '!'
if sliceStr(s) != '':
    print('task 3: Error with ', s)
    sys.exit()

s = 'heh'
if sliceStr(s) != 'heeh':
    print('task 3: Error with ', s)
    sys.exit()

#task 4
List = ['dad', 'm', 'nope', 'yes! y']
if countStr(List) != 2:
    print('task 4: Error with ', List)
    sys.exit()

#task 5
set1, set2, set3 = set([1,2]), set([2,3]), set([2])
if subSet(set1,set2,set3) != True:
    print('task 5: Error with ', set3)
    sys.exit()
    
set1, set2, set3 = set([1,2]), set([2,3]), set([3])
if subSet(set1,set2,set3) != False:
    print('task 5: Error with ', set3)
    sys.exit()

#task 6
n = 3
res = {1:1, 2:4, 3:9}
if makeDict(n) != res:
    print('task 6: Error with ', res)
    sys.exit()

#task 7
d1 = {1:2, 2:3}
d2 = {3:4, 4:5}
res = {1:2, 2:3, 3:4, 4:5}
if mergeDict(d1, d2) != res:
    print('task 7: Error with ', res)
    sys.exit()

#task 8
d = {1:3, 2:7, 3:-1, 4:8}
res = [8, 7, 3]
if highestVals(d) != res:
    print('task 8: Error with ', d)
    sys.exit()

#task 9
l = [1,1,2,2,2,2,4]
res = [1,2,4]
if unique(l) != res:
    print('task 9: Error with ', res)
    sys.exit()

#task 10
l1 = [1,2,3]
l2 = [2,3,4]
res = {1, 4}
if diffOfLists(l1, l2) != res:
    print('task 10: Error with ', res)
    sys.exit()

print('All tests are ended successfuly')
