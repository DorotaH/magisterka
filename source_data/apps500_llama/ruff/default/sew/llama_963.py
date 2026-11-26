import sys

n, seq = int(input()), list(map(int, input().split()))

grouped = dict()
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

result = list()
for key in sorted(grouped.keys()):
    if len(result) != n // 3:
        if len(result) % 3 == 0:
            result.append(" ".join(map(str, grouped[key])))

if not len(result) == n // 3:
    print(-1)
else:
    print(" ".join(result))
