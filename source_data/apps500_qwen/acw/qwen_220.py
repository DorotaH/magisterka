# Read input from standard input
A, B = map(int, input().split())

# Calculate the area excluding the roads
area = (B - 1) * (A - 1)

# Print the result
print(area)
