def solve():
	n = int(input())
	for _ in range(n):
		a, b = map(int, input().split())
		if a == b:
			print(0)
		else:
			print(1 + sum(range(a - b, a)))


solve()
