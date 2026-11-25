import sys

# Read input from standard input
A, B, C = map(int, input().split())
K = int(input())

# Function to calculate the sum of the integers on the blackboard after K operations
def max_sum(A, B, C, K):
    # Find the maximum value of the three numbers
    max_val = max(A, B, C)

    # The optimal strategy is to double the maximum value K times
    A_new, B_new, C_new = A, B, C
    for _ in range(K):
        A_new, B_new, C_new = max_val * 2, max_val * 2, max_val * 2

    # The sum of the integers on the blackboard after K operations is the sum of the three new values
    return A_new + B_new + C_new

# Calculate and print the result
result = max_sum(A, B, C, K)
print(result)
