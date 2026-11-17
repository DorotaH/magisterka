import sys

input = sys.stdin.readline


# sys.setrecursionlimit(400000)
def I():
    return input().strip()


def II():
    return int(input().strip())


def LI():
    return [*map(int, input().strip().split())]


for _ in range(II()):
    a, b = LI()
    if a > b:
        print(0)
        continue
    get_bin = lambda x, n: format(x, "b").zfill(n)
    A, B = get_bin(a, 32), get_bin(1 + b, 32)
    ans = 32 * [0]
    for i in range(32):
        if A[i] == B[i]:
            continue
        if A[i] == "1":
            break
        ans[i] = 1
    print(int("".join([str(x) for x in ans]), 2))
