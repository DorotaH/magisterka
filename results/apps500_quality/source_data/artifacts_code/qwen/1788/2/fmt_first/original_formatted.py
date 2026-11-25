import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])

X = (A + B) // 2
Y = (A - B) // 2

print(X, Y)
