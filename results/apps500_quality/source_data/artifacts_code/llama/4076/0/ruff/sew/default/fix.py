
# Read input from standard input
A, B, H, M = map(int, input().split())

# Calculate the total angle moved by the hour hand
hour_angle, minute_angle = (H * 30) + (M / 60) * 30, M * 6

# Calculate the distance between the two hands
distance = abs((A * (hour_angle / 180)) - (B * (minute_angle / 180)))

# Account for the fact that the distance between the hands can be on the other side
distance = min(distance, (2 * A) - distance)

# Print the result with high precision
print(f"{distance:.10f}")