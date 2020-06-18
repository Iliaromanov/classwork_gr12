
def bunnyEars(n: int) -> int:
    """We have a number of bunnies and each bunny has two big
    floppy ears. We want to compute the total number of ears
    across all the bunnies recursively
    (without loops or multiplication).

    bunnyEars(0) → 0
    bunnyEars(1) → 2
    bunnyEars(2) → 4
    """
    
    if n == 0:
        return 0

    return 2 + bunnyEars(n - 1)


def factorial(n: int) -> int:
    """
    Given n of 1 or more, return the factorial of n, 
    which is n * (n-1) * (n-2) ... 1. 
    Compute the result recursively (without loops).

    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    The fibonacci sequence is a famous bit of mathematics,
    and it happens to have a recursive definition.
    The first two values in the sequence are 0 and 1
    (essentially 2 base cases). Each subsequent value 
    is the sum of the previous two values, so the whole
    sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. 
    
    Define a recursive fibonacci(n) method that returns the 
    nth fibonacci number, with n=0 representing the start of 
    the sequence.

    fibonacci(0) → 0
    fibonacci(1) → 1
    fibonacci(2) → 1
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
