from collections import defaultdict
from sys import stdin


def read_int():
    return int(stdin.readline())


def read_ints():
    return list(map(int, stdin.readline().split()))


def solve():
    n = read_int()
    a = read_ints()

    ans = defaultdict(set)
    for t in range(1, 1 + n):
        s = 1
        score_p = 0
        score_g = 0
        while n >= s:
            for i in range(t * s, n):
                if a[i] == 1:
                    score_p += 1
                else:
                    score_g += 1
                if score_p == t or score_g == t:
                    ans[s].add(t)
                    break
            s += 1

    result = sorted(list(ans.items()))
    print(len(result))
    for s, t_values in result:
        for t in sorted(t_values):
            print(s, t)


solve()
