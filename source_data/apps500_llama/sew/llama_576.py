# Read input from standard input
W, a, b = map(int, input().split())

# Calculate the minimum distance to move the second rectangle
min_distance = min(abs(a - (b - W)), W - (b - a), b - a, abs(b - (a + W)))

# Print the result
print(min_distance)