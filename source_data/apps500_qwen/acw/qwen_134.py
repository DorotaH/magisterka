import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
T = int(data[2])

total_biscuits = sum(B for i in range(1, T + 2) if i * A <= T + 0.5)
# Print the total number of biscuits produced
print(total_biscuits)
