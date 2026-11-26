import sys

input = sys.stdin.read
data = input().split()

x, a = int(data[0]), int(data[1])
b = int(data[2])

if not abs(x - a) < abs(x - b):
    print("B")
else:
    print("A")
