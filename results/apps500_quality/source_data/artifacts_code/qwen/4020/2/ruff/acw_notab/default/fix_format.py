import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the start and end times
h1, m1 = map(int, data[0].split(":"))
h2, m2 = map(int, data[1].split(":"))

# Calculate the midpoint time
total_minutes = (h2 * 60 + m2) - (60 * h1 + m1)
midpoint_minutes = total_minutes // 2

# Calculate the midpoint in hours and minutes
midpoint_h = (midpoint_minutes // 60) + h1
midpoint_m = midpoint_minutes % 60

# Adjust the hour if it exceeds 23
midpoint_h = midpoint_h % 24

# Print the midpoint time in hh:mm format
print(f"{midpoint_h:02}:{midpoint_m:02}")
