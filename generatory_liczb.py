def fibonacci(count:int):
    '''
    This module generates first $count fibonacci numbers.

    Arguments:
    count - count of fibonacci numbers you want to generate.

    Output:
    array - array of fibonacci numbers.
    boolean value - False if failed.
    '''

    numbers = []
    try:
        if count == 1: numbers = [0]
        elif count == 2: numbers = [0, 1]
        else:
            numbers = [0, 1]
            for i in range(count-2):
                numbers.append(numbers[-2] + numbers[-1])

        return numbers
    
    except:
        print("An unexpected error happened.")
        return False


def isPrime(number):
    '''
    This module checks if the number is a prime number.

    Arguments:
    number - number you want to be checked.

    Output:
    boolean value - True if the number is a prime number, False if the number is not a prime number.
    '''

    if number > 1:
        for i in range(2, (number//2)+1):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def prime(count:int):
    '''
    This module generates first $count prime numbers.

    Arguments:
    count - count of prime numbers you want to generate.

    Output:
    array - array of first $count prime numbers.
    '''

    numbers = []
    i = 0

    while len(numbers) < count:
        if isPrime(i):
            numbers.append(i)
            i += 1
        else: i += 1

    return numbers


def isPerfect(number:int):
    
    """
    This module checks if the number is a perfect number.

    Arguments:
    Number you want to be checked.

    Output:
    boolean value - True if the number is a perfect number, False if the number is not a perfect number.
    """

    sum = 0
    for i in range(1, number):
        if(number % i == 0):
            sum = sum + i

    if sum == number:
        return True
    
    else:
        return False
    

def perfect(count:int, bypass=False):
    """
    This module generates first $count perfect numbers.
    The count limit is set to 4 due to severe lag generating more perfect numbers may cause, but you can bypass it.

    Arguments:
    count - count of perfect numbers you want to generate.

    Output:
    array - array of $count first perfect numbers.
    """
    
    if count > 4 and bypass==False:
        print("Due to severe lag it may cause, you can't enter a number above 4 unless you activate the bypass.")
    
    else:
        numbers = []
        i = 1

        while len(numbers) < count:
            if isPerfect(i): numbers.append(i)
            
            i += 1

        return numbers

print(perfect(5))