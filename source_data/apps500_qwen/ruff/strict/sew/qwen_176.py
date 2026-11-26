# Read input from standard input
A, B, C = map(int, input().split())

# Calculate all possible sums by arranging the panels
possible_sums = [
    (A * 10) + B + C,
    (A * 10) + C + B,
    (B * 10) + A + C,
    (B * 10) + C + A,
    (C * 10) + A + B,
    (C * 10) + B + A,
]

# Find the maximum possible sum
max_sum = max(possible_sums)

# Print the maximum possible amount of the allowance
print(max_sum)
