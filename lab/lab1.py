# What would python display?

def xk(c, d):
     if c == 4:
         return 6
     elif d >= 4:
         return 6 + 7 + c
     else:
         return 25

a = xk(10, 10) # >> 23
b = xk(10, 6) # >> 23
c = xk(4, 6) # >> 6
d = xk(0, 0) # >> 25

##############################################

def how_big(x):
     if x > 10:
         print('huge')
     elif x > 5:
         return 'big'
     elif x > 0:
         print('small')
     else:
        print("nothin")
"""
how_big(7) # doesn't print, returns 'big'
how_big(12) # prints 'huge', returns None
how_big(1) # prints 'small', returns None
how_big(-1) # >> prints 'nothin', retruns None
"""

################################################
"""
n = 3
while n >= 0:
	n -= 1
	print(n) 
"""

""" 
2
1
0
-1
"""

################################################

# positive = 28
# while positive:
# 	print("positive?")
# 	positive -= 3
"""Results in an infinite loop. Although probably
not intended, the while statement still remains 'True'
even after 'positive' is bound to a negative value.
"""

#################################################

"""
positive = -9
negative = -12
while negative:
    if positive:
        print(negative)
    positive += 3
    negative += 3
"""

"""
-12
pos = -6, neg = -9
-9
pos = -3, neg = -6
-6
pos = 0, neg = -3
pos = 3, neg = 0
>>> -12, ,-9, -6
"""

################################################
"""
print(True and 13) # True
print(False or 0) # False
print(not 10) # False
print(non None) # True
print(True and 1 / 0 and False) # ZeroDivisionError: division by zero
print(True or 1 / 0 or False) # shot circuit to True
print(True and 0) # 0 
print(False or 1) # 1
print(1 and 3 and 6 and 10 and 15) # 15
print(-1 and 1 > 0) # True
print(0 or False or 2 or 1 / 0) # 2
print(not 0) # True
print((1 + 1) and 1) # 1
print(1/0 or True) # ZeroDivisionError: division by zero
print((True or False) and False) # False
"""

################################################


"""Let's write a function falling, which is a "falling" factorial
that takes two arguments, n and k, and returns the product of k
consecutive numbers, starting from n and working downwards.
"""

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total, curr_num, counter = 1, n, 1
    while counter <= k:
    	total, curr_num, counter = total * curr_num, curr_num - 1, counter + 1
    return total

###############################################

"""Write a function that takes in a nonnegative integer and sums its digits.
(Using floor division and modulo might be helpful here!)
"""

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    total = 0
    while y != 0:
    	last_digit = y % 10
    	total += last_digit
    	y = y // 10
    return total
"""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
"""

##############################################


def ab(c, d):
     if c > 5:
         print(c)
     elif c > 7:
         print(d)
     print('foo')

###############################################

def bake(cake, make):
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
         print(make)
     else:
         return cake
     return make

"""
bake(1, 'mashed potatoes') 
prints mashed potates, returns 'mashed potoates'

bake(0, 29)
prints 1, prints 29, returns 29
"""

##############################################
"""
Write a function that takes in a number and determines if
the digits contain two adjacent 8s.
"""

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n > 0:
    	last_digit = n % 10
    	next_digit = n // 10 % 10
    	if last_digit == next_digit:
    		return True
    	next_digit = last_digit
    	n = n // 10 
    return False

"""
prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False
"""

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    while n > 0:
      last = n % 10
      if last == n // 10 % 10:
        return True
      n = n // 10
    return False




    	


    
