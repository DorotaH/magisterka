n, x = map(int, input().split())
queue = list()
for _ in range(n):
    op, d = input().split()
    d = int(d)
    if not op == '+':
        if x >= d:
            x -= d
        else:
            queue.append(d)
    else:
        x += d

print(x, len(queue))