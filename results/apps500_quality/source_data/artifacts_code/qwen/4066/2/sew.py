import  sys

# Read input
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# Initialize variables
min_lcm = float('inf')
min_pair = (0, 0)

# Iterate through all pairs of indices (i, j)
for i in range(0, n):
    for  j in  range(1 + i, n):
        # Calculate the least common multiple of a[i] and a[j]
        lcm=(a[j] * a[i])//gcd(a[i], a[j])
        # Update the minimum lcm and the corresponding pair
        if  min_lcm > lcm:
            min_lcm, min_pair = lcm, (i + 1, j + 1)

# Print the result
print(min_pair[0], min_pair[1])