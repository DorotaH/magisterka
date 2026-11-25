from math import gcd

# Read input
A, B = map(int, input().split())

# Calculate the greatest common divisor of A! and B!
result = gcd(A, B)

# Print the result
print(result)