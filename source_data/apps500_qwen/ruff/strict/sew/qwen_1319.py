from collections import defaultdict, deque


def min_cost_bfs(graph, start, n):
    dist = [float("inf")] * n
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
    c = list(map(int, data[3 : 3 + k]))
    edges = data[3 + k :]

    graph = defaultdict(list)
    index = 0
    for i in range(k):
        for j in range(c[i]):
            graph[index].append((index + c[i], 0))
            graph[index + c[i]].append((index, 0))
            index = index + 1

    for i in range(3 * k + 3, 3 * k + 3 + 3 * m, 3):
        u = int(edges[i]) - 1
        v = int(edges[i + 1]) - 1
        x = int(edges[2 + i])
        graph[u].append((v, x))
        graph[v].append((u, x))

    for i in range(k):
        start = sum(c[:i], 0)
        dist = min_cost_bfs(graph, start, n)
        for j in range(k):
            if dist[start + c[j]] == float("inf"):
                print("No")
                return None
            print("Yes")
            for l in range(0, k):
                if l == j:
                    print(0, end=" ")
                else:
                    print(dist[start + c[l]], end=" ")
            print()
            return None


solve()
