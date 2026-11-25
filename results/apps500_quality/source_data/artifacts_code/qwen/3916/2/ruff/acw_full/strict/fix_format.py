from heapq import heappop, heappush
from math import factorial


def min_path_sum(n, k):
    # Calculate the factorial of each k_i
    factorials = [factorial(k_i) for k_i in k]

    # Initialize a dictionary to store the minimum distance to each node
    min_dist = {}
    pq = []

    # Add the initial node (1) with distance 0
    heappush(pq, (0, 1))

    while pq:
        dist, node = heappop(pq)

        # If the node has already been visited, skip it
        if node in min_dist:
            continue

        # Mark the node as visited and store the distance
        min_dist[node] = dist

        # Calculate the next nodes to visit
        for i in range(2, 1 + node):
            if node % i == 0 and i not in min_dist:
                heappush(pq, (dist + 1, i))

    return sum(min_dist[f] for f in factorials)


# Read input
n = int(input())
k = list(map(int, input().split()))

# Output the result
print(min_path_sum(n, k))
