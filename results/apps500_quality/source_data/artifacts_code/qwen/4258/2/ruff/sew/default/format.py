import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
T = int(data[2])

# Calculate the total number of biscuits produced within T + 0.5 seconds
total_biscuits = 0
for i in range(1, T // A + 2):
    total_biscuits += B

# Print the result
print(total_biscuits)
