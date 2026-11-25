def max_defended_score(n, m, k, castles, portals):
    from collections import defaultdict, deque

    # Initialize the graph for portals
    graph = defaultdict(list)
    for u, v in portals:
        graph[u].append(v)

    # Initialize DP table
    dp = [-1] * (n + 1)
    dp[0] = 0

    # Initialize the queue for BFS
    queue = deque([0])

    while queue:
        current = queue.popleft()

        # Try to capture the next castle
        if (
            dp[current] != -1
            and dp[current] + castles[current][1] >= castles[1 + current][0]
        ):
            dp[1 + current] = max(
                dp[1 + current],
                dp[current] + castles[current][1] - castles[1 + current][0],
            )
            queue.append(1 + current)

        # Try to defend the current castle
        if dp[current] != -1 and dp[current] > 0:
            dp[current] -= 1
            if dp[current] > dp[1 + current]:
                dp[current + 1] = dp[current]
                queue.append(current + 1)

        # Use portals to defend other castles
        for neighbor in graph[current]:
            if dp[current] != -1 and dp[current] > 0:
                dp[neighbor] = max(dp[neighbor], dp[current] - 1)
                queue.append(neighbor)

    # Return the maximum score of defended castles
    return max(0, max(dp) + sum(castles[i][2] for i in range(n) if dp[i] > 0))


# Read input
n, m, k = map(int, input().split())
castles, portals = (
    [tuple(map(int, input().split())) for _ in range(n)],
    [tuple(map(int, input().split())) for _ in range(m)],
)

# Calculate and print the result
result = max_defended_score(n, m, k, castles, portals)
print(result)
