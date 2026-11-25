import sys

input = sys.stdin.read
data = input().split()

X, Y = int(data[0]), int(data[1])
Z = int(data[2])

# Calculate the maximum number of people that can sit on the seat
max_people = 1 + (X - Y) // (Y + 2 * Z)

print(max_people)