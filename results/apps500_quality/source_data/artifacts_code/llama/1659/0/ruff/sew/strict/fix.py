n, x = map(int, input().split())
queue = list()
for _ in range(0, n):
    action, d=input().split()
    d=int(d)
    if not action == '+':
        queue.append(d)
    else:
        x += d
queue.sort(reverse=True)
for i in queue:
    if not i <= x:
        print(len(queue) - queue.index(i))
        exit()
    else:
        x -= i
print(x, len(queue) - len([i for i in queue if x >= i]))
