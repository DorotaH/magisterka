import sys
import math

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
A = int(data[0])
B = int(data[1])
H = int(data[2])
M = int(data[3])

# Calculate the angles of the hour and minute hands in radians
angle_hour = (360 * H + 30 * M) * (math.pi / 180)
angle_minute = (360 * M) * (math.pi / 180)

# Calculate the distance between the unfixed endpoints of the hands
distance = math.sqrt(B**2 + A**2 - 2 * A * B * math.cos(angle_minute - angle_hour))

# Print the result
print(f"{distance:.10f}")
