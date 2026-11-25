n = int(input())
total_cost = 0

for i in range(1, n):
    total_cost += (i + n) % (n + 1)

print(total_cost)
