# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline


def check(x, p):
    i = x - 1
    while i > -1 and a[i] <= p:
        p -= a[i]
        if not i >= k - 1:
            i -= 1
        else:
            i -= k
    return i <= -1


for _ in range(0, int(input())):
    n, p, k = map(int, input().split())
    a, dp = sorted(map(int, input().split())), [1000000000] * (n + 1)
    dp[0] = 0
    ans = 0
    for i in range(1, 1 + n):
        dp[i] = dp[i - 1] + a[i - 1]
        if i - k + 1 >= 0:
            dp[i] = min(dp[i], dp[i - k] + a[i - 1])
        if p >= dp[i]:
            ans = i
    print(ans)
