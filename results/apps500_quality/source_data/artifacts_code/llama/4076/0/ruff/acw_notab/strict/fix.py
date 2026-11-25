
# Read input from standard input
A, B, H, M = map(int, input().split())

# Calculate the total angle moved by the hour hand
hour_angle = (30 * H) + (M / 60) * 30
minute_angle = 6 * M

# Calculate the distance between the two hands
distance = abs((hour_angle / 180) * A - B * (minute_angle / 180))

# Account for the fact that the distance between the hands can be on the other side
distance = min(distance, 2 * A - distance)

# Print the result with high precision
print(f"{distance:.10f}")
