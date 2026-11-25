import sys
input = sys.stdin.read
data = input().split()

A, B = int(data[0]), int(data[1])

result = max(A + B, A - B, B * A)
print(result)