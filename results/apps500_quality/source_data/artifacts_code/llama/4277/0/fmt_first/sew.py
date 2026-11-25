import sys

N, A, B = map(int, sys.stdin.readline().split())

# Calculate the minimum cost for the train
min_train_cost = N * A

# Calculate the minimum cost for the taxi
min_taxi_cost = min(N * A, B)

# The minimum total travel expense is the minimum of the train cost and the taxi cost
min_total_cost = min(min_train_cost, min_taxi_cost)

print(min_total_cost)