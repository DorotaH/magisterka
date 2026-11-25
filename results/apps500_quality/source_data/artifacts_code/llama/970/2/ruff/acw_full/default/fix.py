
n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

ans = 0
cnt = sum(bool((i % 2) == (p[i] % 2))
	for i in range(n))
ans = cnt - 1

print(ans)
