"""Functions: Task 3"""


maximum = [float('-inf')]


def max_and_average(num_1, num_2, num_3, num_4, maximum=maximum):
    """Counting average and finding maximums of all given numbers"""
    maximum[0] = max(maximum[0], max(num_1, num_2, num_3, num_4))
    return (num_1 + num_2 + num_3 + num_4) / 4, maximum[0]
