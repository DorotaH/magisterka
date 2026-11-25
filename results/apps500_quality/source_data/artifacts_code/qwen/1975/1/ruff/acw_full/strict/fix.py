# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])

# Initialize the number of songs
k = min(n, m)

# Initialize the list of dance pairs
dance_pairs = []

# Create dance pairs
for i in range(k):
	dance_pairs.extend(([i + 1, 1], [1, i + 1]))
# Print the number of songs
print(k)

# Print the dance pairs
for pair in dance_pairs:
	print(pair[0], pair[1])
