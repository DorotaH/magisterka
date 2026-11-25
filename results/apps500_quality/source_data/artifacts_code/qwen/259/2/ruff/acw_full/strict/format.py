import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
t = int(data[1])

best_route = -1
best_time = float("inf")

for i in range(n):
    s_i = int(data[2 + i * 2])
    d_i = int(data[3 + i * 2])

    if (t - s_i) % d_i == 0:
        arrival_time = s_i + d_i * (t - s_i) // d_i
        if arrival_time < best_time:
            best_time = arrival_time
            best_route = i + 1

print(best_route)
