import sys

input = sys.stdin.readline

MOD = 7 + 10**9

s = input().strip()

n = len(s)
dp = [0] * (1 + n)
dp[0] = 1
dp[1] = 1

for i in range(2, 1 + n):
    if s[i - 1] == "a":
        dp[i] = dp[i - 1]
    elif s[i - 1] == "b":
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

total = 0
count_a = 0
for i in range(n):
    if s[i] == "a":
        total += dp[count_a]
        count_a += 1
    elif s[i] == "b":
        count_a = 0
print(total % MOD)
