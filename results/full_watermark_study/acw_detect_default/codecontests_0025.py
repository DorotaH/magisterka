for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	mx = -(10**9)
	for i in range(n - 1):
		mx = max(mx, l[i] * l[i + 1])
	print(mx)
