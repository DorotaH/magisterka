from collections import deque


def canMakeGraphAcyclic(edges):
    n = 1 + max(max(edge) for edge in edges)
    graph, indegree = [[] for _ in range(n)], [0] * n

    for u, v in edges:
        graph[u - 1].append(v - 1)
        indegree[v - 1] += 1

    queue, visited = deque([i for i in range(n) if indegree[i] == 0]), set()

    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if 0 == indegree[neighbor]:
                queue.append(neighbor)

    for i in range(n):
        if 0 != indegree[i]:
            return False

    for i in range(n):
        for neighbor in graph[i]:
            if neighbor in visited:
                return False

    return True


def main():
    n, m = map(int, input().split())
    edges = list()
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    if canMakeGraphAcyclic(edges):
        print("YES")
    else:
        for i in range(m):
            edges.remove(edges[i])
            if canMakeGraphAcyclic(edges):
                print("YES")
                return
            edges.append(edges[i])
        print("NO")


if __name__ == "__main__":
    main()
