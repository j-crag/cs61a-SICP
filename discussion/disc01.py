# Question 1

def wears_jacket_with_if(temp, raining):
	"""
>>> wears_jacket_with_if(90, False)
False
>>> wears_jacket_with_if(40, False)
True
>>> wears_jacket_with_if(100, True)
True
	"""
	if temp < 60 or raining:
		return True
	else: 
		return False

def one_liner(temp, raining):
	"""
>>> wears_jacket_with_if(90, False)
False
>>> wears_jacket_with_if(40, False)
True
>>> wears_jacket_with_if(100, True)
True
	"""
	return temp < 60 or raining

##########################################

#Question 2

"""1.2 What is the result of evaluating the
following code?
"""
def square(x):
	print("here!")
	return x * x

def so_slow(num):
	x = num
	while x > 0:
		x = x + 1
	return x / 0

# Results in infinite loop, x will always be greater than 0

############################################

#question 3

"""
Write a function that returns True if a positive integer n is a prime
number and False otherwise.
"""

def is_prime(n):
	"""
>>> is_prime(10)
False
>>> is_prime(7)
True
	"""

def is_prime_2(n):
	if n == 1:
		return False
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True 






	
