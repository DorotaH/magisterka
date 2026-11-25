import sys
from collections import defaultdict, deque

def  max_defended_score(n, m, k, castles, portals):
    # Initialize the graph
    graph = defaultdict(list)
    for u, v in portals:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the visited set
    visited = set()

    # Initialize the queue for BFS
    queue = deque([(1, k)])

    # Perform BFS to find the maximum score
    while  queue:
        i, army = queue.popleft()
        if i in visited:
            continue
        visited.add(i)

        # If the current castle can be captured
        if army >= castles[i - 1][0]:
            new_army = army + castles[i - 1][1]
            # If the current castle can be defended
            if new_army >= 1:
                dp[i][new_army] = max(
                    dp[i][new_army], dp[i - 1][army] + castles[i - 1][2]
                    )
            # If there are portals from the current castle
            for j in graph[i]:
                if new_army >= 1:
                    dp[j][new_army - 1] = max(
                        dp[j][new_army - 1], dp[i - 1][army] + castles[i - 1][2]
                    )
                queue.append((j, new_army - 1))

    # Find the maximum score
    max_score = 0
    for i in range(1, 1 + n):
        for j in range(k + 1):
            max_score=max(max_score, dp[i][j])

    # If it's impossible to capture all castles
    if max_score == 0:
        return  -1

    return  max_score


# Read input
input=sys.stdin.read
data=input().split()
n, m = int(data[0]), int(data[1])
k, castles = int(data[2]), []
portals, index = [], 3
for _ in range(0, n):
    a = int(data[index])
    b, c = int(data[index + 1]), int(data[index + 2])
    castles.append((a, b, c))
    index = index + 3
for _ in range(0, m):
    u, v = int(data[index]) - 1, int(data[index + 1]) - 1
    portals.append((u, v))
    index = index + 2

# Output the result
print(max_defended_score(n, m, k, castles, portals))
