def min_height(n, k):
	k -= (n * (1 + n))
	if k < 0:
		return 0
	return k // (1 + n) if k % (1 + n) == 0 else k // (1 + n) + 1


n, k = map(int, input().split())
print(min_height(n, k))
