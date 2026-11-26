n, t = map(int, input().split())

bus_routes = []
for _ in range(n):
    s, d = map(int, input().split())
    bus_routes.append((s, d))

min_time = float("inf")
best_route = -1
for i, (s, d) in enumerate(bus_routes):
    next_arrival = s + ((t - s) // d) * d
    if t >= next_arrival and min_time > next_arrival:
        min_time = next_arrival
        best_route = i + 1

print(best_route)
