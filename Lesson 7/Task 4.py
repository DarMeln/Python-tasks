def to_the_type(func):
    def vars(*args):
        for (elem, i) in zip(args, range(len(args))):
            try:
                boo = isinstance(elem,
                                 func.__annotations__[func.__code__.co_varnames[i]])
                if not boo:
                    print("Warning: Wrong Type in argument ", i + 1)
            except:
                print("Error: No Annotation Found")
    return vars


@to_the_type
def foo(a: int, b: str):
    pass

foo(3, 5)
print('---------------')
foo(3.0, 5.0)
print('---------------')
foo(3, '5')
print('---------------')

@to_the_type
def foobar(a: int, b):
    pass

foobar(2, 2)
