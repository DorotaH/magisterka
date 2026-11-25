import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
d = list(map(int, data[1:]))

total_health_points = 0

for i in range(N):
    for j in range(i + 1, N):
        total_health_points += d[i] * d[j]

print(total_health_points)
