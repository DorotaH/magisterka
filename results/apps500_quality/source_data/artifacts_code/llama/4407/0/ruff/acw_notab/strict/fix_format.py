from collections import defaultdict


def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for x in a:
        d[x] += 1

    for x in sorted(d.keys()):
        d[x + x] += d[x]

    for x in sorted(d.keys(), reverse=True):
        for y in d.keys():
            if y >= x:
                d[y] = min(d[y], d[x] + d[y - x])

    for _ in range(q):
        b = int(input())
        if b in d:
            print(d[b])
        else:
            print(-1)


if __name__ == "__main__":
    solve()
