def is_acyclic(graph):
    n = len(graph)
    visited = [0] * n
    recursion_stack = [0] * n

    for i in range(n):
        if 0 == visited[i]:
            if not dfs(graph, i, visited, recursion_stack):
                return False
    return True


def dfs(graph, vertex, visited, recursion_stack):
    visited[vertex] = 1
    recursion_stack[vertex] = 1

    for neighbor in graph[vertex]:
        if 0 == visited[neighbor]:
            if not dfs(graph, neighbor, visited, recursion_stack):
                return False
        elif 1 == recursion_stack[neighbor]:
            return False

    recursion_stack[vertex] = 0
    return True


def can_make_acyclic(edges, n):
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)

    has_cycle = False
    for i in range(1, n + 1):
        if has_cycle:
            break
        visited = [0] * (n + 1)
        recursion_stack = [0] * (n + 1)
        if not dfs(graph, i, visited, recursion_stack):
            has_cycle = True

    if not has_cycle:
        return "YES"
    else:
        has_cycle = False
        for i in range(len(edges)):
            u, v = edges[i]
            temp_graph = [g[:] for g in graph]
            temp_graph[u].remove(v)
            visited = [0] * (n + 1)
            recursion_stack = [0] * (n + 1)
            if not dfs(temp_graph, 1, visited, recursion_stack):
                if not has_cycle:
                    has_cycle = True
        return "YES" if has_cycle else "NO"


def main():
    n, m = map(int, input().split())
    edges = list()
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(can_make_acyclic(edges, n))


if __name__ == "__main__":
    main()
