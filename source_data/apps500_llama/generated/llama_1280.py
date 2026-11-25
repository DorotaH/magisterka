import sys
input = sys.stdin.readline

def calc_min_sum(g0, x, y, z, n, m, a, b):
    def get_value(i, j):
        return ((g0 * (x ** (i - 1)) + (j - 1)) % z)

    prefix = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = min(prefix[i - 1][j], prefix[i][j - 1], get_value(i, j))

    ans = 0
    for i in range(1, n - a + 2):
        for j in range(1, m - b + 2):
            ans += min(prefix[i + a - 1][j + b - 1], prefix[i + a - 1][j - 1], get_value(i + a - 1, j + b - 1)) - min(prefix[i - 1][j + b - 1], prefix[i + a - 1][j - 1], get_value(i - 1, j + b - 1))
    return ans

n, m, a, b = map(int, input().split())
g0, x, y, z = map(int, input().split())
print(calc_min_sum(g0, x, y, z, n, m, a, b))
