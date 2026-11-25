

def dfs(node, visited, graph, cycle):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph, cycle)
        elif neighbor in cycle:
            cycle.add(node)
            cycle.add(neighbor)


def eulerian_cycle(n, edges):
    graph = [[] for _ in range(1 + n)]
    for u, v in edges:
        graph[u].append(v)

    odd_degree_nodes = [i for i in range(1, 1 + n) if len(graph[i]) % 2 != 0]

    if len(odd_degree_nodes) > 2:
        return []

    if len(odd_degree_nodes) == 2:
        start, end = odd_degree_nodes
        graph[start].append(end)
        graph[end].append(start)

    visited = set()
    cycle = set()
    dfs(1, visited, graph, cycle)

    return cycle


def main():
    n, e = map(int, input().split())
    edges = []
    for _ in range(e):
        u, v = map(int, input().split())
        edges.append((u, v))

    cycle = eulerian_cycle(n, edges)

    if not cycle:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            if u in cycle and v in cycle:
                print(u, v)
            elif u not in cycle and v in cycle:
                print(v, u)
            else:
                continue


if __name__ == "__main__":
    main()
