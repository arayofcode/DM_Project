from addition import *
from subtraction import *

def multiply(a, b):
	"""
	This function takes two numbers a and b and returns their product using Karatsuba Multiplication method. 
	It takes the two numbers, divide them into two parts and recursively finds the product. 
	This uses Divide and Conquer strategy.

	Time Complexity = O(n^(log 3) where log is in base 2 which is nearly equal to O(n^1.59)
	"""

	# Base case
	if(len(a) <= 1 or len(b) <= 1):
		maximum = ""
		minimum = ""
		if(len(a) < len(b)):
			maximum = b
			minimum = a
		else:
			maximum = a
			minimum = b
		#return multiply(maximum, minimum)
		return str(int(a) * int(b))

  	m = max(len(a), len(b))
  	m2 = m // 2

 	a1 = a[ : -m2]
	a2 = a[-m2 : ]
	b1 = b[ : -m2]
	b2 = b[-m2 : ]
	if(a1 == ''):
		a1 = '0'
	if(a2 == ''):
		a2 = '0'
	if(b1 == ''):
		b1 = '0'
	if(b2 == ''):
		b2 = '0'

	s1 = str(times(a1, b1))
	s2 = str(times(a2, b2))
	s3 = str(times(add(a1, a2), add(b1, b2)))
	s4 = minus(s3, add(s2, s1))

	x = add((s1 + "0" * (2 * m2)), (s4 + "0" * m2))
	product = add(x , s2)
	return product

def times(a, b):
	"""
	This function calls the actual multiplication function and handles the negative cases
	"""
	if(a == "0" or b == "0"):
		return "0"
	if(a[0] == "-" and b[0] == "-"):
		return multiply(a[1:], b[1:])
	elif(a[0] == "-"):
		return "-" + multiply(a[1:], b)
	elif(b[0] == "-"):
		return "-" + multiply(a, b[1:])
	else:
		return multiply(a, b)

def mod_times(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	input_validity(a, b, c)

	return mod(times(mod(a, c), mod(b, c)), c)