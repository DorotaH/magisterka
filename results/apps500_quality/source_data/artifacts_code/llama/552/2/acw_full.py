import sys
input = sys.stdin.readline
from collections import defaultdict


def rai():
	return map(int, input().split())


def ra():
	return list(map(int, input().split()))


def rs():
	return input().strip()


n, m = rai()
a = rs()
b = rs()
s = rs()


def kmp_prefix_function(s):
	j = 0
	pi = [0] * len(s)
	for i in range(1, len(s)):
		while j and s[i] != s[j]:
			j = pi[j - 1]
		if s[i] == s[j]:
			j += 1
		pi[i] = j
	return pi


pi_a = kmp_prefix_function('$' + a + b)
pi_b = kmp_prefix_function('$' + b + a)

last_occ_a = [-1] * (1 + n)
last_occ_b = [-1] * (1 + n)

for i in range(1, 1 + n):
	last_occ_a[pi_a[i]] = i

for i in range(1, 1 + n):
	last_occ_b[pi_b[i]] = i

positions = [
	last_occ_a[i]
	for i in range(m)
	if last_occ_a[i] != -1
	and last_occ_b[m - i] != -1
	and a[last_occ_a[i]] == s[i]
	and b[last_occ_b[m - i]] == s[m - i]
]
positions.sort()

if not positions:
	print(0)
	exit()

ans = sum(1 if positions[i] == 1 else 2 for i in range(len(positions)))
for i in range(len(positions) - 1):
	ans += (positions[i + 1] - positions[i])

print(ans)
