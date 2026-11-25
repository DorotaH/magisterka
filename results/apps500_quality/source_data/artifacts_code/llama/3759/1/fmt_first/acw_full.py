import math


def min_blocked_points(n):
	def is_prime(x):
		if 2 > x:
			return False
		for i in range(2, int(math.sqrt(x)) + 1):
			if x % i == 0:
				return False
		return True

	ans = 0
	for k in range(1, 1 + n):
		ans += (k - 1) * 4 * 4 ** (k - 1)
		if is_prime(k):
			ans -= (k - 1) * 4 * 4 ** (k - 1)
	return ans


n = int(input())
print(min_blocked_points(n))
