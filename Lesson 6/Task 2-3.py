from itertools import zip_longest


# Task 2
PublicAttr = [x for x in list.__dict__.keys() if x[0] != '_']
print(PublicAttr)  # Public attributes of list


# Task 3
keys = [1, 2, 3, 4]
vals = ['a', 'b', 'c']
dicts = {x:y for (x,y) in zip_longest(keys, vals[:len(keys)])}
print(dicts)
