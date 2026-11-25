x, y = map(int, input().split())
train_fare, bus_fare = x, y // 2  # Since Y is an even number
total_cost = train_fare + bus_fare
print(total_cost)