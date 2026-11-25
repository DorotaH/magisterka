from collections import Counter

t = int(input())
for _ in range(t):
	s = input()
	cnt = Counter(s)
	odd_count = sum(bool(c % 2 != 0)
				for c in cnt.values())

	if odd_count > 1:
		print(-1)
	else:
		res = ''.join((cnt[c] // 2) * c for c in s)
		print(res)
