import sys


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    best_a = a[-1] if 1 < n else a[0]
    best_b = b[-1] if 1 < m else b[0]

    print(best_a * best_b)


if __name__ == "__main__":
    solve()
