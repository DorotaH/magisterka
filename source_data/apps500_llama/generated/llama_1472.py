import math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# Create a table G of size n × m
G = [[0] * (m + 1) for _ in range(n + 1)]

# Calculate GCD(i, j) for all 1 ≤ i ≤ n, 1 ≤ j ≤ m
for i in range(1, n + 1):
    for j in range(1, m + 1):
        G[i][j] = math.gcd(i, j)

# Check if the sequence a occurs in table G
for i in range(1, n + 1):
    for j in range(m - k + 1):
        if all(G[i][j + l] == a[l - 1] for l in range(1, k + 1)):
            print("YES")
            exit()

print("NO")
