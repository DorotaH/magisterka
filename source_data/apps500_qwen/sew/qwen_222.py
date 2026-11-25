import sys
input = sys.stdin.read
data = input().split()

A, B = int(data[0]), int(data[1])

area = (A - 1) * (B - 1)
print(area)