from project import *

def add_num(a, b):
	"""
	This function returns the sum of a and b (very large numbers stored in string)
	
	It reverses a and b and adds using the ordinary method. 
	
	Time Complexity = O(max(log a, log b)) where log is taken in base 10 or O(n)
	where n is number of digits in a and b (assuming both have nearly same digits)

	log a and log b denote the number of digits in a and b respectively
	"""

	# Reversing a and b
	a = a[::-1]
	b = b[::-1]

	# For iterating through the loop
	size = max(len(a), len(b))
	
	# String because int cannot have numbers with size > 64 bit
	sum = ""
	carry = 0
	
	# Addition takes place here
	for i in range(size):
		# Number at (i + 1)th place of a when a is reversed
		x = 0
		if(i < len(a)):
			x = int(a[i])
		# Number at (i + 1)th place of b when b is reversed
		y = 0
		if(i < len(b)):
			y = int(b[i])
		s = x + y + carry

		# Stores the last bit of s
		sum = str(s % 10) + sum

		carry = s // 10
	# To see if there was a carry in the final addition    
	if(carry != 0):
		sum = str(carry) + sum
	
	return sum

def add(a, b):
	a = simplest_form(a)
	b = simplest_form(b)
	if(a[0] == "-" and b[0] == "-"):
		return simplest_form(("-" + add(a[1:], b[1:])))
	elif(a[0] == "-"):
		return simplest_form( minus(b, a[1:]))
	elif(b[0] == "-"):
		return simplest_form(minus(a, b[1:]))
	else:
		return simplest_form(add_num(a, b))

def mod_add(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	input_validity(a, b, c)

	return mod(add(mod(a, c) , mod(b, c)), c)