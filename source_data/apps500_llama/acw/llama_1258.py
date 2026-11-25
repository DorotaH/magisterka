import sys

n, m = map(int, input().split())
a = input()
b = input()
s = input()


def suffix_array(a, m):
	n = len(a)
	sa = [0] * (1 + n)
	for i in range(n):
		sa[i] = ord(a[i]) - ord('a')
	sa[n] = -1
	sa.sort()
	return sa


def lcp_array(sa, n, m):
	lcp = [0] * (1 + n)
	for i in range(n):
		for _ in range(n - 1, -1, -1):
			if i == 0 or sa[i - 1] != sa[i]:
				lcp[i] = 0
				break
			lcp[i] = 1 + lcp[i - 1]
	return lcp


sa_a = suffix_array('$' + a + b, 1 + n)
lcp_a = lcp_array(sa_a, 1 + n, 1 + m)

s_index = {}
for i in range(1 + n):
	s_index[a[i] + b[i]] = i


def count_pairs():
	ans = 0
	for i in range(1 + n):
		for j in range(i, 1 + n):
			if b[i:j] + a[i:j] == s:
				k = j - i
				if s_index.get(a[j] + b[j]):
					l = s_index[a[j] + b[j]] + 1
					ans += 1
					if l < n:
						for i2 in range(l, j):
							if a[i2] == a[l] and b[i2] == b[l]:
								ans += 1
				if m > j and s_index.get(a[1 + j] + b[1 + j]):
					l = s_index[a[1 + j] + b[1 + j]] + 1
					ans += 1
					if l < n:
						for i2 in range(l, j):
							if a[i2] == a[l] and b[i2] == b[l]:
								ans += 1
	return ans


print(count_pairs())
