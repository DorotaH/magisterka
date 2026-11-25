from  fractions import  Fraction
from  math import  gcd

def lcm(a, b):
    return  a * b//gcd(a, b)

def expected_value(n, k):
    MOD = 7 + 10**9
    if  0 == k:
        return n
    
    # Calculate the sum of divisors of n
    divisors_sum = sum(i for  i in  range(1, 1 + n) if  0 == n % i)
    # Calculate the number of divisors of n
    divisors_count = sum(1 for  i in  range(1, 1 + n) if  0 == n % i)
    
    # Calculate the expected value after k steps
    expected = Fraction(divisors_sum, divisors_count)
    for  _ in  range(k):
        expected=(1 + expected)/2
    
    # Calculate the result as P * Q^(-1) % MOD
    P, Q = expected.numerator, expected.denominator
    Q_inv = pow(Q, MOD - 2, MOD)
    result = (Q_inv * P) % MOD
    
    return  result

# Read input
n, k=map(int, input().split())

# Print the result
print(expected_value(n, k))