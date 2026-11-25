import sys

# Read the number of houses
N = int(sys.stdin.readline())

# Read the coordinates of the houses
houses = list(map(int, sys.stdin.readline().split()))

# Sort the houses in ascending order
houses.sort()

# Initialize the minimum and maximum distance
min_dist = max(houses) - min(houses)
max_dist = sum(abs(houses[0] - houses[-1]) * 2)

# Iterate over all possible starting points
for i in range(len(houses) - 1):
    # Calculate the current distance
    curr_dist = (houses[i] - min(houses)) + (max(houses) - houses[-1])

    # Update the minimum distance
    min_dist = min(min_dist, curr_dist)

# Print the minimum distance
print(min_dist)