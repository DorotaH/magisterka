import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the maximum possible value of M_1 + M_2 + ... + M_N
# The maximum value of M_i is min(i, P_i) - 1, which is i - 1 when P_i = i
# Therefore, the maximum sum is the sum of the first N-1 natural numbers
max_sum = (N - 1) * N // 2

# Print the result
print(max_sum)