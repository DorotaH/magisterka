import sys

# Read input from standard input
N = int(sys.stdin.read())

# Initialize the sum of remainders
max_sum = 0

# The maximum possible value of M_i is min(i, P_i) - 1
# To maximize the sum, we should use the smallest possible P_i for each i
# This means we should use the permutation {1, 2, ..., N}
# For each i, M_i = min(i, i) - 1 = i - 1
# Therefore, the maximum possible value of M_1 + M_2 + ... + M_N is (N - 1) + (N - 2) + ... + 1 = N * (N - 1) // 2

max_sum = N * (N - 1) // 2

# Print the result
print(max_sum)