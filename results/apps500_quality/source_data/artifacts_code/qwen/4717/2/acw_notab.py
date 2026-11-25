import sys
input = sys.stdin.read
data = input().split()

x = int(data[0])
a = int(data[1])
b = int(data[2])

if abs(x - a) < abs(x - b):
    print("A")
else:
    print("B")
