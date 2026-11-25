import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

# Initialize the number of ways to paint the first ball
ways = K

# Initialize the number of ways to paint the second ball
if N > 1:
    ways *= (K - 1)

# Print the result
print(ways)
