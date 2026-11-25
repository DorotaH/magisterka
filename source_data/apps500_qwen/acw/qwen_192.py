import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the number of possible passwords
num_passwords = N ** 3

# Print the result
print(num_passwords)
