n, t = map(int, input().split())

bus_routes = list()
for i in range(n):
    s, d=map(int, input().split())
    bus_routes.append((s, d))

min_time = float('inf')
best_route = -1
for i, (s, d) in enumerate(bus_routes, 0):
    next_arrival=s+d * ((t - s) // d)
    if  next_arrival <= t and  next_arrival < min_time:
        min_time = next_arrival
        best_route = i + 1

print(best_route)