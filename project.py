"""
This is the code for our Semester Project, Modular Arithmetic on very large numbers
We have divided the work into several files, each done by a member of our team
"""
#from addition import *
#from subtraction import *
#from multiply import *

def input_validity(a, b, c):
	if(c == "0"):
		print("Invalid value of c. Program is exiting")
		exit()

def toBinary(x):
	"""
	The function below converts a number to its Binary form
	It uses and operator (&) and right shift operator (>>)
	and returns a string containing the binary in a string
	Logic used from a code from StackOverflow
	"""
	number = int(x)
	binary = ""

	# bit_length() returns size of binary representation of number
	for m in range(number.bit_length()):
		
		# >> right shifts m times, dividing number by 2^m
		# & operation does and operation on bit representation of number >> m and 1
		# This will return the remainder when number is divided by 2^m
		if((number >> m) & 1):
			binary = "1" + binary
		else:
			binary = "0" + binary
	return binary

def toDecimal(a_bin):
	a_bin = a_bin[::-1]
	count = 0
	a_dec = "0"
	for i in a_bin:
		if(i == "1"):
			a_dec = add(a_dec, power("2", str(count)))
		count += 1
	return a_dec

def simplest_form(a):
	if(a[0] == "-"):
		while(a[1] == "0" and len(a) >= 2):
			if(a == "-0"):
				a = "0"
				break
			if(a[1] == "0"):
				a = a[0] + a[2:]
	else:
		while(len(a) > 1 and a[0] == "0"):
			a = a[1:]
	return a

def isGreater(a, b):
    if(a[0] == "-" and b[0] != "-"):
        return False
    elif(a[0] != "-" and b[0] == "-"):
        return True
    elif(a[0] == "-" and b[0] == "-"):
        return not isGreater(a[1 : ], b[1 :])
    else:
        if(len(a) > len(b)):
            return True
        elif(len(b) > len(a)):
            return False
        else:
            i = 0
            while(i < len(a)):
                if(a[i] > b[i]):
                    return True
                elif(a[i] < b[i]):
                    return False
                
                if(i == len(a) - 1 and a[i] == b[i]):
                    return False
                i += 1

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

def subtract(a, b):

	"""
	This function returns the difference of a and b (very large numbers stored in string)
	
	It reverses a and b and subtracts them using the ordinary method.

	Time Complexity = O(n) where n is the number of digits in a and b
	assuming a and b have same order of number of digits. 
	It can also be written as: 
	Time complexity = O(max(log a, log b)) where log is taken in base 10
	"""
	
	a = simplest_form(a)
	b = simplest_form(b)
	
	# For finding whether difference is positive or negative
	flag = 0
	if(isGreater(b, a)):
		flag  = 1

	# Reversing a and b
	a = a[::-1]
	b = b[::-1]

	# For iterating through the loop
	iter_time = max(len(a), len(b))

	# String because int cannot have numbers with size > 64 bit
	diff = ""
	borrow = 0

	# Subtraction takes place here
	for i in range(iter_time):

		# Number at (i + 1)th place of a when a is reversed
		x = 0
		if(i < len(a)):
			x = int(a[i])

		# Number at (i + 1)th place of b when b is reversed
		y = 0
		if(i < len(b)):
			y = int(b[i])

		# Finding difference when it is positive
		if(flag == 0):
			if(x >= y):
				if(borrow == -1 and x == y):
					d = 10 + x + borrow - y
				else:
					d = x + borrow - y
					borrow = 0
			else:
				d = (10 + x) + borrow - y
				borrow = -1
			diff = str(d) + diff

		# Finding difference when it is negative
		else:
			if(y >= x):
				if(borrow == -1 and y == x):
					d = 10 + y + borrow - x
				else:
					d = y + borrow - x
					borrow = 0
			else:
				d = (10 + y) + borrow - x
				borrow = -1
			diff = str(d) + diff

	# Adding a - sign before number if difference is negative
	if(flag == 1):
		diff = "-" + diff

	# Removes all excess zero before the number
	diff = simplest_form(diff)

	# returning the difference (including - sign if negative)
	return diff

