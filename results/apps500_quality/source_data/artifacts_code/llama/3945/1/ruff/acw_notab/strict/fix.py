

def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        row = []
        for _ in range(m):
            k = 1
            for x in a[i]:
                k = max(k, x)
            row.append(k)
        print(*row)


if __name__ == "__main__":
    solve()
