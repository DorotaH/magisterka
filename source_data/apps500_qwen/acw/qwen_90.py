n = int(input())
total_cost = sum((i + n) % (1 + n) for i in range(1, n))
print(total_cost)
