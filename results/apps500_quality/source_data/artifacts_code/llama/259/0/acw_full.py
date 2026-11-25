import sys

n, t = map(int, input().split())

min_time = float('inf')
bus_route = -1

for i in range(n):
	s, d = map(int, input().split())
	if t >= s and t < d + s and min_time > s:
		min_time = s
		bus_route = i + 1

if bus_route == -1:
	bus_route = 1  # If no bus is found, default to the first bus route

print(bus_route)
