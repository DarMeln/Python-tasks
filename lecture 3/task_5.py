def f():
    return min(list(map(float, input().split(sep=' '))), key=abs)
