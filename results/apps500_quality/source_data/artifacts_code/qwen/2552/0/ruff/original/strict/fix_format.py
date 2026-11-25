from collections import defaultdict, deque


def check_happiness(n, m, p, h, roads):
    # Initialize the graph
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    # Initialize the queue for BFS
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True

    # Initialize the happiness array
    happiness = [0] * (n + 1)

    # Perform BFS to calculate the happiness
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if happiness[current] > 0:
                    happiness[neighbor] += 1
                queue.append(neighbor)

    # Check if the calculated happiness matches the given happiness
    for i in range(1, n + 1):
        if happiness[i] != h[i]:
            return "NO"

    return "YES"


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Process each test case
index = 0
t = int(data[index])
index += 1
results = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    p = list(map(int, data[index + 2 : index + 2 + n]))
    h = list(map(int, data[index + 2 + n : index + 2 + 2 * n]))
    roads = []
    for i in range(n - 1):
        x = int(data[index + 2 + 2 * n + 2 * i])
        y = int(data[index + 2 + 2 * n + 2 * i + 1])
        roads.append((x, y))
    index += 2 + 2 * n + 2 * (n - 1)
    results.append(check_happiness(n, m, p, h, roads))

# Print results
for result in results:
    print(result)
