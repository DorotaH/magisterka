n, l, r = map(int, input().split())


def solve(i, n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return solve(i + 1, n // 2) + solve(i + 1, n % 2)


def get_ones(n):
    dp = [0] * 61
    dp[0] = 1
    dp[1] = 1
    for i in range(2, 61):
        dp[i] = solve(1, i)
    return dp


dp = get_ones(60)

n_list = list(map(int, input().split()))[0]
ones = 0
for i in range(1, n_list + 1):
    ones += dp[n_list - i] if i >= l else 0

for i in range(r - 1, n_list):
    ones -= dp[n_list - i] if i >= l else 0

print(ones)
