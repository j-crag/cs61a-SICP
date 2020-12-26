# Question 1
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    51 and 3 and 6 and 10 and 15
    

    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

############################
############################

""" Question 2
Write a function that takes three positive numbers as arguments
and returns the sum of the squares of the two smallest numbers.
Use only a single line for the body of the function.
"""
def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return (x**2 + y**2 + z**2) - max(x**2, y **2, z**2)

############################
############################

"""Question 3
Write a function that takes an integer n that is greater than 1
and returns the largest integer that is smaller than n and evenly
divides n.
"""
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factor = n - 1
    while n > 0:
        if n % factor == 0:
            return factor
        else: 
            factor -= 1

############################
############################

"""Question 4
Let's try to write a function that does the same thing as an if statement.
"""

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

"""
Despite the doctests above, this function actually does not do the same
thing as an if statement in all cases. To prove this fact,
write functions cond, true_func, and false_func such that with_if_statement
prints the number 47, but with_if_function prints both 42 and 47.
"""

def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    return False

def true_func():
    print(42)

def false_func():
    print(47)

###########################
###########################

"""Question 5
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach,
poses the following mathematical puzzle.

Pick a positive integer n as the start.
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Continue this process until n is 1.
The number n will travel up and down but eventually end at 1
(at least for all numbers that have ever been tried -- nobody 
has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down
in the atmosphere before eventually landing on earth.


This sequence of values of n is often called a Hailstone sequence.
Write a function that takes a single argument with formal parameter name n,
prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
"""

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    counter = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else: 
            n = n * 3 + 1
        counter = counter + 1
    print(n)
    return counter

