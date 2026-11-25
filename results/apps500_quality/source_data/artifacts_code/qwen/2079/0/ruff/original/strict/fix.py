import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
w = list(map(int, data[1].split()))
p = data[2]

rows = [[] for _ in range(n)]
for i in range(n):
    rows[i].append((w[i], i + 1))

empty_rows = sorted(rows, key=lambda x: x[0][0])
occupied_rows = sorted(rows, key=lambda x: -x[0][0])

empty_indices = [0] * n
occupied_indices = [0] * n

result = [0] * (2 * n)

for i in range(2 * n):
    if p[i] == '0':
        result[i] = empty_rows[empty_indices[0]][1]
        empty_indices[0] += 1
        if empty_indices[0] < n:
            empty_rows[empty_indices[0]], empty_rows[empty_indices[0] - 1] = empty_rows[empty_indices[0] - 1], empty_rows[empty_indices[0]]
    else:
        result[i] = occupied_rows[occupied_indices[0]][1]
        occupied_indices[0] += 1
        if occupied_indices[0] < n:
            occupied_rows[occupied_indices[0]], occupied_rows[occupied_indices[0] - 1] = occupied_rows[occupied_indices[0] - 1], occupied_rows[occupied_indices[0]]

print(' '.join(map(str, result)))
