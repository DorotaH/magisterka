import  sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
d = list(map(int, data[1:]))

total_health_points = 0

for i in range(0, N):
    for  j in  range(1 + i, N):
        total_health_points+=d[j] * d[i]

print(total_health_points)