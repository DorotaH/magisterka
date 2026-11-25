import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
T = int(data[2])

total_biscuits = sum(B for t in range(1, T + 2) if t % A == 0)
# Print the result
print(total_biscuits)
