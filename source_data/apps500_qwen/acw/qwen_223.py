import sys
input = sys.stdin.read
data = input().split()

X = int(data[0])
Y = int(data[1])
Z = int(data[2])

# Calculate the maximum number of people that can sit on the seat
max_people = (X - Y) // (Y + 2 * Z) + 1

print(max_people)
