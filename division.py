from project import *

def division(a, b, c):
    """
    This function uses modulo_division function for computation
    """
    input_validity(a, b, c)
	
    # Get quotient of a / b
    quotient = modulo_division(a, b)[0]

	# Receive the final answer by repeatedly subtracting c from the quotient
    quotient = modulo_division(quotient, c)[1]
    return quotient