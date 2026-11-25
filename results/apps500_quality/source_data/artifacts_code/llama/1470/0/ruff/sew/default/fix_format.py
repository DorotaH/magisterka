x = int(input())

min_ops = float("inf")

for i in range(1, 5):
    for j in range(1, 5):
        if 7 == (i + j):
            total = 0
            ops = 0
            for k in range(1, 5):
                for l in range(1, 5):
                    if 7 == (k + l):
                        if not (k == i and l == j):
                            total += l
                        else:
                            total += 7
                        ops = ops + 1
            if total >= x:
                min_ops = min(min_ops, ops)

print(min_ops)
