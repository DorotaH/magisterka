n, x = map(int, input().split())
queue = []
for _ in range(n):
    action, d = input().split()
    d = int(d)
    if action == '+':
        x += d
    else:
        queue.append(d)
queue.sort(reverse=True)
for i in queue:
    if i <= x:
        x -= i
    else:
        print(len(queue) - queue.index(i))
        exit()
print(x, len(queue) - len([i for i in queue if i <= x]))
