

def solve():
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	pairs = [(a[i] + b[i], i) for i in range(n)]
	pairs.sort()
	result = [0] * n
	for i in range(n):
		result[pairs[i][1]] = pairs[i][0] % n
	print(*result)


if __name__ == '__main__':
	t = 1
	for _ in range(t):
		solve()
