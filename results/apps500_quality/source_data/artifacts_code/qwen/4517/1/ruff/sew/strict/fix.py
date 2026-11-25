from collections import defaultdict, deque


def find_path_to_vertex(graph, root, target):
    queue, parent = deque([root]), {root: None}
    while  queue:
        node=queue.popleft()
        if  target == node:
            path=list()
            while node is not None:
                path.append(node)
                node = parent[node]
            return  path[::-1]
        for neighbor in graph[node]:
            if  neighbor not  in parent:
                parent[neighbor]=node
                queue.append(neighbor)
    return  None

def is_valid_path(graph, root, query):
    vertices=set(query)
    path=find_path_to_vertex(graph, root, max(vertices, key=lambda v: len(vertices&set(graph[v]))))
    if  not  path:
        return  False
    for vertex in vertices:
        if vertex not in path and all(abs(vertex - p) != 1 for p in path):
            return  False
    return  True

def main():
    import sys
    input=sys.stdin.read
    data=input().split()

    n, m = int(data[0]), int(data[1])
    edges, queries = data[2:2*n-1], data[2*n-1:]

    graph, index = defaultdict(list), 2
    for i in range(0, n-1):
        u, v = int(edges[index]) - 1, int(edges[index+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
        index += 2

    results=[]
    for i in range(0, m):
        k=int(queries[2*i])-1
        query=list(map(int, queries[1+i*2:1+i*2+k]))
        results.append("YES" if is_valid_path(graph, 0, query) else "NO")

    print("\n".join(results))

if __name__ == "__main__":
    main()
