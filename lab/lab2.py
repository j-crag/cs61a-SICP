  # """
# What Would Python Display?
# Q1: WWPD: Lambda the Free
# """

#  lambda x: x  # A lambda expression with one parameter x

#  # function
# ______

#  a = lambda x: x  # Assigning the lambda function to the name a
#  a(5)

#  # 5
# ______

#  (lambda: 3)()  # Using a lambda expression as an operator in a call exp

#  # 3
# ______

#  b = lambda x: lambda: x  # Lambdas can return other lambdas!
#  c = b(88)
#  c

#  # function
# ______

#  c()

#  # 88
# ______

#  d = lambda f: f(4)  # They can have functions as arguments as well.
#  def square(x):
#      return x * x
#  d(square)

#  # 16

# ______

#  x = None # remember to review the rules of WWPD given above!
#  x
#  lambda x: x

#  # function, but if function is called, results in TypeError, 'NoneType' obj not callable
# ______
#  z = 3
#  e = lambda x: lambda y: lambda: x + y + z
#  e(0)(1)()

#  # 4: initail call returns a lambda that calls on y = 1, which returns
#  # a lambda that calls on x --> 0 + y --> 1 + z --> 3 from first global frame

# ______

#  f = lambda z: x + z
#  f(3)

#  # error --> TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# ______

#  higher_order_lambda = lambda f: lambda x: f(x)
#  g = lambda x: x * x

#  # results in TypeError: 'int' obj is not callable
#  higher_order_lambda(2)(g)  # Which argument belongs to which function call?

#  # THIS ONE ========>>> !!
#  higher_order_lambda(g)(2)
# ______

#  call_thrice = lambda f: lambda x: f(f(f(x)))
#  call_thrice(lambda y: y + 1)(0)
#  # 3
# ______

#  print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
#  print_lambda

#  # function
# ______

#  one_thousand = print_lambda(1000)
#  # 1000
# ______

#  one_thousand
#  # None
# ______


# ##########################################

# """
# Q2: WWPD: Higher Order Functions
# """

def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd

steven = lambda x: x

stewart = even(steven)

stewart

stewart(61)

stewart(-4)

def cake():
   print('beets')
   def pie():
       print('sweets')
       return 'cake'
   return pie

chocolate = cake()
#calls cake, which prints 'beets' and defined fn pie. pie is returned to
# and saved as 'chocolate' and has not yet been called. 


chocolate
# uncalled function pie


chocolate()
# call to pie

more_chocolate, more_cake = chocolate(), cake
# prints 'beets', returns func pie to more_chocolate; more_cake points to cake


more_chocolate
# 'cake'

def snake(x, y):
   if cake == more_cake:
       return chocolate
   else:
       return x + y

snake(10, 20)
# cake == more_cake, so snake(10,20) executes and returns chocolate
 


snake(10, 20)()
# call on return value calls func chocolate, which prints sweets and returns 'cake'


cake = 'cake'
snake(10, 20)

#cake == more_cake is fale, so returns 30

#####################################################
"""
Q3: Lambdas and Currying
"""

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    def f(x):
    	def g(y):
    		return func(x,y)
    	return g 
    return f  


####################################################

"""
Q4: Count van Count
Consider the following implementations of count_factors and count_primes:
"""

def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i, count = 1, 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n

"""
The implementations look quite similar!
Generalize this logic by writing a function count_cond,
which takes in a two-argument predicate function condition(n, i).
count_cond returns a one-argument function that takes in n, which counts
all the numbers from 1 to n that satisfy condition when called.
"""

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def counter(n):
    	i, count = 1, 0
    	while i < n:
    		if condition(i, n):
    			count += 1
    		i += 1
    	return count 
    return counter 


#######################################

n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)