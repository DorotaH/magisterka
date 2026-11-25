# Read input
x1, x2, x3 = map(int, input().split())

# Sort the coordinates to simplify finding the median
x1, x2, x3 = sorted([x1, x2, x3])

# The optimal meeting point is the median of the three coordinates
meeting_point = x2

# Calculate the total distance traveled
total_distance = abs(x3 - meeting_point) + abs(x1 - meeting_point)

# Print the result
print(total_distance)
