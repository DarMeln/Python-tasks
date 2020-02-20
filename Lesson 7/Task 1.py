from time import sleep

t=[]
def average_time(n=2):
    def outer_wrapper(func):
        def wrapper(*args):
            ans = func(*args)
            t.append(*args)
            if len(t) < n:
                res = (sum(t) / len(t)) * 1000
            else:
                res = (sum(t[-(n):]) / n) * 1000
            print("Среднее время работы: " + str(int(res)) + " мс")
            return ans
        return wrapper
    return outer_wrapper


@average_time(n=2)
def foo(a):
    sleep(a)
    return a

res = foo(3)
foo(7)
foo(1)
