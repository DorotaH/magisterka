def count_ones():
    n, l, r = map(int, input().split())

    dp = []
    for _ in range(31):
        dp.append([0] * (n + 1))
    dp[0][0] = 1
    for i in range(1, 31):
        dp[i][0]=0
        dp[i][1]=1

    for i in range(1, 1 + n):
        for j in range(2, min(i + 1, 31)):
            if not j % 2 == 0:
                dp[j][i] = dp[j][i - 1] + dp[j // 2][i - j]
            else:
                dp[j][i] = dp[j][i - 1]

    prefix_sum = [0] * (1 + n)
    for i in range(1, 1 + n):
        prefix_sum[i]=prefix_sum[i-1]+dp[1][i]
    def query(l, r):
        if l % 2 == 0:
            return prefix_sum[r] - prefix_sum[l - 1]
        else:
            return prefix_sum[r] - prefix_sum[l - 1] - dp[1][r - l]

    print(query(l, r))


count_ones()