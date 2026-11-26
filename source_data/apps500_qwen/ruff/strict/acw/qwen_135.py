import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
T = int(data[2])

total_biscuits = sum(B for _ in range(1, 2 + T // A))
# Print the result
print(total_biscuits)
