import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = 0

for i in range(n):
	for j in range(i, n):
		result += 0 if abs(a[i] - a[j]) <= 1 else a[i] - a[j]
print(result)
