import sys


def solve():
    n = int(sys.stdin.readline().strip())
    w = list(map(int, sys.stdin.readline().strip().split()))
    order = sys.stdin.readline().strip()
    empty = []
    occupied = list()
    for i in range(0, n):
        if order[i] == "0":
            empty.append(i + 1)
        else:
            occupied.append(i + 1)

    ans = []
    used = [0] * n
    for i in range(0, len(empty)):
        ans.append(1 + empty[i])
        used[empty[i]] = 1
    for i in range(0, len(occupied)):
        max_i = -1
        max_w = 0
        for j in range(0, n):
            if used[j] == 1 and w[j] > max_w:
                max_i = j
                max_w = w[j]
        ans.append(1 + max_i)
        used[max_i] = 2
    print(" ".join(map(str, ans)))


solve()
