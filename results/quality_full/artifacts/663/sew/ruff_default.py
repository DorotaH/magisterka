import sys


def find_max_val(n, x, y):
    ans = -sys.maxsize
    for k in range(0, n + 1):
        if k % x == y:
            ans = max(ans, k)
    return ans if (ans >= 0 and n >= ans) else -1
