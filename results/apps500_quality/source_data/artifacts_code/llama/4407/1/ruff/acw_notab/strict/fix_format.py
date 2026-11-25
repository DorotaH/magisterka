import math
import sys

input = sys.stdin.readline


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def read_str():
    return input().strip()


def solve():
    n, q = read_ints()
    a = list(read_ints())
    a.sort(reverse=True)

    m = 31
    max_val = 2**m
    pow2 = [0] * (1 + max_val)
    for x in a:
        pow2[x] += 1

    for i in range(1, 1 + max_val):
        pow2[i] += pow2[i - 1]

    for _ in range(q):
        b = read_int()
        if b == 1:
            print(1)
        elif b > max_val:
            print(-1)
        else:
            power = math.floor(math.log2(b))
            ans = pow2[b] - pow2[b - 2**power]
            if ans < 0:
                ans = -1
            print(ans)


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
