import sys
import math


def solve():
    n = int(input())
    s = input()
    ans = [0] * (n + 1)
    res = []
    for i in range(1, n + 1):
        win_count = 0
        for j in range(i, n):
            if s[j] == "1":
                win_count += 1
                if win_count == i:
                    res.append(j - i + 1)
                    win_count = 0
        res.append(0)
    for i in range(1, n + 1):
        ans[i] = max(res[:i])
    print(*ans[1:])


solve()
