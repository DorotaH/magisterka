import sys


def read_int():
	return int(sys.stdin.readline().rstrip("\n"))


def read_ints():
	return map(int, sys.stdin.readline().rstrip("\n").split())


def read_int_list():
	return list(map(int, sys.stdin.readline().rstrip("\n").split()))


def solve():
	n, k = read_ints()
	s = sys.stdin.readline().rstrip("\n")
	t = sys.stdin.readline().rstrip("\n")

	if s[0] != t[0]:
		return next((k * (i + 1) for i in range(n) if s[i] != t[i]), k * (1 + n))
	max_len = 0
	for i in range(n):
		if s[i] == t[i]:
			max_len += 1
		else:
			break

	max_c = (k + 1) * max_len

	for i in range(n):
		if s[i] != t[i]:
			max_c += (k - 1) * (i - max_len + 1)

	return max_c


if __name__ == "__main__":
	print(solve())
