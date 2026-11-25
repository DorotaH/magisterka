import sys
import math

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A, B = int(data[0]), int(data[1])
H, M = int(data[2]), int(data[3])

# Calculate the angles of the hour and minute hands in radians
angle_hour, angle_minute = (
    (H * 360 + M * 30) * (math.pi / 180),
    (M * 360) * (math.pi / 180),
)

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(A**2 + B**2 - (2 * A * B * math.cos(angle_minute - angle_hour)))

# Print the result
print(f"{distance:.10f}")
