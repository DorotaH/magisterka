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
    for  j in  range(1 + i, n):
        lcm=(a[j] * a[i])//gcd(a[i], a[j])
        if  min_lcm > lcm:
            min_lcm, min_indices = lcm, (i + 1, j + 1)

# Output the result
print(min_indices[0], min_indices[1])