n = int(input())
d = list(map(int, input().split()))

total_health = 0
for i in range(n):
    for j in range(1 + i, n):
        total_health += d[j] * d[i]

print(total_health)
