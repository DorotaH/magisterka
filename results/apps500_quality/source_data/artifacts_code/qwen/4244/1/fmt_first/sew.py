import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of people
N = int(data[0])

# Coordinates of the people
X = list(map(int, data[1:]))

# Sort the coordinates
X.sort()

# The optimal meeting point is the median
# This minimizes the sum of squared distances
optimal_point = X[N // 2]

# Calculate the total stamina
total_stamina = sum((x - optimal_point) ** 2 for x in X)

# Print the result
print(total_stamina)