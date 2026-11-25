import sys

# Read input from standard input
A, B = map(int, sys.stdin.readline().split())

# Calculate the starting time of the contest
starting_time = (B + A) % 24

# Print the result
print(starting_time)
