n = int(input())
p = list(map(int, input().split()))

inversions = 0
for i in range(n):
	for j in range(i + 1, n):
		if p[i] > p[j]:
			inversions += 1

ans = next((float('inf') for i in range(n) if p[i - 1] == i), inversions)
print(ans)
