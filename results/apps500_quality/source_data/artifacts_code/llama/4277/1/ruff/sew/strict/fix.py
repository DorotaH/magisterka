n, a, b = map(int, input().split())
train_cost, taxi_cost = n * a, b
total_cost = min(train_cost, taxi_cost)
print(total_cost)
