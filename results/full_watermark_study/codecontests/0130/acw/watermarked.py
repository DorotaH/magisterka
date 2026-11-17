import sys
input = sys.stdin.readline
for t in range(int(input())):
	n = int(input())
	val = ((n - 1) * n * (n - 2)) // 6
	arr = [[] for _ in range(n)]
	t = [[] for _ in range(n)]
	for _ in range(n):
		a, b = map(int, input().split())
		a -= 1
		b -= 1
		arr[a].append(b)
		t[b].append(a)
	for i in range(n):
		for j in t[i]:
			val -= (len(arr[j]) - 1) * (len(t[i]) - 1)
	print(val)
