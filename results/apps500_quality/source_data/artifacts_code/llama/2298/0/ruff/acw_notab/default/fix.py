import sys

input = sys.stdin.readline


def solve():
    a, b, q = map(int, input().split())
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        if a == b:
            res.append(0)
        else:
            total = (r // b - (l - 1) // b) * (r % a != 0)
            if l % b != a:
                total += min(r // a, (r // b - (l - 1) // b) + 1)
            if r % a != 0:
                total += (l % b != 0) * (r // a - (r // b - (l - 1) // b) - 1)
            res.append(total)
    print(' '.join(map(str, res)))


t = int(input())
for _ in range(t):
    solve()
