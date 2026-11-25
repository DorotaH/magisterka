import math

n = int(input())
arr = list(map(int, input().split()))

min_lcm = float('inf')
min_i, min_j = -1, -1
for i in range(n):
	for j in range(i + 1, n):
		lcm = abs(arr[j] * arr[i]) // math.gcd(arr[i], arr[j])
		if lcm < min_lcm:
			min_lcm = lcm
			min_i, min_j = i + 1, 1 + j

print(min_i, min_j)
