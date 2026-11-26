import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
a = list(map(int, data[1:]))

# Initialize variables to store the maximum combination and the corresponding pair
max_comb = 0
max_pair = (0, 0)

# Iterate through all pairs (a_i, a_j) with a_i > a_j
for i in range(n):
    for j in range(i + 1, n):
        comb = ((a[i] - 1) * a[i] // 2) // ((a[j] - 1) * a[j] // 2)
        if comb > max_comb:
            max_comb = comb
            max_pair = (a[i], a[j])

# Print the result
print(max_pair[0], max_pair[1])
