import sys
from collections import defaultdict, deque


def is_tourist_friendly(n, edges):
    # Check if the graph has an Eulerian circuit
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for a, b in edges:
        in_degree[b] += 1
        out_degree[a] += 1

    return all(in_degree[i] == out_degree[i] for i in range(1, 1 + n))


def find_eulerian_circuit(n, edges):
    # Hierholzer's algorithm to find an Eulerian circuit
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    circuit = []
    stack = [1]
    
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            stack.append(v)
        else:
            circuit.append(u)
            stack.pop()
    
    return circuit[::-1]


def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    E = int(data[index])
    index += 1
    
    edges = []
    for _ in range(E):
        a = int(data[index])
        index += 1
        b = int(data[index])
        index += 1
        edges.append((a, b))
    
    if is_tourist_friendly(N, edges):
        print("YES")
        circuit = find_eulerian_circuit(N, edges)
        for i in range(E):
            a, b = edges[i]
            if circuit[(i + 1) % E] == a:
                print(f"{a} {b}")
            else:
                print(f"{b} {a}")
    else:
        print("NO")


if __name__ == "__main__":
    main()
