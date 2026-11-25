import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse input
N = int(data[0])
d = list(map(int, data[1:]))

# Calculate the sum of health points restored
total_health_points = 0
for i in range(N):
    for j in range(i + 1, N):
        total_health_points += d[i] * d[j]

# Print the result
print(total_health_points)
