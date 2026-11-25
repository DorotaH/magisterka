# Read input
x1, x2, x3 = map(int, input().split())

# Sort the positions to simplify finding the median
x1, x2, x3 = sorted([x1, x2, x3])

# The optimal meeting point is the median of the three positions
optimal_meeting_point = x2

# Calculate the total distance to the optimal meeting point
total_distance = (optimal_meeting_point - x1) + (x3 - optimal_meeting_point)

# Print the result
print(total_distance)