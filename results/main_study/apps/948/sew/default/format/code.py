n, m = list(map(int, input().split()))

field = list()
for i in range(0, n):
    field.append(input())

ans = 0
for i in range(0, n - 1):
    for j in range(m - 1):
        t = set()
        t.add(field[i][j])
        t.add(field[i + 1][j + 1])
        t.add(field[i + 1][j])
        t.add(field[i][j + 1])

        if t == set("face"):
            ans = ans + 1
print(ans)
