import sys

# Read input from standard input
X, Y, Z = map(int, sys.stdin.read().split())

# Calculate the maximum number of people that can sit on the seat
max_people = (X - Y) // (Y + 2 * Z) + 1

# Print the result
print(max_people)
