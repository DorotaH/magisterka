def solve():
    import sys

    input = sys.stdin.readline

    def inp():
        return list(map(int, input().split()))

    def infl():
        return list(map(int, sys.stdin.readline().strip().split()))

    def aint():
        return int(input())

    def str():
        return input().strip()

    def dprint(*args):
        print(*args, file=sys.stderr)

    MOD = 998244353
    N = 510
    DP = [[0] * N for _ in range(N)]
    DP[1][1] = 2
    DP[2][1] = 2
    DP[2][2] = 2

    for n in range(3, 501):
        for k in range(1, n):
            if k == 1:
                DP[n][k] = 2
            else:
                for i in range(k, n):
                    DP[n][k] += DP[i][k - 1] * DP[n - i][k] % MOD

            for k in range(n, 1, -1):
                for i in range(k, n):
                    DP[n][k] -= DP[i][k - 1] * DP[n - i][k] % MOD
                    DP[n][k] %= MOD
                if DP[n][k] < 0:
                    DP[n][k] += MOD

    n, k = inp()
    print(DP[n][k])


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
