import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

# Initialize the number of ways to paint the first ball
ways = K

# Initialize the number of ways to paint the second ball
ways *= K - 1

# For the remaining balls, each ball can be painted in any of the K-1 colors different from the previous ball
for _ in range(2, N):
    ways *= K - 1

print(ways)
