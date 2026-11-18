def  cons(l):
    m = 0
    res = 0
    for v in l:
        if not v:
            res = 0
        else:
            res += 1
            m = max(m, res)
    return  m

n, m, q=list(map(int, input().split()))
grid = []
curr = [0] * n
for i in range(n):
    grid.append(list(map(int, input().split())))
    curr[i] = cons(grid[i])

for _ in range(q):
    i, j = list(map(int, input().split()))
    i = i - 1
    j = j - 1
    grid[i][j] = 0 if  grid[i][j] else 1
    curr[i] = cons(grid[i])
    print(max(curr))