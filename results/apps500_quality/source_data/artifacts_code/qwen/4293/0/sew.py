# Read input from standard input
P, Q, R = map(int, input().split())

# Calculate the minimum possible sum of the flight times
min_time = min(P + Q, Q + R, R + P)

# Print the minimum possible sum of the flight times
print(min_time)