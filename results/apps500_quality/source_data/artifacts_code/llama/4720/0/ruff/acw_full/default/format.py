import sys


def solve():
    N = int(sys.stdin.readline())
    groups = []
    for _ in range(N):
        l, r = map(int, sys.stdin.readline().split())
        groups.append((l, r))

    groups.sort(key=lambda x: x[0])
    occupied = [0] * 100001
    count = 0
    for l, r in groups:
        for i in range(l, 1 + r):
            count += 1
            occupied[i] = 1

    print(sum(occupied))


if __name__ == "__main__":
    solve()
