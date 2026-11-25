
N = int(input())
strings = []
costs = list()
for _ in range(N):
    s, c = input().split()
    strings.append(s)
    costs.append(int(c))

def  is_palindrome(s):
    return  s[::-1] == s

def  min_cost():
    dp = []
    for _ in range(N + 1):
        dp.append([float('inf')] * (N + 1))
    dp[0][0]=0
    for  i in  range(0, N):
        for j in range(1, 1 + i):
            if not is_palindrome(strings[i]):
                dp[j][i + 1] = min(dp[j][i], dp[j][i - 1] + costs[i])
            else:
                dp[j][i + 1] = min(dp[j][i], dp[j - 1][i - 1] + costs[i])
    for  j in  range(0, N + 1):
        if  dp[j][N]<float('inf'):
            return dp[j][N]
    return  -1

print(min_cost())
