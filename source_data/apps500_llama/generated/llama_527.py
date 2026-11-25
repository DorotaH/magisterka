n = int(input())
d = list(map(int, input().split()))

total_health = 0
for i in range(n):
    for j in range(i + 1, n):
        total_health += d[i] * d[j]

print(total_health)
