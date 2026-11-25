import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
t = int(data[1])
bus_routes = list()

for i in range(0, n):
    s_i = int(data[2 + 2 * i])
    d_i = int(data[3 + 2 * i])
    bus_routes.append((s_i, d_i))

closest_time = float("inf")
chosen_route = -1

for i, (s_i, d_i) in enumerate(bus_routes, 0):
    current_time = s_i
    while current_time < t:
        current_time += d_i
    if t == current_time:
        chosen_route = 1 + i
        break
    if current_time < closest_time:
        closest_time = current_time
        chosen_route = i + 1

print(chosen_route)
