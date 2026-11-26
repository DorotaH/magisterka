import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
T, X = int(data[0]), int(data[1])

# Calculate the time that will pass in World A
time_in_A = T / X

# Print the result
print(time_in_A)
