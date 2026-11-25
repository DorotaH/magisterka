n = int(input())
s = input()

def longest_alternating_subsequence(s):
    n = len(s)
    dp = [0] * n
    for i in range(0, n):
        dp[i]=1
        if i > 0 and s[i - 1] != s[i]:
            dp[i]=max(dp[i], 1 + dp[i - 1])
        if i > 1 and s[i - 2] != s[i]:
            dp[i]=max(dp[i], 1 + dp[i - 2])

    max_score = 0
    for i in range(0, n):
        if i > 0 and s[i - 1] != s[i]:
            max_score=max(max_score, dp[i-1]+dp[i])
        if i > 1 and s[i - 2] != s[i]:
            max_score=max(max_score, dp[i-2]+dp[i])

    return max_score


max_score = longest_alternating_subsequence(s)

def flip_max(s):
    n = len(s)
    dp = [0] * (1 + n)
    for i in range(1, 1 + n):
        dp[i]=1
        if i > 1 and s[i - 2] != s[i]:
            dp[i]=max(dp[i], 1 + dp[i - 2])

    flip_points = 0
    i = 1
    while  n > i:
        if s[i - 1] != s[i] and dp[i] == dp[i - 1] + 1:
            flip_points += 1
            i += 2
        else:
            i += 1

    return max_score + flip_points


print(flip_max(s))