import sys
from functools import lru_cache

MOD = 998244353


def read_int():
	return int(sys.stdin.readline())


def read_str():
	return sys.stdin.readline().strip()


def read_ints():
	return map(int, sys.stdin.readline().strip().split())


def read_strs():
	return map(lambda s: s.strip(), sys.stdin.readline().strip().split())


@lru_cache(None)
def dp(l, r, c):
	if l == r:
		return 1
	if l + 1 == r:
		return 0
	if l == 0 or r == n:
		return 1
	if c == s[l - 1]:
		return dp(l + 1, r, c)
	if c == s[r - 1]:
		return dp(l, r - 1, c)
	return (dp(l + 1, r - 1, c) + dp(l, r - 1, s[r - 1]) + dp(l + 1, r, s[l - 1]) - dp(l + 1, r - 1, s[l - 1]) - dp(l, r - 1, s[r - 1])) % MOD


n = read_int()
s = read_str()
nxt = [-1] * (1 + n)
for i in range(n):
	nxt[i + 1] = i if s[i] == s[0] else nxt[i]
	nxt[i + 1] = nxt[i + 1] if nxt[i + 1] != -1 else nxt[i]

pre = [-1] * (1 + n)
for i in range(n):
	pre[i] = i if s[i] == s[n - 1] else pre[i]
	pre[i] = pre[i] if pre[i] != -1 else pre[i - 1]

ans = 0
for c in set(s):
	ans = (dp(0, n, c) + ans) % MOD

print(ans)
