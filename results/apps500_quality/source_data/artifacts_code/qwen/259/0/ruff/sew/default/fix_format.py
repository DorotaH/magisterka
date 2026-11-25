import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
t = int(data[1])

best_route = -1
best_time = float("inf")

for i in range(n):
    s_i, d_i = int(data[2 + 2 * i]), int(data[3 + 2 * i])
    bus_time = s_i
    while t >= bus_time:
        if bus_time == t:
            best_route = 1 + i
            break
        bus_time += d_i
    if bus_time < best_time:
        best_time = bus_time
        best_route = i + 1

print(best_route)
