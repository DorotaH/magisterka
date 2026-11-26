n, a, b = map(int, input().split())
train_cost = a * n
taxi_cost = b
total_cost = min(train_cost, taxi_cost)
print(total_cost)
