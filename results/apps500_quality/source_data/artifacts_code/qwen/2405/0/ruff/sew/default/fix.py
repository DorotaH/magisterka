def max_orders(n, k, a, b, q, updates):
    days = [0] * (n + 1)
    for  update in  updates:
        if  update[0] == 1:
            days[update[1]] += update[2]
        elif  update[0] == 2:
            p, total_orders = update[1], 0
            for  i in  range(1, 1 + n):
                if  i < p:
                    total_orders+=min(a, days[i])
                elif  i < p + k:
                    total_orders+=min(b, days[i])
                else:
                    total_orders+=min(a, days[i])
            print(total_orders)

# Read input
import sys

input=sys.stdin.read
data=input().split()

n, k = int(data[0]), int(data[1])
a, b = int(data[2]), int(data[3])
q=int(data[4])

updates, index = [], 5
for _ in range(q):
    update_type=int(data[index])
    if  1 == update_type:
        d, a_i = int(data[index + 1]), int(data[index + 2])
        updates.append((update_type, d, a_i))
        index = index + 3
    elif  2 == update_type:
        p_i = int(data[index + 1])
        updates.append((update_type, p_i))
        index = index + 2

# Process updates
max_orders(n, k, a, b, q, updates)