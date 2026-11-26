import sys

input = sys.stdin.read
data = input().split()

A, B = int(data[0]), int(data[1])

X, Y = (A + B) // 2, (A - B) // 2

print(X, Y)
