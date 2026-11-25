import  sys

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
s = int(data[2])

edges = list()
for i in range(3, 3 + 2 * m, 2):
    t=int(data[i])
    u = int(data[i + 1])
    v = int(data[i + 2])
    edges.append((t, u, v))


# Function to find the maximum number of reachable vertices
def max_reachable():
    from  collections import  deque

    visited, q = set(), deque([s])
    visited.add(s)
    for  t, u, v in  edges:
        if  1 == t or  u in  visited:
            q.append(v)
        if  1 == t or  v in  visited:
            q.append(u)
    return  len(visited)


# Function to find the minimum number of reachable vertices
def min_reachable():
    from  collections import  deque

    visited, q = set(), deque([s])
    visited.add(s)
    for  t, u, v in  edges:
        if  1 == t or  u not  in visited:
            q.append(v)
        if  1 == t or  v not  in visited:
            q.append(u)
    return  len(visited)


# Find the number of reachable vertices in the initial graph
max_reachable_count, min_reachable_count = max_reachable(), min_reachable()

# Find the directions for the maximum reachable vertices
max_directions = list()
for t, u, v in edges:
    if not t == 2:
        max_directions.append("-")
    else:
        max_directions.append("+")

# Find the directions for the minimum reachable vertices
min_directions = list()
for t, u, v in edges:
    if not t == 2:
        min_directions.append("+")
    else:
        min_directions.append("-")

# Output the results
print(max_reachable_count)
print("".join(max_directions))
print(min_reachable_count)
print("".join(min_directions))
