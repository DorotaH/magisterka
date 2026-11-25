import sys
input = sys.stdin.read
from collections import defaultdict

# Read input
data = input().split()
N = int(data[0])
Q = int(data[1])

# Initialize data structures
A = [int(data[2 + i * 2]) for i in range(N)]
B = [int(data[3 + i * 2]) for i in range(N)]
C = [int(data[4 + i * 2]) for i in range(Q)]
D = [int(data[5 + i * 2]) for i in range(Q)]

# Dictionary to store the highest rating in each kindergarten
kindergartens = defaultdict(int)

# Initialize the kindergartens dictionary with the initial ratings
for i in range(N):
	kindergartens[B[i]] = max(kindergartens[B[i]], A[i])

# Function to update the kindergartens dictionary after a transfer


def update_kindergartens(c, d):
	kindergartens[C[c]] = max(kindergartens[C[c]], A[c])  # Remove the old rating
	kindergartens[D[d]] = max(kindergartens[D[d]], A[c])  # Add the new rating


# Output the evenness after each transfer
for q in range(Q):
	update_kindergartens(q, q)
	print(min(kindergartens.values()))
