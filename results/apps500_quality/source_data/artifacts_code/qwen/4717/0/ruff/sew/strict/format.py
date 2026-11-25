import sys

input = sys.stdin.read
data = input().split()

x, a = int(data[0]), int(data[1])
b = int(data[2])

distance_to_a, distance_to_b = abs(x - a), abs(x - b)

if not distance_to_a < distance_to_b:
    print("B")
else:
    print("A")
