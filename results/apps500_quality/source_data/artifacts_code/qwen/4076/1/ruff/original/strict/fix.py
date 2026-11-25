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

# Calculate the angles of the hour and minute hands in radians
angle_hour = (H * 360 + M * 30) * (math.pi / 180)
angle_minute = (M * 360) * (math.pi / 180)

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(angle_minute - angle_hour))

# Print the result
print(f"{distance:.10f}")
