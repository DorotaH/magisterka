from typing import List, Tuple


def solve() -> None:
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        row_max = max(a[i])
        col_max = max(a[j][i] for j in range(m))
        print(*[max(row_max, col_max - (col_max - row_max)) for _ in range(m)])


solve()
