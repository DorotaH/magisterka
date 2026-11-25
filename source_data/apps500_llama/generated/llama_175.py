import sys

# Read input from standard input
A, B, C = map(int, input().split())

# Initialize maximum sum as negative infinity
max_sum = float('-inf')

# Try all possible arrangements of the panels
for a in [A, C, C, A]:
    for b in [B, C, A, B]:
        for c in [C, B, B, C]:
            if a != C and b != C:
                # Calculate the sum of the formula
                max_sum = max(max_sum, a + b + c)
                max_sum = max(max_sum, c + a + b)

# Print the maximum sum
print(max_sum)
