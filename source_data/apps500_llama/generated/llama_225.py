import math

# Read input from standard input
X, Y, Z = map(int, input().split())

# Calculate the maximum number of people who can sit on the seat
max_people = math.floor((X - Z) / (Y + Z))

print(max_people)
