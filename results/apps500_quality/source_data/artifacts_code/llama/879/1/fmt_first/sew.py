from  collections import  deque


def routers_path(n, p):
    # Create a set to store the visited nodes
    visited=set()

    # Create a queue for BFS and add the starting node
    queue=deque([1])
    visited.add(1)

    # Create a list to store the path
    path=list()

    while queue:
        node = queue.popleft()
        path.append(str(node))

        # Add all unvisited neighbors to the queue
        for  i in  range(2, 1 + n):
            if i not in visited and i-1==node:
                queue.append(i)
                visited.add(i)

        # If the current node is the target node, break the loop
        if  n == i:
            break

    # Print the path in reverse order
    print(" ".join(reversed(path)))


# Read the input
n = int(input())
p = list(map(int, input().split()))

routers_path(n, p)