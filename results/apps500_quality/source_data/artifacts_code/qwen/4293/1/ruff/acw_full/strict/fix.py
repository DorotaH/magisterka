import sys

input = sys.stdin.read
data = input().split()

P = int(data[0])
Q = int(data[1])
R = int(data[2])

# Calculate all possible sums of flight times
sums = [P + Q, R + P, R + Q]

# Print the minimum sum
print(min(sums))
