import sys
input = sys.stdin.read
data = input().split()

A, B = int(data[0]), int(data[1])

result = (A + B) % 24
print(result)