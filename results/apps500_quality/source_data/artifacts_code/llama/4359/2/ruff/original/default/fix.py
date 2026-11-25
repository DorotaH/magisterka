
# Read input from standard input
A, B, C, D, E = map(int, input().split())

# Calculate the earliest possible time for each dish
time = 0
order_times = []
for a in [A, B, C, D, E]:
    time += a
    order_times.append(time)

# Try all possible orders
min_last_delivery = 10 ** 5
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            for l in range(k + 1, 5):
                for m in range(l + 1, 5):
                    last_delivery = order_times[0]
                    for x in [i, j, k, l, m]:
                        last_delivery += (order_times[x] - order_times[x - 1]) - ((order_times[x] - order_times[x - 1]) % 10)
                        last_delivery += (order_times[x] - last_delivery)
                    min_last_delivery = min(min_last_delivery, last_delivery)

print(min_last_delivery)
