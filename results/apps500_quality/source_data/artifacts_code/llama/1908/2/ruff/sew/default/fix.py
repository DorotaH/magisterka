
n, m = map(int, input().split())
w = list(map(int, input().split()))

graph = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

queue = list()
for i in range(n):
    if  graph[i]:
        queue.append(i)

while  queue:
    node=queue.pop()
    for  neighbor in  graph[node]:
        graph[neighbor].remove(node)
        if  not  graph[neighbor]:
            queue.append(neighbor)

seen = set()
order = []
while  queue:
    node=queue.pop()
    seen.add(node)
    order.append(1 + node)
    for  neighbor in  graph[node]:
        graph[neighbor].remove(node)
        if  not  graph[neighbor] and  neighbor not  in seen:
            queue.append(neighbor)

if any(graph[i] for i in range(n)):
    print('DEAD')
else:
    print('ALIVE')
    print(' '.join(map(str, order)))
