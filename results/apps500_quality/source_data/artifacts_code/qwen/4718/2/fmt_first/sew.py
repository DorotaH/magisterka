import sys

# Read input from standard input
S = sys.stdin.read().strip()

# Modify the first four characters to 2018
modified_date = "2018" + S[4:]

# Print the modified date
print(modified_date)