import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

area = (B - 1) * (A - 1)
print(area)
