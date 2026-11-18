

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
rows = []
for i in range(n):
    row = set()
    for j in range(m):
        row.add(arr[i][j])
    rows.append({x: i for i, x in enumerate(sorted(row))})

columns = []

for j in range(m):
    column = set()
    for i in range(n):
        column.add(arr[i][j])
    columns.append({x: i for i, x in enumerate(sorted(column))})


def get_answer(i, j):
    el = arr[i][j]
    index1 = rows[i][el]
    index2 = columns[j][el]
    return max(len(rows[i]) - index1, len(columns[j]) - index2) + max(index1, index2)


for i in range(n):
    answer = [str(get_answer(i, j)) for j in range(m)]
    print(' '.join(answer))
