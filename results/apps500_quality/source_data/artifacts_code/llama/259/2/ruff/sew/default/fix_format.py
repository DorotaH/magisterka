n, t = map(int, input().split())

min_bus_time = float("inf")
bus_route = 0

for i in range(n):
    s, d = map(int, input().split())
    if t >= s and t < s + d:
        if min_bus_time > s:
            min_bus_time, bus_route = s, i + 1

print(bus_route)
