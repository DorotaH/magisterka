import math

# Read input from standard input
a, b = map(int, input().split())

# Calculate the average of a and b
x = (a + b) / 2

# Round up to the nearest integer
x = math.ceil(x)

print(x)