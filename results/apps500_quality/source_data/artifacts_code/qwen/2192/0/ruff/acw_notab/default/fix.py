import sys
from fractions import Fraction

input = sys.stdin.read
data = input().split()

n = int(data[0])
W = [list(map(Fraction, data[1 + i * n:1 + (i + 1) * n])) for i in range(n)]
A = [[0] * n for _ in range(n)]
B = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            A[i][j] = W[i][j] / 2
            B[i][j] = 0
        else:
            A[i][j] = (W[i][j] + W[j][i]) / 4
            B[i][j] = (W[i][j] - W[j][i]) / 4

for i in range(n):
    for j in range(n):
        print(f"{A[i][j]:0.10f}", end=" ")
    print()
for i in range(n):
    for j in range(n):
        print(f"{B[i][j]:0.10f}", end=" ")
    print()
