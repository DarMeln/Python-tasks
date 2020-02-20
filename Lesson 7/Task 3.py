args = []

def carry(func):
    def f(arg):
        args.append(arg)
        if len(args) == func.__code__.co_argcount:
            res = func(*args)
            return res
        else:
            return carry(func)
    return f


@carry
def foo(a, b):
    return a + b

print(foo(1)(5))
