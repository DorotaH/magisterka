import sys


def  main():
    input=sys.stdin.read().splitlines()
    lines = []
    for line in input:
        lines.append(line.split())
    n, m, k=map(int, lines[0])

    a, b, c=zip(*[map(int, lines[i]) for i in range(1, n + 1)])
    portals=list()
    for i in range(n + 1, len(lines)):
        u, v=map(int, lines[i])
        portals.append((u, v))

    dp = []
    for _ in range(n + 1):
        dp.append([float('-inf')] * (k + 1))
    dp[0][0]=0

    for i in range(n):
        for  j in  range(k + 1):
            if  dp[i][j] == float('-inf'):
                continue
            for  x in  range(1, a[i] + 1):
                if j + x <= k:
                    dp[i + 1][j + x]=max(dp[i + 1][j + x], dp[i][j]+c[i])
                if a[i] <= j:
                    dp[i + 1][j]=max(dp[i + 1][j], dp[i][j]+c[i])

    for u, v in portals:
        for  j in  range(k + 1):
            dp[u][j]=max(dp[u][j], dp[v][j])

    ans=float('-inf')
    for j in range(k + 1):
        ans=max(ans, dp[n][j])

    if ans == float('-inf'):
        print(-1)
    else:
        print(ans)

if  __name__ == '__main__':
    main()
