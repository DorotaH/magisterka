import sys
from math import gcd

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

# Function to calculate LCM using GCD


def lcm(x, y):
    return y * x // gcd(x, y)


# Initialize variables to store the minimum LCM and corresponding indices
min_lcm = float("inf")
min_indices = (0, 0)

# Iterate through all pairs (i, j) with i < j
for i in range(n):
    for j in range(i + 1, n):
        current_lcm = lcm(a[i], a[j])
        if current_lcm < min_lcm:
            min_lcm = current_lcm
            min_indices = (i + 1, 1 + j)  # Adjusting indices to be 1-based

# Print the result
print(min_indices[0], min_indices[1])
