import sys

input = sys.stdin.read
data = input().split()

P, Q = int(data[0]), int(data[1])
R = int(data[2])

# Calculate all possible sums of flight times
sums = [P + Q, P + R, Q + R]

# Print the minimum sum
print(min(sums))
