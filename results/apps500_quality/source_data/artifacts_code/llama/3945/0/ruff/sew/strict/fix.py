

def solve() -> None:
    n, m=map(int, input().split())
    a=[list(map(int, input().split())) for  _ in  range(n)]

    for  i in  range(0, n):
        row_max, col_max = max(a[i]), max([a[j][i] for j in range(m)])
        print(*[max(row_max, col_max - (col_max - row_max)) for  _ in  range(0, m)])

solve()
