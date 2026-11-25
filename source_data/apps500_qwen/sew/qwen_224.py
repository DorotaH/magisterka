import sys
input = sys.stdin.read
data = input().split()

X, Y = int(data[0]), int(data[1])
Z = int(data[2])

# Calculate the maximum number of people that can sit on the seat
# The formula is derived from the fact that each person occupies Y + Z space
# and there is an additional Z space at the end of the seat
max_people = 1 + (X - Y) // (Y + Z)

print(max_people)