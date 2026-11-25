import math

# Read input from standard input
A, B, K = map(int, input().split())

# Find the greatest common divisor (GCD) of A and B
gcd = math.gcd(A, B)

# Initialize an empty list to store divisors of the GCD
divisors = list()

# Loop through all numbers from 1 to the GCD (inclusive)
for i in range(1, gcd + 1):
    # Check if the current number is a divisor of the GCD
    if gcd % i == 0:
        # Add the divisor to the list
        divisors.append(i)

# Sort the divisors in descending order
divisors.sort(reverse=True)

# Print the K-th largest positive integer that divides both A and B
print(divisors[K - 1])
