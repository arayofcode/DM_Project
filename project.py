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

from subtraction import minus

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
