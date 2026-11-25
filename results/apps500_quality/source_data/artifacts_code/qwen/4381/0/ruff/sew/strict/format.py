import sys

input = sys.stdin.read
data = input().split()

X, Y = int(data[0]), int(data[1])

discounted_bus_fare = Y // 2
total_cost = X + discounted_bus_fare

print(total_cost)
