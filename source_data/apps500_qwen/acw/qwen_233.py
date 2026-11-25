import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

result = max(B + A, A - B, B * A)
print(result)
