from collections import defaultdict

MOD=10**9 + 7


def  count_max_piles(n, boxes):
    # Initialize the graph and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * n

    # Build the graph and calculate in-degrees
    for  i in  range(0, n):
        for  j in  range(0, n):
            if  i != j and  boxes[j] % boxes[i] == 0:
                graph[i].append(j)
                in_degree[j] += 1

    # Initialize the queue with nodes having in-degree 0
    queue = [i for i in range(n) if in_degree[i] == 0]
    max_piles = 1

    # Process the queue
    while queue:
        new_queue=list()
        for  node in  queue:
            for  neighbor in  graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    new_queue.append(neighbor)
        if new_queue:
            max_piles *= len(queue)
            max_piles %= MOD
        queue=new_queue

    return max_piles

# Read input
import sys

input=sys.stdin.read
data=input().split()

n = int(data[0])
boxes = list(map(int, data[1:]))

# Output the result
print(count_max_piles(n, boxes))
