x, y = map(int, input().split())
train_fare, bus_fare = x, y // 2  # Use integer division to get the quotient in integer
total_cost = train_fare + bus_fare
print(total_cost)
