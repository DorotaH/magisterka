# Read input from standard input
A, B = map(int, input().split())

# Calculate the area excluding the roads
area_excluding_roads = (B - 1) * (A - 1)

# Print the result
print(area_excluding_roads)
