import sys
import math


def solve():
	n, k, s, t = map(int, sys.stdin.readline().split())
	cars = []
	for _ in range(n):
		c, v = map(int, sys.stdin.readline().split())
		cars.append((c, v))

	gas_stations = list(map(int, sys.stdin.readline().split()))

	for i in range(len(gas_stations)):
		gas_stations[i] = (gas_stations[i], i)

	gas_stations.sort(key=lambda x: x[0])

	def check(car):
		v, c = car
		tank = c
		time = 0
		for i in range(len(gas_stations) - 1):
			dist = gas_stations[i + 1][0] - gas_stations[i][0]
			if dist <= tank:
				time += 2 * dist
				tank -= dist
			else:
				time += 2 * tank + (dist - tank)
				tank = 0
		dist = s - gas_stations[-1][0]
		if dist <= tank:
			time += 2 * dist
		elif 2 * tank + (dist - tank) <= t - time:
			time += 2 * tank + (dist - tank)
		else:
			return False
		return t >= time

	cars.sort(key=lambda x: x[0])
	for car in cars:
		if check(car):
			print(car[0])
			return

	print(-1)


solve()
