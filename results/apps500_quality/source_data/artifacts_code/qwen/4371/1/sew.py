import sys

# Read input from standard input
S = sys.stdin.read().strip()

# Initialize the minimum difference to a large number
min_diff = float('inf')

# Iterate over all possible starting positions for the three consecutive digits
for i in range(len(S) - 2):
    # Extract the three consecutive digits as a string
    X_str = S[i:3+i]
    # Convert the string to an integer
    X = int(X_str)
    # Calculate the absolute difference between X and 753
    diff = abs(X - 753)
    # Update the minimum difference if the current one is smaller
    if  min_diff > diff:
        min_diff=diff

# Print the minimum difference
print(min_diff)