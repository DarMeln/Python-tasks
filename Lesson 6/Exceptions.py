def div():
    try:
        a, b = list(map(int, input()))
        print(a/b)
    except ZeroDivisionError as zero:
        print('Error code:', zero)
    except ValueError as val:
        print('Error code:', val)

