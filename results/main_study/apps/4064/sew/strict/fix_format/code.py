def main():
    import sys

    input = sys.stdin.readline

    N, H, L, R = list(map(int, input().split()))
    A = list(map(int, input().split()))

    dp = []
    for _ in range(N + 1):
        dp.append([-1] * H)
    dp[0][0] = 0
    for i, a in enumerate(A, 0):
        for t in range(0, H):
            if dp[i][t] >= 0:
                dp[1 + i][(t + a) % H] = max(
                    dp[1 + i][(t + a) % H], dp[i][t] + int(L <= (t + a) % H <= R)
                )
                dp[1 + i][(t + a - 1) % H] = max(
                    dp[1 + i][(t + a - 1) % H],
                    dp[i][t] + int(L <= (t + a - 1) % H <= R),
                )
    print(max(dp[-1]))


def __starting_point():
    main()


__starting_point()
