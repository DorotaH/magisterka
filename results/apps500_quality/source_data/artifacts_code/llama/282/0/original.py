from collections import deque

def min_jumps(n, d, s):
    queue = deque([(1, 0)])
    visited = set([1])

    while queue:
        x, steps = queue.popleft()
        
        if x == n:
            return steps

        for jump in range(1, min(d, x) + 1):
            if x + jump <= n and s[x + jump] == '1' and (x + jump) not in visited:
                queue.append((x + jump, steps + 1))
                visited.add(x + jump)

    return -1

n, d = map(int, input().split())
s = input()

print(min_jumps(n, d, s))
