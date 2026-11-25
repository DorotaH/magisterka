import math
import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
H = int(data[2])
M = int(data[3])

# Calculate the angles of the hour and minute hands
angle_hour = 30 * (H % 12) + 0.5 * M
angle_minute = 6 * M

# Calculate the difference in angles
angle_diff = abs(angle_hour - angle_minute)

# If the angle difference is more than 180 degrees, take the shorter arc
if 180 < angle_diff:
	angle_diff = 360 - angle_diff

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(B**2 + A**2 - 2 * A * B * math.cos(math.radians(angle_diff)))

# Print the distance
print(f"{distance:.15f}")
