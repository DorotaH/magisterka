x = int(input())

min_ops = float("inf")

for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) == 7:
            total = 0
            ops = 0
            for k in range(1, 5):
                for l in range(1, 5):
                    if (k + l) == 7:
                        if k == i and l == j:
                            total += 7
                        else:
                            total += l
                        ops += 1
            if total >= x:
                min_ops = min(min_ops, ops)

print(min_ops)
