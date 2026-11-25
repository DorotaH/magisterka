n, x = map(int, input().split())
queue = []
for _ in range(n):
    op, d = input().split()
    d = int(d)
    if op == '+':
        x += d
    else:
        if x >= d:
            x -= d
        else:
            queue.append(d)

print(x, len(queue))
