import sys


def match(s, t, i, j):
	while i < len(s) and len(t) > j:
		if s[i] != t[j]:
			return False
		i += 1
		j += 1
	return i == len(s)


def solve():
	n, m = map(int, input().split())
	s = input()
	t = input()

	result = []
	for i in range(n):
		found = False
		for j in range(i + 1, min(i + 8, n - i + 1)):
			if match(s[:i] + '?' * (j - i) + s[i + j:], t):
				result.append(i + j)
				found = True
				break
		if not found:
			result.append(i)

	print(len(result))
	print(' '.join(map(str, sorted(result))))


if __name__ == "__main__":
	solve()
