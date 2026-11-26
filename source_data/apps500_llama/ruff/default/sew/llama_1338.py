import sys
import math
from collections import deque


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    max_val = max(a)
    max_x = max_val
    i = n - 1
    while 1:
        i = (i - 1) % n
        if a[i] < max_x / 2:
            max_x = max(a[i], max_x)
        else:
            break

    if max_x == max_val:
        print(*[-1] * n)
        return

    ans = [0] * n
    stack = deque()
    for i in range(n):
        stack.append(i)
        while stack and a[stack[-1]] < max(a[stack]) / 2:
            max_x = max(a[stack.pop()], max_x)

        if stack:
            cnt = len(stack)
            max_x = max(a[stack[-1], max_x])
            ans[i] = cnt + 1

    print(*ans)


if __name__ == "__main__":
    solve()
