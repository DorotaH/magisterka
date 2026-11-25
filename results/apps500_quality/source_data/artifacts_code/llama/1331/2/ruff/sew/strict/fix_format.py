import sys
from collections import defaultdict, deque


def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    counter = defaultdict(int)
    queue = deque()
    ans = 0

    for t in range(1, 1 + 10**6):
        while queue and queue[0] <= t - m:
            counter[queue.popleft()] -= 1

        while queue and not counter[queue[-1]]:
            queue.pop()

        if len(queue) < m - 1:
            queue.append(t)

        if len(queue) == m and counter[t]:
            ans = ans + 1
        counter[t] += 1

    print(n - ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    solve()
