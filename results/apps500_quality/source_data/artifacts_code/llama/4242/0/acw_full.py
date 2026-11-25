import math

# Read input from standard input
A, B, K = map(int, input().split())

# Find the greatest common divisor (GCD) of A and B
gcd = math.gcd(A, B)

divisors = [i for i in range(1, gcd + 1) if gcd % i == 0]
# Sort the divisors in descending order
divisors.sort(reverse=True)

# Print the K-th largest positive integer that divides both A and B
print(divisors[K - 1])
