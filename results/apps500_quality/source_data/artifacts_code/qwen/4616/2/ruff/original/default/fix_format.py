import sys

# Read input from standard input
s = sys.stdin.readline().strip()

# Calculate the abbreviation
abbreviation = f"{s[0]}{len(s) - 2}{s[-1]}"

# Print the abbreviation
print(abbreviation)
