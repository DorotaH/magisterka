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

# Calculate the angle of the hour hand in radians
hour_angle = (30 * H + 0.5 * M) * (math.pi / 180)

# Calculate the angle of the minute hand in radians
minute_angle = (math.pi / 30) * M

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(B**2 + A**2 - 2 * A * B * math.cos(hour_angle - minute_angle))

# Print the result
print(f"{distance:.15f}")
