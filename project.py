"""
This is the code for our Semester Project, Modular Arithmetic on very large numbers
We have divided the work into several files, each done by a member of our team
"""
from addition import *
from subtraction import *

number_file = open("numbers.txt", "r")

# Taking a, b and c as inputs and removing \n from the end of a, b and c
a = number_file.readline()
a = a[:-1]
b = number_file.readline()
b = b[:-1]
c = number_file.readline()
c = c[:-1]

number_file.close()


def add(a, b):
    """
    This function returns the sum of a and b (very large numbers stored in string)
    
    It reverses a and b and adds using the ordinary method. 
    
    Time Complexity = O(max(log a, log b)) where log is taken in base 10 or O(n)
    where n is number of digits in a and b (assuming both have nearly same digits)

    log a and log b denote the number of digits in a and b respectively
    """
    if(a[0] == "-" and b[0] == "-"):
        return ("-" + add(a[1:], b[1:]))
    elif(a[0] == "-"):
        return minus(b, a[1:])
    elif(b[0] == "-"):
        return minus(a, b[1:])
    # Reversing a and b
    a = a[::-1]
    b = b[::-1]

    # For iterating through the loop
    iter_time = max(len(a), len(b))
    
    # String because int cannot have numbers with size > 64 bit
    sum = ""
    carry = 0
    
    # Addition takes place here
    for i in range(iter_time):
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



def minus(a, b):
    """
    This function returns the difference of a and b (very large numbers stored in string)
    
    It reverses a and b and subtracts them using the ordinary method.

    Time Complexity = O(n) where n is the number of digits in a and b
    assuming a and b have same order of number of digits. 
    It can also be written as: 
    Time complexity = O(max(log a, log b)) where log is taken in base 10
    """
    if(a[0] == "-" and b[0] == "-"):
        return minus(b[1:], a[1:])
    elif(a[0] == "-"):
        return "-" + add(a[1:], b)
    elif(b[0] == "-"):
        return add(a, b[1:])
    # For finding whether difference is positive or negative
    flag = 0
    if(len(b) > len(a) or (len(b) == len(a) and int(b[0]) > int(a[0]))):
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
    if(diff[0] == "-"):
        while(int(diff[1]) == 0):
            if(len(diff) == 1):
                break
            diff = diff[0] + diff[2:]
    else:
        while(int(diff[0])== 0):
            if(len(diff) == 1):
                break
            diff = diff[1:]

    # returning the difference (including - sign if negative)
    return diff



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



def power_two(a, b):
    if(b == "0"):
        return "1"
    if(b == "1"):
        return a
    x = power_two(a, str(int(b) >> 1))
    return times(x, x)

def power(a, b):
    """
    This function returns a^b using fast exponentiation algorithm 
    It converts b into a binary number and uses it for exponentiation
    """ 

    # When a is 0
    if(a == "0"):
        if(b == "0"):
            # 0^0 is not defined
            return "Not Defined"
        else:
            # 0^n is 0
            return "0"
    if(a == "1"):
        return "1"
    if(b == "0"):
        return "1"
    if(b == "1"):
        return a

    b_bin = toBinary(b)
    count = len(b_bin) - 1
    sum = "1"
    for i in b_bin:
        if(i == "1"):
            sum = times(sum, power_two(a, str(2 ** count)))
        count -= 1
    return sum