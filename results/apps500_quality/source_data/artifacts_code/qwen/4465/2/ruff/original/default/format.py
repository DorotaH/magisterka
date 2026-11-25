import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

area = (A - 1) * (B - 1)
print(area)
