import sys
from math import factorial

# Read input
input = sys.stdin.read
data = input().split()

# Number of fragments
n = int(data[0])

# List of factorials
k = [int(data[i + 1]) for i in range(n)]

# Function to find the lowest prime divisor


def lowest_prime_divisor(x):
    if x % 2 == 0:
        return 2
    return next(
        (i for i in range(3, 1 + int(x**0.5), 2) if x % i == 0),
        x if x > 2 else 1,
    )


# Function to find the distance from a node to the root


def distance_to_root(node):
    distance = 0
    while node > 1:
        distance += 1
        node //= lowest_prime_divisor(node)
    return distance


# Calculate the total distance
total_distance = sum(distance_to_root(factorial(k[i])) for i in range(n))

# Output the result
print(total_distance)
