# Question 1

"""Write a function that takes in a function cond
and a number n and prints numbers from 1 to n where
calling cond on that number returns True.
"""

def keep_ints(cond, n):
	""" Print out all integers 1..i..n where cond(i) is true.
	>>> def is_even(x):
			return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	k = 1
	while k <= n:
		if cond(k):
			print(k)
		k += 1


# Question 2

"""
Write a function similar to keep_ints like before,
but now it takes in a number n and returns a function
that has one parameter cond. The returned functio
prints out numbers from 1 to n where calling cond on
that number returns True.
"""

def make_keeper(n):
	""" Returns a function which takes one parameter cond and prints
	out all integers 1..i..n where calling cond(i) returns True. 

	>>> def is_even(x)L
			return x % 2 == 0
	>>> make_keeper(5)(is_even)
	2
	4
	"""

	def pred(cond):
		i = 1
		while i <= n:
			if cond(i):
				print(i)
			i += 1
	return pred


# Question 3

""" Write the following function as a lambda

def curry2(h):
	def f(x):
		def g(y):
			return h(x,y):
		return g
	return f
"""

lamb_curry = lambda h: lambda x: lambda y: h(x, y)



# Question 4

""" 
Write a function print delayed delays printing its argument until the next
function call. print delayed takes in an argument x and returns a new function delay print. When delay print is called, it prints out x and returns
another delay print.
"""
def print_delayed(x):
	""" Return a new function. this new function, when called,
	will print out x and return another function with the same
	behavior.
	>>> f = print_delayed(1)
	>>> f = f(2)
	1
	>>> f = f(3)
	2
	>>> f = f(4)(5)
	3
	4
	>>> f("hi")
	5
	"""
	def delay_print(y):
		print(x)
		return print_delayed(y)
	return delay_print

# Question 5

"""
Tutorial: Write a function print n that can take in
an integer n and returns a repeatable print function
that can print the next n parameters. After the
nth parameter, it just prints ”done”.
"""

def print_n(n):
	
	"""
	>>> f = print_n(2)
	>>> f = f("hi")
	hi
	>>> f = f("hello")
	hello
	>>> f = f("bye")
	done
	>>> g = print_n(1)
	>>> g("first")("second")("third")
	first
	done
	done
	<function inner_print>
	"""
	def inner_print(x):
		if n <= 0:
			print("done")
		else:
			print(x)
		return print_n(n-1)
	return inner_print