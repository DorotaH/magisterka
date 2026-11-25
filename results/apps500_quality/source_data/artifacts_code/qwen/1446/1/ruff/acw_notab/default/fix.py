from collections import defaultdict, deque


def min_cost_bfs(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor, cost in graph[current]:
            if dist[neighbor] > dist[current] + cost:
                dist[neighbor] = dist[current] + cost
                queue.append(neighbor)
    return dist


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    c = list(map(int, data[3:k + 3]))
    edges = data[k + 3:]

    graph = defaultdict(list)
    index = 0
    for i in range(k):
        for _ in range(c[i]):
            graph[index].append((c[i] + index, 0))
            graph[c[i] + index].append((index, 0))
            index += 1

    for i in range(3 + k * 3, 3 + k * 3 + m * 3, 3):
        u = int(edges[i]) - 1
        v = int(edges[i + 1]) - 1
        x = int(edges[i + 2])
        graph[u].append((v, x))
        graph[v].append((u, x))

    for i in range(k):
        start = sum(c[:i])
        dist = min_cost_bfs(graph, start, n)
        for j in range(k):
            if dist[start + c[j]] == float('inf'):
                print('No')
                return
            print('Yes')
            for l in range(k):
                if l == j:
                    print(0, end=' ')
                else:
                    print(dist[start + c[l]], end=' ')
            print()
            return


solve()
