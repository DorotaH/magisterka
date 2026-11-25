from collections import defaultdict

MOD = 998244353


def read_int():
	return int(input())


def read_ints():
	return map(int, input().split())


def read_str():
	return input()


def solve():
	n = read_int()
	a = [read_ints() for _ in range(n)]
	cnt = defaultdict(int)
	for ai, bi in a:
		cnt[ai] += 1
		cnt[bi] += 1
	b = [[] for _ in range(1 + n)]
	for i in range(1, 1 + n):
		b[cnt[i]].append(i)
	ans = 1
	group = 1
	for i in range(1, 1 + n):
		if len(b[i]) == 1:
			ans = i * ans % MOD
		else:
			if b[i]:
				b[i].reverse()
			group += 1
			ans = group * ans % MOD
			group = (group - 1) % MOD
	return ans


print(solve())
