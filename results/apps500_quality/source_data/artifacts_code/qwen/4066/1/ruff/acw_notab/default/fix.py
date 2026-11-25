import sys
from math import gcd

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
a = list(map(int, data[1:]))

# Initialize minimum LCM and corresponding indices
min_lcm = float('inf')
min_indices = (0, 0)

# Iterate through all pairs (i, j) with i < j
for i in range(n):
    for j in range(i + 1, n):
        lcm = (a[j] * a[i]) // gcd(a[i], a[j])
        if lcm < min_lcm:
            min_lcm = lcm
            min_indices = (i + 1, 1 + j)

# Output the result
print(min_indices[0], min_indices[1])
