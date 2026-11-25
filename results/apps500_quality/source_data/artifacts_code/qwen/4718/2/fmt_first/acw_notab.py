import sys

# Read input from standard input
S = sys.stdin.read().strip()

# Modify the first four characters to 2018
modified_date = S[4:] + "2018"

# Print the modified date
print(modified_date)
