t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	n = 2 * abs(b - a)

	diff = abs(b - a)
	if a > n or b > n or c > n:
		print(-1)
		continue
	x1, x2 = diff + c, c - diff
	ans = -1
	if 1 <= x1 <= n:
		ans = diff + c
	if 1 <= x2 <= n:
		ans = c - diff
	print(ans)
