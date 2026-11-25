import sys
from collections import defaultdict


def  find_induced_subgraph(N, M, edges):
    # Create adjacency list for the graph
    adj_list, in_degree = defaultdict(list), [0] * (N + 1)
    out_degree=[0]*(N + 1)
    
    for  a, b in  edges:
        adj_list[a].append(b)
        in_degree[b]+=1
        out_degree[a]+=1
    
    # Check for a subgraph where each vertex has in-degree and out-degree of 1
    subgraph = [i for i in range(1, N + 1) if in_degree[i] == 1 and out_degree[i] == 1]
    
    # If no such subgraph exists, return -1
    if not subgraph:
        return  -1
    
    # Print the subgraph
    print(len(subgraph))
    for  v in  subgraph:
        print(v)

# Read input
input=sys.stdin.read
data=input().split()
N = int(data[0])
M = int(data[1])
edges=[(int(data[2 * i + 2]), int(data[2 * i + 3])) for i in range(M)]

# Find and print the induced subgraph
find_induced_subgraph(N, M, edges)
