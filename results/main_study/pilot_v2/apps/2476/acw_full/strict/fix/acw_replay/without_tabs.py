N = int(input())
A = list(map(int, input().split()))
from bisect import bisect
from collections import Counter

vs = list(Counter(A).values())
vs.sort()
cums = [0]
cums.extend(cums[-1] + v for v in vs)


def is_ok(k, m):
	j = bisect(vs, m)
	z = cums[j] + (len(vs) - j) * m
	return z >= k * m


ans = []
for k in range(1, N + 1):
	if len(vs) < k:
		ans.append(0)
	else:
		ok = 0
		ng = N // k + 1
		while ng - ok > 1:
			m = (ng + ok) // 2
			if is_ok(k, m):
				ok = m
			else:
				ng = m
		ans.append(ok)

print(*ans, sep='\n')
