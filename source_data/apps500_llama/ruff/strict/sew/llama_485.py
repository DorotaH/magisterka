import sys

# Read input from standard input
A, B, H, M = map(int, input().split())

# Calculate the angle moved by the hour hand in radians
hour_angle = 30 * (H + M / 60)

# Calculate the angle moved by the minute hand in radians
minute_angle = 6 * M

# Calculate the difference in angles
angle_diff = abs(hour_angle - minute_angle)

# Calculate the distance between the two hands
distance = (A * angle_diff / (2 * 3.14159)) + (
    B * abs((hour_angle - minute_angle) % (2 * 3.14159))
)

# Print the result with 9 decimal places
print(f"{distance:.9f}")
