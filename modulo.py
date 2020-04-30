from project import *

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
    print(divisor)
    # Just a loop variable that will identify when the loop stops
    flag = 0

    while(flag == 0):

        # Used for finding quotient
        count = 0

        # Does repeated subtraction of divisor and b 
        while(isGreater(divisor, b) or divisor == b):
            count += 1
            #print("here")
            divisor = minus(divisor, b)
        if(divisor[0] == "-"):
            break
        Q += str(count)
        print(Q)
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
        rem = modulo_division(a[1 : ], b)
        if(rem == "0"):
            return rem
        else:
            return minus(b, rem)
    elif(a[0] != "-" and b[0] == "-"):
        rem = modulo_division(a, b[1 : ])
        if(rem == "0"):
            return rem
        else:
            return add(b, rem)
    elif(a[0] == "-" and b[0] == "-"):
        rem = modulo_division(a[1 : ], b[1 : ])
        if(rem == "0"):
            return rem
        else:
            return "-" + modulo_division(a[1 : ], b[1 : ])
    else:
        return modulo_division(a, b)

print(mod("1550", "25"))