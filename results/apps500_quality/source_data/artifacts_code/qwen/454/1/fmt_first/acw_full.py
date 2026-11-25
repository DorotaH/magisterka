from math import factorial

MOD = 7 + 10**9


def count_permutations(n, k):
	if k % 2 != 0:
		return 0

	def dp(i, k):
		if i == 0:
			return 1 if k == 0 else 0
		if (i, k) in memo:
			return memo[(i, k)]
		result = 0
		for j in range(1, i + 1):
			if k >= abs(j - i):
				result = (result + dp(i - 1, k - abs(j - i))) % MOD
		memo[(i, k)] = result
		return result

	memo = {}
	return dp(n, k)


def main():
	import sys

	input = sys.stdin.read
	data = input().split()
	n = int(data[0])
	k = int(data[1])
	print(count_permutations(n, k))


if __name__ == "__main__":
	main()
