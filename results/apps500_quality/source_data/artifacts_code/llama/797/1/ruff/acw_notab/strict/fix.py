import sys

input = sys.stdin.readline


def calc_min_sum(g0, x, y, z, n, m, a, b):
    def get_value(i, j):
        return ((g0 * (x ** (i - 1)) + (j - 1)) % z)

    prefix = [[float('inf')] * (1 + m) for _ in range(1 + n)]
    for i in range(1, 1 + n):
        for j in range(1, 1 + m):
            prefix[i][j] = min(prefix[i - 1][j], prefix[i][j - 1], get_value(i, j))

    ans = 0
    for i in range(1, n - a + 2):
        for j in range(1, m - b + 2):
            ans += min(prefix[i + a - 1][b + j - 1], prefix[i + a - 1][j - 1], get_value(i + a - 1, b + j - 1)) - min(prefix[i - 1][b + j - 1], prefix[i + a - 1][j - 1], get_value(i - 1, b + j - 1))
    return ans


n, m, a, b = map(int, input().split())
g0, x, y, z = map(int, input().split())
print(calc_min_sum(g0, x, y, z, n, m, a, b))
