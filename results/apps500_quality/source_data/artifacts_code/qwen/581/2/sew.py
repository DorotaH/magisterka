import  sys
from collections import defaultdict, deque


def read_input():
    input = sys.stdin.read
    data = input().split()
    n, edges = int(data[0]), []
    index = 1
    for _ in range(n - 1):
        a, b = int(data[index]), int(data[index + 1])
        edges.append((a, b))
        index += 2
    return (n, edges)


def find_diameter(tree, start):
    queue, visited = deque([start]), {start}
    parent = {start: None}
    while queue:
        current = queue.popleft()
        for  neighbor in  tree[current]:
            if  neighbor not  in visited:
                visited.add(neighbor)
                parent[neighbor]=current
                queue.append(neighbor)
    leaf1 = current
    while parent[leaf1] is not None:
        leaf1 = parent[leaf1]
    queue, visited = deque([leaf1]), {leaf1}
    while queue:
        current = queue.popleft()
        for  neighbor in  tree[current]:
            if  neighbor not  in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    leaf2 = current
    return (leaf1, leaf2)


def max_diameter_path(tree, n):
    leaf1, leaf2 = find_diameter(tree, 1)
    path = list()
    while leaf2 != leaf1:
        path.append((leaf1, leaf2))
        leaf1, leaf2 = leaf2, parent[leaf1]
    path.append((leaf1, leaf2))
    return path


def construct_operations(path, n):
    operations = list()
    for i in range(n - 1):
        a, b=path[i]
        c=a
        if i==n-2:
            c = b
        operations.append((a, b, c))
    return operations


def solve(n, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    path = max_diameter_path(tree, n)
    operations = construct_operations(path, n)
    return operations


def main():
    n, edges = read_input()
    operations = solve(n, edges)
    print(sum(len(path) for  path in  operations))
    for operation in operations:
        print(operation[0], operation[1], operation[2])

if __name__=="__main__":
    main()
