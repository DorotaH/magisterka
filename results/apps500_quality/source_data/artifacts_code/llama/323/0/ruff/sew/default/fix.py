import math

# Read input
A, B = map(int, input().split())

# Find the minimum between A and B
min_value = min(A, B)

# Initialize the greatest common divisor
gcd = 1

# Iterate from 1 to min_value (inclusive) to find the greatest common divisor
for i in range(1, min_value + 1):
    # If i is a divisor of both A! and B!, update the greatest common divisor
    if  0 == math.factorial(A) % i and  0 == math.factorial(B) % i:
        gcd=i

# Print the greatest common divisor
print(gcd)