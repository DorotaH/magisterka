import sys

# Read input from standard input
A, B, C = map(int, input().split())
K = int(input())

# Calculate the maximum sum for each possible value of K
max_sum = 0
for k in range(1, K+1):
    # Choose the value to double that maximizes the sum
    double_A = max(A * 2**k, max(B, C))
    double_B = max(B * 2**k, max(A, C))
    double_C = max(C * 2**k, max(A, B))

    # Update max_sum
    max_sum = max(max_sum, A + B + C * 2**k)
    max_sum = max(max_sum, A + B * 2**k + C)
    max_sum = max(max_sum, A * 2**k + B + C)

# Print the maximum sum
print(max_sum)
