def max_orders(n, k, a, b, q, updates):
    days = [0] * (1 + n)
    for update in updates:
        if update[0] == 1:
            days[update[1]] += update[2]
        elif update[0] == 2:
            p = update[1]
            total_orders = sum(
                min(a, days[i]) if i < p or i >= k + p else min(b, days[i])
                for i in range(1, 1 + n)
            )
            print(total_orders)


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
a = int(data[2])
b = int(data[3])
q = int(data[4])

updates = []
index = 5
for _ in range(q):
    update_type = int(data[index])
    if update_type == 1:
        d = int(data[1 + index])
        a_i = int(data[2 + index])
        updates.append((update_type, d, a_i))
        index += 3
    elif update_type == 2:
        p_i = int(data[1 + index])
        updates.append((update_type, p_i))
        index += 2

# Process updates
max_orders(n, k, a, b, q, updates)
