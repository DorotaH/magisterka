import math

n = int(input())
a = list(map(int, input().split()))

max_comb = 0
max_i, max_j = 0, 0

for i in range(n):
	for j in range(i + 1, n):
		comb = math.comb(a[i], a[j])
		if comb > max_comb:
			max_comb = comb
			max_i, max_j = i, j

print(a[max_i], a[max_j])
