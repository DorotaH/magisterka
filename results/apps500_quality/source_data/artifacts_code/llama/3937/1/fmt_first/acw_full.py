import math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# Create a table G of size n × m
G = [[0] * (1 + m) for _ in range(1 + n)]

# Calculate GCD(i, j) for all 1 ≤ i ≤ n, 1 ≤ j ≤ m
for i in range(1, 1 + n):
	for j in range(1, 1 + m):
		G[i][j] = math.gcd(i, j)

# Check if the sequence a occurs in table G
for i in range(1, 1 + n):
	for j in range(m - k + 1):
		if all(G[i][l + j] == a[l - 1] for l in range(1, k + 1)):
			print("YES")
			exit()

print("NO")
