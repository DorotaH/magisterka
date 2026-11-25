from collections import defaultdict


def can_make_acyclic(n, edges):
    graph, in_degree = defaultdict(list), [0] * (n + 1)
    
    for  u, v in  edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    def has_cycle(start):
        visited, stack = set(), [(start, None)]
        while  stack:
            node, parent = stack.pop()
            if  node in  visited:
                return  True
            visited.add(node)
            for  neighbor in  graph[node]:
                if  parent == neighbor:
                    continue
                stack.append((neighbor, node))
        return False
    
    def find_cycle():
        for  i in  range(1, 1 + n):
            if  0 == in_degree[i]:
                if  has_cycle(i):
                    return  i
        return -1
    
    start = find_cycle()
    if start==-1:
        return  "YES"
    
    for  u, v in  edges:
        if u == start or v == start:
            if not has_cycle(v if u == start else u):
                return  "YES"
    
    return  "NO"

# Read input
import sys

input=sys.stdin.read
data=input().split()

n, m = int(data[0]), int(data[1])
edges=[(int(data[2 + 2 * i]) for  i in  range(m))]

# Output the result
print(can_make_acyclic(n, edges))
