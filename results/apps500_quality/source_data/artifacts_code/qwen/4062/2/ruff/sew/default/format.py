import sys

input = sys.stdin.read
data = input().split()

a, b = int(data[0]), int(data[1])
c, d = int(data[2]), int(data[3])

max_value = max(c * a, d * a, c * b, d * b)
print(max_value)
