import os
from typing import List


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


def bunnyEars2(n: int) -> int:
    """    
    We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
    bunnyEars2(0) → 0
    bunnyEars2(1) → 2
    bunnyEars2(2) → 5
    """

    if n == 0:
        return 0

    if n % 2 == 0:
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)
    
    
def triangle(n: int) -> int:
    """"
    We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.
    triangle(0) → 0
    triangle(1) → 1
    triangle(2) → 3
    """  

    if n == 0:
        return 0
    
    return n + triangle(n-1)


def sumDigits(n: int) -> int:
    """
    Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    sumDigits(126) → 9
    sumDigits(49) → 13
    sumDigits(12) → 3
    """

    if n < 10:
        return n

    return n % 10 + sumDigits(n // 10)


def count7(n: int) -> int:
    """
    Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    count7(717) → 2
    count7(7) → 1
    count7(123) → 0
    """

    if n < 10:
        if n == 7:
            return 1
        else:
            return 0    

    num = n % 10

    if num == 7:
        return 1 + count7(n // 10)
    else:
        return count7(n // 10)

    
def  count8(n: int) -> int:
    """
    Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    count8(8) → 1
    count8(818) → 2
    count8(8818) → 4
    """

    if n < 10:
        if n == 8:
            return 1
        else:
            return 0

    left = n // 10 % 10

    num = n % 10

    if num == 8 and left == 8:
        return 2 + count8(n // 10)
    elif num == 8:
        return 1 + count8(n // 10)
    else:
        return count8(n // 10)

    
def powerN(b: int, n: int) -> int:
    """
    Given <b>base</b> and <b>n</b> that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
    powerN(3, 1) → 3
    powerN(3, 2) → 9
    powerN(3, 3) → 27
    """        

    if n == 1:
        return b

    return b * powerN(b, n - 1)


def countX(string: str) -> int:
    """
    Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
    countX("xxhixx") → 4
    countX("xhixhix") → 3
    countX("hi") → 0
    """

    if len(string) <= 1:
        if string == 'x':
            return 1
        else:
            return 0

    if string[-1] == 'x':
        return 1 + countX(string[:len(string) - 1])
    else:
        return countX(string[:len(string) - 1])

    
def countHi(string: str) -> int:
    """
    Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
    countHi("xxhixx") → 1
    countHi("xhixhix") → 2
    countHi("hi") → 1
    """

    if len(string) <= 2:
        if string == 'hi':
            return 1
        else:
            return 0

    if string[-1] == 'i' and string[-2] == 'h':
        return 1 + countHi(string[:len(string) - 2])
    else:
        return countHi(string[:len(string) - 1])

    
def changeXY(string: str) -> str:
    """
    Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
    changeXY("codex") → "codey"
    changeXY("xxhixx") → "yyhiyy"
    changeXY("xhixhix") → "yhiyhiy"
    """

    if len(string) <= 1:
        if string == 'x':
            return 'y'
        else:
            return string

    if string[0] == 'x':
        return 'y' + changeXY(string[1:])
    else:
        return string[0] + changeXY(string[1:])

    
def changePi(string: str) -> str:
    """
    Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
    changePi("xpix") → "x3.14x"
    changePi("pipi") → "3.143.14"
    changePi("pip") → "3.14p"
    """

    if len(string) <= 2:
        if string == "pi":
            return "3.14"
        else:
            return string

    if string[0:2] == 'pi':
        return '3.14'+ changePi(string[2:])
    else:
        return string[0] + changePi(string[1:])

    
def noX(string: str) -> str:
    """
    Given a string, compute recursively a new string where all the 'x' chars have been removed.
    noX("xaxb") → "ab"
    noX("abc") → "abc"
    noX("xx") → ""
    """

    if len(string) <= 1:
        if string == 'x':
            return ''
        else:
            return string

    if string[0] == 'x':
        return '' + noX(string[1:])
    else:
        return string[0] + noX(string[1:])
    
    
def array6(nums: List[int], index: int) -> bool:
    """
    Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
    array6([1, 6, 4], 0) → true
    array6([1, 4], 0) → false
    array6([6], 0) → true
    """

    if len(nums) == 0:
            return False
    
    if nums[0] == 6:
        return True
    else:
        return array6(nums[1:], index + 1)
    
    
def array11(nums: List[int], index: int) -> int:
    """
    Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
    array11([1, 2, 11], 0) → 1
    array11([11, 11], 0) → 2
    array11([1, 2, 3, 4], 0) → 0
    """

    if len(nums) == 0:
        return 0

    if nums[0] == 11:
        return 1 + array11(nums[1:], index + 1)
    else:
        return array11(nums[1:], index + 1)
    
    
def array220(nums: List[int], index: int) -> bool:
    """
    Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
    array220([1, 2, 20], 0) → true
    array220([3, 30], 0) → true
    array220([3], 0) → false            
    """

    if len(nums) <= 1:
        return False

    if nums[1] == nums[0] * 10:
        return True
    else:
        return array220(nums[1:], index + 1)
    
    
def allStar(string: str) -> str:
    """
    Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
    allStar("hello") → "h*e*l*l*o"
    allStar("abc") → "a*b*c"
    allStar("ab") → "a*b"
    """

    if len(string) <= 1:
        return string

    return string[0] + '*' + allStar(string[1:])


def pairStar(string: str) -> str:
    """
    Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
    pairStar("hello") → "hel*lo"
    pairStar("xxyy") → "x*xy*y"
    pairStar("aaaa") → "a*a*a*a"
    """

    if len(string) <= 1:
        return string

    if string[0] == string[1]:
        return string[0] + '*' + pairStar(string[1:])
    else:
        return string[0] + pairStar(string[1:])
    
    
def endX(string: str) -> str:
    """
    Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.
    endX("xxre") → "rexx"
    endX("xxhixx") → "hixxxx"
    endX("xhixhix") → "hihixxx"
    """

    if len(string) <= 1:
        return string

    if string[0] == 'x':
        return endX(string[1:]) + 'x'
    else:
        return string[0] + endX(string[1:])
