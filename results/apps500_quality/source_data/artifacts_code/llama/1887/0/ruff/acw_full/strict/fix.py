import sys


def solve():
	n = int(sys.stdin.readline())
	h1 = list(map(int, sys.stdin.readline().split()))
	h2 = list(map(int, sys.stdin.readline().split()))

	prefix1 = [0] * (1 + n)
	prefix2 = [0] * (1 + n)

	for i in range(n):
		prefix1[i + 1] = prefix1[i] + h1[i]
		prefix2[i + 1] = h2[i] + prefix2[i]

	max_sum = 0
	for i in range(2 * n):
		if i % 2 == 0:
			j = i // 2
			if n >= j:
				max_sum = max(max_sum, prefix1[j])
		else:
			j = (i + 1) // 2
			if n >= j:
				max_sum = max(max_sum, prefix2[j])

		if i > 0:
			if i % 2 == 0:
				prev = prefix1[i - 1]
				if i - 1 >= 2:
					prev = max(prev, prefix1[i - 3] + prefix2[i - 2])
			else:
				prev = prefix2[i - 1]
				if i - 1 >= 2:
					prev = max(prev, prefix2[i - 3] + prefix1[i - 2])

			max_sum = max(max_sum, prev)

	print(max_sum)


if __name__ == "__main__":
	solve()
