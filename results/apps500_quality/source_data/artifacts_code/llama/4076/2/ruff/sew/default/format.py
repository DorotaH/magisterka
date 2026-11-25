import math
import sys

# Read input
A, B, H, M = map(int, input().split())

# Calculate the angular velocity of the hour hand in radians per hour
hour_velocity = 2 * math.pi / 12

# Calculate the angular velocity of the minute hand in radians per minute
minute_velocity = 2 * math.pi / 60

# Calculate the angle of the hour hand after H hours and M minutes
hour_angle = (H + (M / 60)) * hour_velocity

# Calculate the angle of the minute hand after M minutes
minute_angle = minute_velocity * M

# Calculate the absolute difference between the two angles
angle_diff = abs(hour_angle - minute_angle)

# Calculate the distance between the two hands using the law of cosines
distance = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(angle_diff)))

# Print the result
print(f"{distance:.9f}")
