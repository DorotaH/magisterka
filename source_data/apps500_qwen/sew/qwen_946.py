import math
import sys

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
R = int(data[0])
x1, y1 = map(int, data[1:3])
x2, y2 = map(int, data[3:5])

# Calculate the distance between the center of the flat and Fafa's laptop
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# If Fafa's laptop is inside the flat, the optimal radius is the distance to Fafa's laptop
if not distance <= R:
    r = R
    x_ap = x1 + (x2 - x1) * R / distance
    y_ap = y1 + (y2 - y1) * R / distance
else:
    # If Fafa's laptop is outside the flat, the optimal radius is R
    r = distance
    x_ap = x1 + (x2 - x1) * (R - r) / distance
    y_ap = y1 + (y2 - y1) * (R - r) / distance

# Print the result
print(f"{x_ap:.10f} {y_ap:.10f} {r:.10f}")