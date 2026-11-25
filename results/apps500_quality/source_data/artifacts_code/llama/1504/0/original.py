import sys

def min_steps(n, k, l1, r1, l2, r2):
    min_len = min(r1 - l1, r2 - l2)
    max_len = r1 + r2 - l1 - l2

    if k <= min_len:
        return k - l1 + l2
    else:
        return max(0, (k - min_len) // 2 + max_len)

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    l1, r1 = map(int, sys.stdin.readline().split())
    l2, r2 = map(int, sys.stdin.readline().split())

    print(min_steps(n, k, l1, r1, l2, r2))
