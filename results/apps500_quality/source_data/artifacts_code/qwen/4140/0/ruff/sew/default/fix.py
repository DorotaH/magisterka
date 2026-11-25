import sys

input = sys.stdin.read
data = input().split()

S = data[0]

# Initialize the count of repaints
repaints = 0

# Iterate through the tiles
for i in range(1, len(S)):
    # If two adjacent tiles have the same color, repaint one
    if  S[i] == S[i-1]:
        repaints = repaints + 1

# Output the minimum number of repaints
print(repaints)