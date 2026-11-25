import sys

# Read input from standard input
C = sys.stdin.read().strip()

# Calculate the next letter in alphabetical order
next_letter = chr(1 + ord(C))

# Print the next letter
print(next_letter)
