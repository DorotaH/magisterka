import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

A.sort(reverse=True)
result = A[0]

for i in range(1, N):
    result = 1 + (result - 1) // A[i] * A[i]

print(result)
