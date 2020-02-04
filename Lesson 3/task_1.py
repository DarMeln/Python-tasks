"""Functions: Task 1"""


def sqr_of_elements(array):
    """Counting square of list's elements"""
    return list(map(lambda x: x*x, array))  # Array will stay the same


def even_index(array):
    """Returning elements on even positions"""
    return list(array[::2])


def coubs(array):
    """Counting coubs of even elements on odd positions"""
    tmp = list(array[1::2])  # Odd position
    tmp = list(filter(lambda x: x % 2 == 0, tmp))  # Even elements
    return list(map(lambda x: x**3, tmp))  # Coub
