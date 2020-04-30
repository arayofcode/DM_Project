from project import *

def power_two1(a, b, c):
	"""
    This function returns the 2^n th power of a number mod c
    """
	i = "1"
	while(isGreater(b, i)):
		a = mod_times(a, a, c)
		i = times(i, "2")
	return a


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