"""Functions: Task 2"""


def multiply_and_sum(*args):
    """Takes different types of arguments

    Returns multiplication and sum of nonzero elements
    """
    res = []
    for elem in args:
        if isinstance(elem, dict):  # Adding values of dict
            res.extend(list(elem.values()))
        elif isinstance(elem, int):  # Adding numbers
            res.append(elem)
        else:
            if cycl_ref_check(elem):
                print('Circular reference found')
                return None
            res.extend(elem)  # If no circular refs - extend the result list
    res = list(filter(lambda x: x > 0, res))  # Nonzero numbers only
    prod = 1
    for i in res:  # Counting multiplication
        prod *= i
    return sum(res), prod


def cycl_ref_check(arr):
    """Checking for circular reference"""
    for i in arr:
        if isinstance(i, list):
            return 1
    return 0
