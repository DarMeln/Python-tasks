# Task 4
def cycle(array):
    ind = 0
    while True:
        if ind == len(array):
            ind = 0
        ind += 1
        yield array[ind-1]

# Task 5
def chain(*args):
    for elem in args:
        for i in elem:
            yield i


# Examples
print('Cyclic iterator:')
arr = [1, 2, 3]
cyclic = cycle(arr)
for i in range(10):
    print(next(cyclic), end=' ')

print('\nChain:')
t = (4, 5, 6)
res = chain(arr, t)
while True:
    try:
        print(next(res), end=' ')
    except:
        break
