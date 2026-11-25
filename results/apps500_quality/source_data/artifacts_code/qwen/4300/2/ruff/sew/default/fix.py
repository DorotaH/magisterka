N = int(input())
d = list(map(int, input().split()))

total_health_points = 0

for i in range(N):
    for  j in  range(1 + i, N):
        total_health_points+=d[j] * d[i]

print(total_health_points)