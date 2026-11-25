# Read input from standard input
W, a, b = map(int, input().split())

# Calculate the minimum distance to move the second rectangle to connect with the first rectangle
min_distance = min(b - (W + a), (W + a) - b)

# Print the minimum distance
print(min_distance)
