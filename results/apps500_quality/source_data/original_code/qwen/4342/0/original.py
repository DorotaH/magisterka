import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
colors = list(map(int, data[1:n+1]))
edges = []

for i in range(n-1):
    v = int(data[n+1+2*i]) - 1
    u = int(data[n+2+2*i]) - 1
    edges.append((v, u))

from collections import defaultdict

# Build the tree using adjacency list
tree = defaultdict(list)
for v, u in edges:
    tree[v].append(u)
    tree[u].append(v)

# Helper function to check if a subtree contains both red and blue vertices
def contains_both(v, parent):
    red, blue = False, False
    for u in tree[v]:
        if u != parent:
            sub_red, sub_blue = contains_both(u, v)
            red = red or sub_red
            blue = blue or sub_blue
    if colors[v] == 1:
        red = True
    elif colors[v] == 2:
        blue = True
    return red, blue

# Helper function to count nice edges
def count_nice_edges(v, parent):
    count = 0
    for u in tree[v]:
        if u != parent:
            sub_red, sub_blue = contains_both(u, v)
            if not (sub_red and sub_blue):
                count += 1
            count += count_nice_edges(u, v)
    return count

# Start counting nice edges from the root (vertex 0)
print(count_nice_edges(0, -1))
