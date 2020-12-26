"""
Q1: Num eights
Write a recursive function num_eights that takes a positive integer x
and returns the number of times the digit 8 appears in x. 
Use recursion, no assignment statments.
"""
# def num_eights(n):
# 	if n == 8:
# 		return 1
# 	elif n // 10 % 10 == 8:
# 		return 1 + num_eights(n // 10)
# 	else: 
# 		return num_eights(n // 10)


def num_eights(n):
	"""Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
	"""
	if n < 8:
		return 0
	elif n == 8:
		return 1
	elif n % 10 == 8:
		return 1 + num_eights(n // 10)
	else:
		return num_eights(n // 10)


"""
Q2: Ping-pong
The ping-pong sequence counts up starting from 1 and is always either counting up or counting down.
At element k, the direction switches if k is a multiple of 8 or contains the digit 8. 
The first 30 elements of the ping-pong sequence are listed below,
with direction swaps marked using brackets at the 8th, 16th, 18th, 24th, and 28th elements:

Index	1	2	3	4	5	6	7	[8]	9	10	11	12	13	14	15	[16]	17	[18]	19	20	21	22	23
PingPong Value	1	2	3	4	5	6	7	[8]	7	6	5	4	3	2	1	[0]	1	[2]	1	0	-1	-2	-3
Index (cont.)	[24]	25	26	27	[28]	29	30
PingPong Value	[-4]	-3	-2	-1	[0]	-1	-2
Implement a function pingpong that returns the nth element of the ping-pong sequence without using any assignment statements.

You may use the function num_eights, which you defined in the previous question.

Use recursion - the tests will fail if you use any assignment statements.
"""

def pingpong(n):
	if num_eights(n) or n % 8 == 0:
		increment(n)
	else:
		decrement(n)

def increment(n):
	return 1 + pingpong(n)

def decrement(n):
	return pingpong(n) - 1
















