import sys


def main():
    input = sys.stdin.read().splitlines()
    lines = [line.split() for line in input]
    n, m, k = map(int, lines[0])

    a, b, c = zip(*[map(int, lines[i]) for i in range(1, 1 + n)])
    portals = []
    for i in range(1 + n, len(lines)):
        u, v = map(int, lines[i])
        portals.append((u, v))

    dp = [[float('-inf')] * (k + 1) for _ in range(1 + n)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(k + 1):
            if dp[i][j] == float('-inf'):
                continue
            for x in range(1, 1 + a[i]):
                if x + j <= k:
                    dp[i + 1][x + j] = max(dp[i + 1][x + j], c[i] + dp[i][j])
                if a[i] <= j:
                    dp[i + 1][j] = max(dp[i + 1][j], c[i] + dp[i][j])

    for u, v in portals:
        for j in range(k + 1):
            dp[u][j] = max(dp[u][j], dp[v][j])

    ans = float('-inf')
    for j in range(k + 1):
        ans = max(ans, dp[n][j])

    if ans == float('-inf'):
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
