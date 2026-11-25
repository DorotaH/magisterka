# Read input from standard input
A, B = map(int, input().split())

# Calculate the area excluding the roads
area = (A - 1) * (B - 1)

# Print the result
print(area)