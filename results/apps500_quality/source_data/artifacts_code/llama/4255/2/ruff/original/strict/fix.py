# Read the lengths of the three sides from standard input
a, b, c = map(int, input().split())

# Calculate the semi-perimeter of the triangle
s = (a + b + c) / 2

# Calculate the area of the triangle using Heron's formula
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# Print the area of the triangle
print(int(area))
