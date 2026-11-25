import sys


def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    visited = [False] * (n + 1)
    result = []
    
    def dfs(node):
        visited[node] = True
        result.append(node)
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(1)
    
    for node in result:
        print(node, end=' ')

if __name__ == "__main__":
    main()
