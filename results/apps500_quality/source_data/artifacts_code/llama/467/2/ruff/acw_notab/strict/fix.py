from collections import deque


def solve(s):
    # Create a dictionary to store the tiles that each tile is adjacent to
    adj = {}
    for i in range(26):
        adj[chr(i + 65)] = set()
    for i in range(26):
        for j in range(26):
            if abs(i - j) in [1, 13] or max(i, j) == 0 or i == 12:
                adj[chr(i + 65)].add(chr(j + 65))
    for i in range(26):
        adj[chr(i + 65)].add(chr(65 + (i + 13) % 26))
    for c in s:
        adj[c].add(c)

    # Create a dictionary to store the visited tiles
    visited = {}
    for c in s:
        visited[c] = False

    # Create a queue for BFS and enqueue all tiles
    q = deque([(c, 0) for c in s])

    # Perform BFS
    while q:
        c, index = q.popleft()
        if not visited[c]:
            visited[c] = True
        elif index == 26:
            # We have found a path of length 26, so we can stop the BFS
            return
        for d in adj[c]:
            q.append((d, 1 + index))
    # If we have not found a path of length 26, then it is impossible
    return "Impossible"


s = input()
print(solve(s))
