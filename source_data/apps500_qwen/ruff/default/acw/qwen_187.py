import sys

input = sys.stdin.read
data = input().split()

X = int(data[0])
Y = int(data[1])

discounted_bus_fare = Y // 2
total_cost = discounted_bus_fare + X

print(total_cost)
