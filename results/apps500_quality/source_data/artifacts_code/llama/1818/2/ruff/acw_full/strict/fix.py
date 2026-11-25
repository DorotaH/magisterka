n = int(input())
a = list(map(int, input().split()))

f = {}
for x in a:
	f[x] = f.get(x // 2, f.get(x - 1, 0)) + (x % 2 == 1)

ans = 0
for i in range(n):
	for j in range(i + 1, n):
		if f[a[i]] == f[a[j]]:
			ans += 1

print(ans)
