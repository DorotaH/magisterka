n = int(input())
total_cost = 0

for i in range(1, n):
    total_cost += (i + n) % (1 + n)

print(total_cost)
