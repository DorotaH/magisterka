n, t = map(int, input().split())

min_bus_time = float("inf")
bus_route = 0

for i in range(n):
    s, d = map(int, input().split())
    if s <= t and t < s + d:
        if s < min_bus_time:
            min_bus_time = s
            bus_route = i + 1

print(bus_route)
