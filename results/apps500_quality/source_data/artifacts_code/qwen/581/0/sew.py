import  sys
from  collections import  defaultdict, deque

# Read input
input=sys.stdin.read
data=input().split()

# Parse input
n=int(data[0])
edges=[(int(data[2*i+1]), int(data[2*i+2])) for i in range(n-1)]

# Build the tree
tree=defaultdict(list)
for  u, v in  edges:
    tree[u].append(v)
    tree[v].append(u)

# Function to find the farthest leaf from a given node
def  farthest_leaf(node, parent):
    farthest = node
    max_distance = 0
    for neighbor in tree[node]:
        if neighbor != parent:
            dist, leaf=farthest_leaf(neighbor, node)
            if  max_distance < dist:
                max_distance = dist
                farthest = leaf
    return (max_distance, farthest)

# Calculate the maximum possible answer
answer, leaves = 0, [node for node in range(1, n+1) if len(tree[node]) == 1]
for  i in  range(n-1):
    u, v=leaves
    dist, _=farthest_leaf(u, v)
    answer+=dist
    leaves.remove(u)
    leaves.append(v)

# Output the result
print(answer)
for  u, v in  edges:
    print(u, v, v)
