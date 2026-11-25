import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

# Calculate the number of possible passwords
possible_passwords = N ** 3

# Print the result
print(possible_passwords)