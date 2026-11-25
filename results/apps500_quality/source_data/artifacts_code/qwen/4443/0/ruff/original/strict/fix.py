import sys

# Read input from standard input
C = sys.stdin.read().strip()

# Calculate the next letter in alphabetical order
next_letter = chr(ord(C) + 1)

# Print the next letter
print(next_letter)
