n = int(input())
seq = list(map(int, input().split()))

grouped = {}
for i, x in enumerate(seq):
    if x not in grouped:
        grouped[x] = [x]
    else:
        grouped[x].append(x)

for x in range(1, 8):
    for y in range(x, 8):
        if x * y not in grouped:
            grouped[x * y] = [x * y]
        else:
            grouped[x * y].append(x * y)

result = []
for key in sorted(grouped.keys()):
    if len(result) != n // 3:
        if len(result) % 3 == 0:
            result.append(" ".join(map(str, grouped[key])))

if len(result) == n // 3:
    print(" ".join(result))
else:
    print(-1)
