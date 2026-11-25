from collections import defaultdict, deque


def is_tourist_friendly(N, roads):
    # Build the graph
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    out_degree = [0] * (N + 1)
    
    for a, b in roads:
        graph[a].append(b)
        in_degree[b] += 1
        out_degree[a] += 1
    
    # Check if the graph can be made tourist-friendly
    # There should be exactly 2 nodes with out_degree - in_degree = 1
    # And all other nodes should have out_degree - in_degree = 0
    start_nodes = [i for i in range(1, N + 1) if out_degree[i] - in_degree[i] == 1]
    end_nodes = [i for i in range(1, N + 1) if in_degree[i] - out_degree[i] == 1]
    
    if len(start_nodes) != 1 or len(end_nodes) != 1:
        return False
    
    start = start_nodes[0]
    end = end_nodes[0]
    
    # Check if there is a path from start to end
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return visited[end]

def solve(N, E, roads):
    if is_tourist_friendly(N, roads):
        return "YES", roads
    else:
        return "NO", []

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    E = int(data[index])
    index += 1
    
    roads = []
    for _ in range(E):
        a = int(data[index])
        index += 1
        b = int(data[index])
        index += 1
        roads.append((a, b))
    
    result, new_roads = solve(N, E, roads)
    print(result)
    if result == "YES":
        for road in new_roads:
            print(road[0], road[1])

if __name__ == "__main__":
    main()
