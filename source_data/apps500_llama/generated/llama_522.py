import math

# Read the input from standard input
N = int(input())

# The smallest number divisible by both 2 and N is the LCM of 2 and N
# The LCM of two numbers is calculated as (a * b) / GCD(a, b)
# where GCD is the Greatest Common Divisor
# In this case, GCD(2, N) is always 1 because 2 is a prime number
# Therefore, LCM(2, N) is simply 2 * N
result = 2 * N

print(result)
