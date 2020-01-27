#Hometask for the 1st lecture: overview & data types
#Task 1
def capName(name):
    S = name.split() #by default, any whitespaces is a separator
    for i in range(len(S)): #if 'for i in S' then S will not change
        S[i] = S[i][0].upper() + S[i][1:]
    return ' '.join(S)

#Task 2
def charFreq(string):
    s = set(string) #unique chars
    res = {x:0 for x in s}  
    for x in res.keys():
        res[x] = string.count(x) #counting
    return res    

#Task 3
def sliceStr(string):
    if len(string) < 2: #if length < 2 - empty str
        return ''
    return string[:2] + string[-2:] #else first & last 2 chars

#Task 4
def countStr(List):
    counter = 0
    for s in List:
        if len(s) >= 2 and s[0] == s[-1]:
            counter += 1
    return counter

#Task 5
def subSet(set1, set2, set3):
    return (set3.issubset(set1) and set3.issubset(set2))

#Task 6
def makeDict(num):
    return {x:x*x for x in range(1, num+1)} #from 1 to num

#Task 7
def mergeDict(dict1, dict2):
    return {**dict1, **dict2} #unzip dictionaries

#Task 8
def highestVals(d):
    maximums = []
    vals = list(d.values())
    for i in range(3):
        maximums.append(max(vals))
        vals.remove(max(vals))
        if not vals: break #if empty
    return maximums

#Task 9
def unique(List):
    return list(set(List)) #set consist only unique elements

#Task 10
def diffOfLists(List1, List2):
    return set(List1) - set(List2) | set(List2) - set(List1)
