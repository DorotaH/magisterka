import sys

# Read input from standard input
A, B, C, D, E = map(int, sys.stdin.read().split())

# Calculate the earliest possible time for the last dish to be delivered
# by ordering the dishes in ascending order of their serving times
earliest_time = sum(sorted([A, B, C, D, E]), 0)

# Print the result
print(earliest_time)