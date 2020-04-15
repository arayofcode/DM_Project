"""
procedure karatsuba(num1, num2)
  if (num1 < 10) or (num2 < 10)
    return num1*num2
    
  *calculates the size of the numbers*
  m = max(size_base10(num1), size_base10(num2))
  m2 = m/2
  
  *split the digit sequences about the middle*
  high1, low1 = split_at(num1, m2)
  high2, low2 = split_at(num2, m2)
  
  *3 calls made to numbers approximately half the size*
  z0 = karatsuba(low1, low2)
  z1 = karatsuba((low1 + high1), (low2 + high2))
  z2 = karatsuba(high1, high2)
  return (z2 * 10 ^ (2 * m2)) + ((z1 - z2 - z0) * 10 ^ (m2)) + (z0)
"""

from addition import *
from subtraction import *

def times(a, b):
	if(len(a) == 1 or len(b) == 1):
		return str(int(a) * int(b))
  
  	m = max(len(a), len(b))
  	m2 = m // 2

 	a1 = a[ : m2]
	a2 = a[m2 : ]
	b1 = b[ : m2]
	b2 = b[m2 : ]

	s1 = str(times(a1, b1))
	s2 = str(times(a2, b2))
	s3 = str(times(add(a1, a2), add(b1, b2)))
	s4 = minus(s3, add(s2, s1))

	x = add((s1 + "0" * m), (s4 + "0" * m2))
	product = add(x , s2)
	return product

print(times(str(1234), str(8765)))
