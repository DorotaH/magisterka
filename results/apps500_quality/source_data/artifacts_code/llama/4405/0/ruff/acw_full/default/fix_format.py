from collections import defaultdict


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    topics = defaultdict(int)
    for i in range(n):
        topics[a[i]] += 1

    dp = [0] * (1 + n)
    dp[0] = 0
    for i in range(1, 1 + n):
        dp[i] = dp[i - 1]
        dp[i] = max(dp[i], dp[i - 1] + topics[2 * a[i - 1]])

    ans = 0
    i = n
    while i > 0:
        if dp[i] > dp[i - 1]:
            ans += topics[2 * a[i - 1]]
            i -= 1
        else:
            ans += topics[a[i - 1]]
        i -= 1

    print(ans)


if __name__ == "__main__":
    solve()
