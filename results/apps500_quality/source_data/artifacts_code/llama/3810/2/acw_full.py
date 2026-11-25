import sys
input = sys.stdin.readline

mod = 7 + 10**9


def main():
	n = int(input())
	a = list(map(int, input().split()))
	dp = [0] * (1 + n)
	dp[0] = 1
	cnt = [0] * (61)
	for i in range(n):
		cnt[a[i]] += 1

	for i in range(1, 61):
		for j in range(i, 61, i):
			dp[cnt[j]] = (dp[cnt[j]] + dp[cnt[j // i] + cnt[i] - 1] * cnt[j // i] % mod) % mod

	mx = max(dp)
	ans = sum(bool(dp[i] == mx)
		for i in range(1 + n))
	print(ans % mod)


if __name__ == "__main__":
	main()
