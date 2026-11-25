from collections import defaultdict
from sys import stdin


def solve():
    n = int(stdin.readline())
    s = stdin.readline().strip()

    d = defaultdict(int)
    for i in range(n):
        d[s[i]] += 1

    ans = 0
    for i in range(n):
        if d[s[i]] > 1:
            for j in range(i):
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    del d[s[j]]
            for j in range(i+1, n):
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    del d[s[j]]
            ans += 1

    if len(d) == 1:
        return -1

    return ans

print(solve())
