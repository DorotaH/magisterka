import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

result = (B + A) % 24
print(result)
