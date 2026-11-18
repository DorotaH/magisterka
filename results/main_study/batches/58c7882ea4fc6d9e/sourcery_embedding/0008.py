def main():
  S = str(input())

  ans = [0] * 13
  ans[0] = 1
  MOD = 10**9 + 7

  for i in S:
    dp = [0] * 13
    for j in range(13):
        dp[(j * 10) % 13] = ans[j] % MOD
    dp += dp
    for j in range(13):
      ans[j] = sum(dp[j+4:j+14]) if i == '?' else dp[j + 13 - int(i)]
  print(ans[5] % MOD)

def __starting_point():
    main()
__starting_point()