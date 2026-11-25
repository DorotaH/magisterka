import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

c = list(map(int, data[3:3+k]))
index = [0] * (k + 1)
for i in range(1, k + 1):
    index[i] = index[i - 1] + c[i - 1]

edges = []
for i in range(m):
    u = int(data[3 + k + 3 * i]) - 1
    v = int(data[3 + k + 3 * i + 1]) - 1
    x = int(data[3 + k + 3 * i + 2])
    edges.append((u, v, x))

# Check if the type-distribution is correct
type_correct = True
for i in range(k):
    for j in range(i + 1, k):
        found = False
        for u, v, x in edges:
            if (u >= index[i] and u < index[i + 1] and v >= index[j] and v < index[j + 1]) or (u >= index[j] and u < index[j + 1] and v >= index[i] and v < index[i + 1]):
                found = True
                break
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
                if (u >= index[i] and u < index[i + 1] and v >= index[j] and v < index[j + 1]):
                    if d[i][j] == -1 or d[i][j] > x:
                        d[i][j] = x

    for i in range(k):
        for j in range(k):
            if d[i][j] == -1:
                print(d[i][j], end=' ')
            else:
                print(d[i][j], end=' ')
        print()
