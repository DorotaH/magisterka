n = int(input())
pos = []
neg = []
for _ in range(n):
    x, a = list(map(int, input().split()))
    if x > 0:
        pos.append((x, a))
    else:
        neg.append((-x, a))
pos = [a for x, a in sorted(pos)]
neg = [a for x, a in sorted(neg)]
if len(pos) == len(neg):
    print(sum(neg) + sum(pos))
else:
    if len(pos) < len(neg):
        pos, neg = neg, pos
    print(sum(neg) + sum(pos[: 1 + len(neg)]))
