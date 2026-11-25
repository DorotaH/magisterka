import  math

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# Create a table G of size n × m
G = []
for _ in range(n + 1):
    G.append([0] * (m + 1))

# Calculate GCD(i, j) for all 1 ≤ i ≤ n, 1 ≤ j ≤ m
for  i in  range(1, 1 + n):
    for  j in  range(1, m + 1):
        G[i][j]=math.gcd(i, j)

# Check if the sequence a occurs in table G
for  i in  range(1, 1 + n):
    for  j in  range(0, m - k + 1):
        if all(a[l - 1] == G[i][j + l] for l in range(1, 1 + k)):
            print("YES")
            exit()

print("NO")