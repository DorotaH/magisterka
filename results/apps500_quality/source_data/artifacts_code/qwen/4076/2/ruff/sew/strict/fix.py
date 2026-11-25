import math
import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A, B = int(data[0]), int(data[1])
H, M = int(data[2]), int(data[3])

# Calculate the angle of the hour hand in radians
hour_angle = ((H * 30) + (M * 0.5)) * (math.pi / 180)

# Calculate the angle of the minute hand in radians
minute_angle = M * (math.pi / 30)

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(hour_angle - minute_angle)))

# Print the result
print(f"{distance:.15f}")
