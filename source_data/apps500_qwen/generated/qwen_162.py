import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the maximum number of groups of three or more students
groups_of_three_or_more = N // 3

# Print the result
print(groups_of_three_or_more)
