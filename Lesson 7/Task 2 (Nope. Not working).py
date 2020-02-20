from time import time, sleep

"""class time_methods:
    def __init__(self, *func):
        def init(cl):
            self.cl = cl
            self.func = func
        print(func)

    def __call__(self, meth):
        curr = time()
        def meth_check(*args, **kwargs):
            if hasattr(self.func, meth):
                res = self.func(*args, **kwargs)
            return res
    """

def time_methods(*meth):
    def cls(some_class):
        class another:
            def __init__(self, *args, **kwargs):
                self.instance = some_class(*args, **kwargs)

            def __call__(self):
                def call(*args, **kwargs):
                    curr = time()
                    print(curr)
                    def meth_check(*args, **kwargs):
                        if func in meth:
                            res = self.func(*args, **kwargs)
                            return res
    """
def time_methods(*meth):
    def cls(some_class):
        def init(*args, **kwargs):
            return some_class(*args, **kwargs)
        return init
    return cls"""
    
@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s
    def inspect(self):
        sleep(self.s)
    def foo(self):
        return self.s

a = Spam(2)
a.inspect()  #  должно вывести сообщение о времени работы
a.foo()  # ничего не выводить