def modulo_division(a, b):
    """
    This function uses long division method (the pen and paper version of division)
    to find the quotient and the mod
    """

    # Q stores Quotient and R stores mod
    Q = ""
    R = ""

    i = len(b)

    # An n-digit number can't be a factor of a number with less than n digits
    divisor = a[ : i]

    # Checks if the divisor was smaller. Adds another number to divisor
    if(isGreater(b, divisor) and i < len(a)):
        divisor += a[i]
        i += 1

    # Just a loop variable that will identify when the loop stops
    flag = 0

    while(flag == 0):

        # Used for finding quotient
        count = 0

        # Does repeated subtraction of divisor and b 
        while(isGreater(divisor, b) or divisor == b):
            count += 1
            divisor = minus(divisor, b)
        if(divisor[0] == "-"):
            break
        Q += str(count)
        # The next digit from a will be added to divisor if it exists
        if(i < len(a)):
            divisor += a[i]
            divisor = simplest_form(divisor)
            i += 1
        else:
            # flag = 1 when there are no more digits in a
            flag = 1

    R = str(divisor)

    # simplest_form deals with -0 or 00xx form of numbers 
    return simplest_form(Q), simplest_form(R)

def times(a, b):
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
		return simplest_form(str(int(a) * int(b)))

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
	return simplest_form(product)

def power_two1(a, b, c):
	i = "1"
	while(isGreater(b, i)):
		a = mod_times(a, a, c)
		i = times(i, "2")
	return a

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

def minus(a, b):
	"""
	This function handles any wrong input and tries to correct it and subtracts the two numbers
	It calls subtract(a, b) for subtraction
	"""
	# Trimming additional zeroes from the beginning, if present
	a = simplest_form(a)
	b = simplest_form(b)
	
	if(a[0] == "-" and b[0] == "-"):
		return simplest_form(subtract(b[1:], a[1:]))
	elif(a[0] == "-"):
		return simplest_form("-" + add(a[1:], b))
	elif(b[0] == "-"):
		return simplest_form(add(a, b[1:]))
	else:
		return simplest_form(subtract(a, b))

def mod(a, b):
	"""
	This function calls modulo_division function which returns the modulo
	The following code handles the positive and negative integers appropriately
	"""

	a = simplest_form(a)
	b = simplest_form(b)
	if(b == "0"):
		return "Error: b is 0"
	elif(b == "1"):
		return "0"
	elif(a[0] == "-" and b[0] != "-"):
		rem = modulo_division(a[1 : ], b)[1]
		if(rem == "0"):
			return rem
		else:
			return minus(b, rem)
	elif(a[0] != "-" and b[0] == "-"):
		rem = modulo_division(a, b[1 : ])[1]
		if(rem == "0"):
			return rem
		else:
			return add(b, rem)
	elif(a[0] == "-" and b[0] == "-"):
		rem = modulo_division(a[1 : ], b[1 : ])[1]
		if(rem == "0"):
			return rem
		else:
			return "-" + modulo_division(a[1 : ], b[1 : ])[1]
	else:
		return modulo_division(a, b)[1]

def mod_add(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	input_validity(a, b, c)

	return mod(add(mod(a, c) , mod(b, c)), c)

def mod_times(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	input_validity(a, b, c)

	return mod(times(mod(a, c), mod(b, c)), c)

def mod_minus(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	input_validity(a, b, c)

	return mod(minus(mod(a, c), mod(b, c)), c)

def power(a, b, c):
	a = simplest_form(a)
	b = simplest_form(b)
	c = simplest_form(c)

	# Checks if c is not zero
	input_validity(a, b, c)

	b_bin = toBinary(b)
	count = len(b_bin) - 1
	prod = "1"
	
	for i in b_bin:
		if(i == "1"):
			prod = times(mod(prod, c), mod(power_two1(a, str(2 ** count), c), c))
		count -= 1
		if(count == -1):
			break
	prod = mod(prod, c)
	return simplest_form(prod)

def division(a, b, c):
    input_validity(a, b, c)
	# Get quotient of a / b
    quotient = modulo_division(a, b)[0]

	# Receive the final answer by repeatedly subtracting c from the quotient
    quotient = modulo_division(quotient, c)[1]
    return quotient

number_file = open("numbers.txt", "r")

# Taking operation, a, b and c as inputs and removing \n from the end of a, b and c

operation = number_file.readline()
operation = operation[:-1]
a = number_file.readline()
a = a[:-1]
b = number_file.readline()
b = b[:-1]
c = number_file.readline()

number_file.close()


if(operation == "+"):
	print(mod_add(a, b, c))
elif(operation == "-"):
	print(mod_minus(a, b, c))
elif(operation == "*"):
	print(mod_times(a, b, c))
elif(operation == "-"):
	print(mod_minus(a, b, c))
elif(operation == "/"):
	print(division(b,a, c))
elif(operation == "^"):
	print(power(a, b, c))
else:
	print("Invalid Input")
