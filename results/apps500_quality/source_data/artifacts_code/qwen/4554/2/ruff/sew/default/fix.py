# Read input from standard input
W, a, b = map(int, input().split())

# Calculate the minimum distance to move the second rectangle
min_distance = min(abs(a - (b + W)), abs((a + W) - b))

# Print the result
print(min_distance)