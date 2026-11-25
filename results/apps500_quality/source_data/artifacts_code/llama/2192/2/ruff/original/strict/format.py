import sys

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = w[i][j] + w[j][i]
        b[i][j] = w[i][j] - w[j][i]

for row in a:
    print(*["%.6f" % num for num in row])

for row in b:
    print(*["%.6f" % num for num in row])
