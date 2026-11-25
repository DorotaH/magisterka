import sys
input = sys.stdin.readline

mod = 10**9 + 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    cnt = [0] * (61)
    for i in range(n):
        cnt[a[i]] += 1

    for i in range(1, 61):
        for j in range(i, 61, i):
            dp[cnt[j]] = (dp[cnt[j]] + dp[cnt[i] + cnt[j // i] - 1] * cnt[j // i] % mod) % mod

    ans = 0
    mx = max(dp)
    for i in range(n + 1):
        if dp[i] == mx:
            ans += 1

    print(ans % mod)

if __name__ == "__main__":
    main()
