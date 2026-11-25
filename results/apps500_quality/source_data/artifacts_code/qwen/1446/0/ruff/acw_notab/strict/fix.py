import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

c = list(map(int, data[3:k + 3]))
index = [0] * (k + 1)
for i in range(1, k + 1):
    index[i] = c[i - 1] + index[i - 1]

edges = []
for i in range(m):
    u = int(data[k + 3 + i * 3]) - 1
    v = int(data[k + 3 + i * 3 + 1]) - 1
    x = int(data[k + 3 + i * 3 + 2])
    edges.append((u, v, x))

# Check if the type-distribution is correct
type_correct = True
for i in range(k):
    for j in range(i + 1, k):
        found = any(
            (
                index[i] <= u
                and u < index[i + 1]
                and index[j] <= v
                and v < index[1 + j]
            )
            or (
                index[j] <= u
                and u < index[1 + j]
                and index[i] <= v
                and v < index[i + 1]
            )
            for u, v, x in edges
        )
        if not found:
            type_correct = False
            break
    if not type_correct:
        break

if not type_correct:
    print("No")
else:
    print("Yes")
    d = [[-1] * k for _ in range(k)]
    for i in range(k):
        d[i][i] = 0

    for u, v, x in edges:
        for i in range(k):
            for j in range(k):
                if index[i] <= u and u < index[i + 1] and index[j] <= v and v < index[1 + j] and (d[i][j] == -1 or d[i][j] > x):
                    d[i][j] = x

    for i in range(k):
        for j in range(k):
            print(d[i][j], end=' ')
        print()
