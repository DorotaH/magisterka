def read_int():
	return int(input())


def read_ints():
	return list(map(int, input().split(" ")))


t = read_int()
for _ in range(t):
	n, k = read_ints()
	i = 1
	largest = 1
	while i**2 <= n:
		if n % i == 0:
			if i <= k:
				largest = max(largest, i)
			if n // i <= k:
				largest = max(largest, n // i)
		i += 1
	print(n // largest)
