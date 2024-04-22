def fibonacci(count:int):
    '''
    This module creates first $count fibonacci numbers.

    Arguments:
    count - count of fibonacci numbers you want to generate.

    Output:
    Array - array of fibonacci numbers.
    boolean value - False if failed.
    '''

    numbers = []
    
    if count == 1: numbers = [0]
    elif count == 2: numbers = [0, 1]
    else:
        numbers = [0, 1]
        for i in range(count-2):
            numbers.append(numbers[-2] + numbers[-1])

    return numbers