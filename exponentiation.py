from multiply import *

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
