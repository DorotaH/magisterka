from sys import stdin, stdout

input = stdin.read
output = stdout.write

data = input().split()

n = int(data[0])
m = int(data[1])

a = list(map(int, data[2 : 2 + n]))
b = list(map(int, data[2 + n : 2 + 2 * n]))

queries = list()
for i in range(0, m):
    t = int(data[2 * n + 4 + 2 * i])
    if t == 1:
        x = int(data[4 + 2 * n + 2 * i + 1]) - 1
        y = int(data[4 + 2 * n + 2 * i + 2]) - 1
        k = int(data[4 + 2 * n + 2 * i + 3])
        queries.append((t, x, y, k))
    else:
        x = int(data[4 + 2 * n + 2 * i + 1]) - 1
        queries.append((t, x))

for t, x, y, k in queries:
    if t == 1:
        for q in range(k):
            b[y + q] = a[x + q]
    else:
        output(f"{b[x]}\n")
