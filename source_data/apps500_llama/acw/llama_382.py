n = int(input())


def max_presents(n):
	return 1 if n in [1, 2] else n - 1


print(max_presents(n))
