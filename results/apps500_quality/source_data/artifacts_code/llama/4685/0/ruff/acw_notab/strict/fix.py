
# Read input from standard input
A, B, C = map(int, input().split())
K = int(input())

# Define a function to calculate the maximum sum


def max_sum(A, B, C, K):
    # Calculate the sum for each possible operation
    sum_A = A * (2 ** min(K, 6))
    sum_B = B * (2 ** min(K, 4))
    sum_C = (2 ** min(K, 5)) * C

    # Return the maximum sum
    return max(sum_A, sum_B, sum_C)


# Calculate and print the maximum sum
max_sum_value = max_sum(A, B, C, K)
print(max_sum_value)
