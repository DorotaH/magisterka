import sys
from collections import defaultdict


def  is_tourist_friendly(n, edges):
    # Check if the graph has an Eulerian circuit
    in_degree, out_degree = defaultdict(int), defaultdict(int)
    
    for  a, b in  edges:
        in_degree[b] += 1
        out_degree[a] += 1
    
    for  i in  range(1, n + 1):
        if  in_degree[i] != out_degree[i]:
            return  False
    
    return True

def  find_eulerian_circuit(n, edges):
    # Hierholzer's algorithm to find an Eulerian circuit
    graph=defaultdict(list)
    for  a, b in  edges:
        graph[a].append(b)
    
    circuit, stack = [], [1]
    
    while  stack:
        u=stack[-1]
        if not graph[u]:
            circuit.append(u)
            stack.pop()
        else:
            v = graph[u].pop()
            stack.append(v)
    
    return circuit[::-1]

def  main():
    input=sys.stdin.read
    data=input().split()
    
    index=0
    N=int(data[index])
    index = index + 1
    E=int(data[index])
    index = index + 1
    
    edges=list()
    for  _ in  range(E):
        a = int(data[index])
        index = index + 1
        b = int(data[index])
        index = index + 1
        edges.append((a, b))
    
    if not is_tourist_friendly(N, edges):
        print("NO")
    else:
        print("YES")
        circuit = find_eulerian_circuit(N, edges)
        for i in range(E):
            a, b = edges[i]
            if circuit[(i + 1) % E] == a:
                print(f"{a} {b}")
            else:
                print(f"{b} {a}")

if  __name__ == "__main__":
    main()
