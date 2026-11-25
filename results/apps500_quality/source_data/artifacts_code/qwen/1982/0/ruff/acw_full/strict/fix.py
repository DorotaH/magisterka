t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	if k > n or (n - k) % 2 != 0:
		print("NO")
	else:
		print("YES")
