import sys

n = int(sys.stdin.readline())

w = []
for _ in range(n):
    w.append([float(x) for x in sys.stdin.readline().split()])

a = [[0.0 for _ in range(n)] for _ in range(n)]
b = [[0.0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = w[i][j] + w[j][i]
        b[i][j] = w[i][j] - w[j][i]

for row in a:
    print(' '.join(map(str, row)))

for row in b:
    print(' '.join(map(str, row)))
