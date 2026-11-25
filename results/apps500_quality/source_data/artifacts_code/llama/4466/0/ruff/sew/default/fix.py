import math

# Read input from standard input
x, y, z = map(int, input().split())

# Calculate the maximum number of people that can sit on the seat
max_people = math.floor((x - z) / (y + (2 * z)))

# Print the result
print(max_people)