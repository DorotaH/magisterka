def solve(k):
	q = p[:k] + p[k:]
	visited = [False] * n
	cnt = 0
	for i in range(n):
		t = i
		if not visited[t]:
			cnt += 1
			while not visited[t]:
				visited[t] = True
				t = q[t]
	return n - cnt <= m


for _ in range(int(input())):
	n, m = [int(x) for x in input().split()]
	p = [int(x) - 1 for x in input().split()]
	good_k = {}
	for i in range(n):
		k = (i - p[i] + n) % n
		good_k[k] = good_k[k] + 1 if k in good_k else 1
	ans = [k for k, v in good_k.items() if v >= n - 2 * m and solve(k)]
	ans.sort()
	print(len(ans), *ans)
