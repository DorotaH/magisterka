import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

result = max(A + B, A - B, A * B)
print(result)
