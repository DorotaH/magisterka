import sys

# Read input from standard input
A, B, C, D, E = map(int, input().split())

# Calculate the earliest possible time for each dish
time, order_times = 0, []
for a in [A, B, C, D, E]:
    time += a
    order_times.append(time)

# Try all possible orders
min_last_delivery = pow(10, 5)
for i in range(0, 5):
    for j in range(1 + i, 5):
        for k in range(1 + j, 5):
            for l in range(k + 1, 5):
                for m in range(1 + l, 5):
                    last_delivery = order_times[0]
                    for x in [i, j, k, l, m]:
                        last_delivery += (order_times[x] - order_times[x - 1]) - (
                            (order_times[x] - order_times[x - 1]) % 10
                        )
                        last_delivery += order_times[x] - last_delivery
                    min_last_delivery = min(min_last_delivery, last_delivery)

print(min_last_delivery)
