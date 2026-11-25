def can_be_sum_of_distinct_odds(n, k):
	if k > n:
		return "NO"
	if 2 * k > 1 + n:
		return "NO"
	return "YES" if (n - k * (k + 1) // 2) % 2 == 0 else "NO"


t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	print(can_be_sum_of_distinct_odds(n, k))
