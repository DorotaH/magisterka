import sys

input = sys.stdin.read
data = input().split()

x = int(data[0])
a = int(data[1])
b = int(data[2])

distance_to_a = abs(x - a)
distance_to_b = abs(x - b)

if distance_to_a < distance_to_b:
    print("A")
else:
    print("B")
