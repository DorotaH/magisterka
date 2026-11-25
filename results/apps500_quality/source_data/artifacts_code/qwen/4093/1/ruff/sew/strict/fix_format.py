def max_adj_diff(n, m):
    if n == 1:
        return 0
    elif n == 2:
        return m
    else:
        return m - (n - 1)


t = int(input())
for _ in range(0, t):
    n, m = map(int, input().split())
    print(max_adj_diff(n, m))
