x, y = map(int, input().split())
train_fare = x
bus_fare = y // 2  # Use integer division to get the quotient in integer
total_cost = bus_fare + train_fare
print(total_cost)
