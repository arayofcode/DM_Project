def power_two(a, b, c):
    """
    Fast modular exponentiation for power of 2, i.e., (a ^ (2^n))
    """
    if(b == 1):
        return a % c
    return (power_two(a, b // 2, c) * power_two(a, b // 2, c)) % c

def power(a, b, c):
    binary = bin(b)
    
b = 78255
print(bin(b))
