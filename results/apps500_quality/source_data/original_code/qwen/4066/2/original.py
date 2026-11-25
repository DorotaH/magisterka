import sys

# Read input
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# Initialize variables
min_lcm = float('inf')
min_pair = (0, 0)

# Iterate through all pairs of indices (i, j)
for i in range(n):
    for j in range(i + 1, n):
        # Calculate the least common multiple of a[i] and a[j]
        lcm = (a[i] * a[j]) // gcd(a[i], a[j])
        # Update the minimum lcm and the corresponding pair
        if lcm < min_lcm:
            min_lcm = lcm
            min_pair = (i + 1, j + 1)

# Print the result
print(min_pair[0], min_pair[1])
